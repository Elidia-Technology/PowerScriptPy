"""
PowerScript to Python Transpiler - Converts PowerScript AST to Python AST and code
"""

import ast
from typing import List, Dict, Any, Optional, Union
from .ast_nodes import *
from .lexer import Token


class TranspilerError(Exception):
    """Exception raised during transpilation"""
    
    def __init__(self, message: str, node: Optional[ASTNode] = None):
        self.message = message
        self.node = node
        location_info = ""
        if node and node.location:
            location_info = f" at line {node.location.line}, column {node.location.column}"
        super().__init__(f"{message}{location_info}")


class Transpiler(ASTVisitor):
    """Transpiles PowerScript AST to Python AST and code"""
    
    def __init__(self):
        self.python_ast_nodes: List[ast.AST] = []
        self.current_class: Optional[str] = None
        self.imports: Dict[str, List[str]] = {}
        self.type_imports: List[str] = []
        self.runtime_checks_enabled = True
        self.strict_typing = True
    
    def transpile(self, powerscript_nodes: List[ASTNode]) -> ast.Module:
        """Transpile PowerScript AST to Python AST Module"""
        self.python_ast_nodes = []
        self.imports = {}
        self.type_imports = []
        
        # Process all nodes
        for node in powerscript_nodes:
            python_node = node.accept(self)
            if python_node:
                if isinstance(python_node, list):
                    self.python_ast_nodes.extend(python_node)
                else:
                    # Wrap expressions in ast.Expr for statement context
                    if isinstance(python_node, (ast.Call, ast.Name, ast.Constant, 
                                               ast.BinOp, ast.UnaryOp, ast.Compare,
                                               ast.BoolOp, ast.Attribute, ast.Subscript)):
                        python_node = ast.Expr(value=python_node)
                    self.python_ast_nodes.append(python_node)
        
        # Add necessary imports at the beginning
        import_nodes = self._generate_imports()
        all_nodes = import_nodes + self.python_ast_nodes
        
        # Create Python module
        module = ast.Module(body=all_nodes, type_ignores=[])
        
        # Fix missing locations
        ast.fix_missing_locations(module)
        
        return module
    
    def transpile_to_code(self, powerscript_nodes: List[ASTNode]) -> str:
        """Transpile PowerScript AST to Python source code"""
        module = self.transpile(powerscript_nodes)
        return ast.unparse(module)
    
    def _generate_imports(self) -> List[ast.AST]:
        """Generate necessary import statements"""
        imports = []
        
        # Add PowerScript built-ins import
        builtins_import = ast.ImportFrom(
            module='powerscript.runtime.builtins',
            names=[ast.alias(name='*', asname=None)],
            level=0
        )
        imports.append(builtins_import)
        
        # Add typing imports if needed
        if self.type_imports:
            typing_import = ast.ImportFrom(
                module='typing',
                names=[ast.alias(name=name, asname=None) for name in set(self.type_imports)],
                level=0
            )
            imports.append(typing_import)
        
        # Add asyncio if async functions are used
        if 'asyncio' in self.imports:
            asyncio_import = ast.Import(names=[ast.alias(name='asyncio', asname=None)])
            imports.append(asyncio_import)
        
        # Add runtime validation imports if needed
        if self.runtime_checks_enabled:
            beartype_import = ast.ImportFrom(
                module='beartype',
                names=[ast.alias(name='beartype', asname=None)],
                level=0
            )
            imports.append(beartype_import)
        
        return imports
    
    def visit_class(self, node: ClassNode) -> ast.ClassDef:
        """Visit class node"""
        self.current_class = node.name
        
        # Base classes
        bases = [ast.Name(id=base, ctx=ast.Load()) for base in node.base_classes]
        
        # Generic support
        if node.generic_params:
            self.type_imports.extend(['Generic', 'TypeVar'])
            # Add Generic as base class
            bases.append(ast.Name(id='Generic', ctx=ast.Load()))
            
            # Create TypeVar definitions
            for param in node.generic_params:
                type_var = ast.Assign(
                    targets=[ast.Name(id=param, ctx=ast.Store())],
                    value=ast.Call(
                        func=ast.Name(id='TypeVar', ctx=ast.Load()),
                        args=[ast.Constant(value=param)],
                        keywords=[]
                    )
                )
                self.python_ast_nodes.append(type_var)
        
        # Class body
        body = []
        
        # Add constructor if present
        if node.constructor:
            constructor_method = node.constructor.accept(self)
            body.append(constructor_method)
        
        # Add methods
        for method in node.methods:
            method_def = method.accept(self)
            body.append(method_def)
        
        # Add fields as class variables or in __init__
        for field in node.fields:
            if field.initializer and field.is_const:
                # Class constant
                field_assign = ast.Assign(
                    targets=[ast.Name(id=field.name, ctx=ast.Store())],
                    value=field.initializer.accept(self)
                )
                body.append(field_assign)
        
        # If no body, add pass
        if not body:
            body.append(ast.Pass())
        
        class_def = ast.ClassDef(
            name=node.name,
            bases=bases,
            keywords=[],
            decorator_list=self._get_class_decorators(node),
            body=body
        )
        
        self.current_class = None
        return class_def
    
    def visit_function(self, node: FunctionNode) -> ast.FunctionDef:
        """Visit function node"""
        # Handle constructor specially
        if node.is_constructor:
            return self._create_constructor(node)
        
        # Function arguments
        args = []
        defaults = []
        
        # Add self parameter for methods
        if self.current_class:
            args.append(ast.arg(arg='self', annotation=None))
        
        # Add parameters
        for param in node.parameters:
            arg_node = ast.arg(
                arg=param.name,
                annotation=self._get_type_annotation(param.param_type) if param.param_type else None
            )
            args.append(arg_node)
            
            if param.default_value:
                defaults.append(param.default_value.accept(self))
        
        # Function body
        body = []
        if node.body:
            for stmt in node.body.statements:
                stmt_node = stmt.accept(self)
                if stmt_node:
                    if isinstance(stmt_node, list):
                        body.extend(stmt_node)
                    else:
                        body.append(stmt_node)
        
        if not body:
            body.append(ast.Pass())
        
        # Create function
        func_class = ast.AsyncFunctionDef if node.is_async else ast.FunctionDef
        
        func_def = func_class(
            name=node.name,
            args=ast.arguments(
                posonlyargs=[],
                args=args,
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=defaults
            ),
            body=body,
            decorator_list=self._get_function_decorators(node),
            returns=self._get_type_annotation(node.return_type) if node.return_type else None
        )
        
        return func_def
    
    def _create_constructor(self, node: FunctionNode) -> ast.FunctionDef:
        """Create Python __init__ method from PowerScript constructor"""
        # Arguments
        args = [ast.arg(arg='self', annotation=None)]
        defaults = []
        
        for param in node.parameters:
            arg_node = ast.arg(
                arg=param.name,
                annotation=self._get_type_annotation(param.param_type) if param.param_type else None
            )
            args.append(arg_node)
            
            if param.default_value:
                defaults.append(param.default_value.accept(self))
        
        # Body
        body = []
        
        # Add parameter assignments to self
        for param in node.parameters:
            assignment = ast.Assign(
                targets=[ast.Attribute(
                    value=ast.Name(id='self', ctx=ast.Load()),
                    attr=param.name,
                    ctx=ast.Store()
                )],
                value=ast.Name(id=param.name, ctx=ast.Load())
            )
            body.append(assignment)
        
        # Add constructor body
        if node.body:
            for stmt in node.body.statements:
                stmt_node = stmt.accept(self)
                if stmt_node:
                    if isinstance(stmt_node, list):
                        body.extend(stmt_node)
                    else:
                        body.append(stmt_node)
        
        if not body:
            body.append(ast.Pass())
        
        return ast.FunctionDef(
            name='__init__',
            args=ast.arguments(
                posonlyargs=[],
                args=args,
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=defaults
            ),
            body=body,
            decorator_list=self._get_function_decorators(node),
            returns=None
        )
    
    def visit_parameter(self, node: ParameterNode) -> ast.arg:
        """Visit parameter node"""
        return ast.arg(
            arg=node.name,
            annotation=self._get_type_annotation(node.param_type) if node.param_type else None
        )
    
    def visit_variable(self, node: VariableNode) -> ast.Assign:
        """Visit variable node"""
        target = ast.Name(id=node.name, ctx=ast.Store())
        
        if node.initializer:
            value = node.initializer.accept(self)
        else:
            value = ast.Constant(value=None)
        
        return ast.Assign(targets=[target], value=value)
    
    def visit_identifier(self, node: IdentifierNode) -> ast.Name:
        """Visit identifier node"""
        return ast.Name(id=node.name, ctx=ast.Load())
    
    def visit_literal(self, node: LiteralNode) -> ast.Constant:
        """Visit literal node"""
        return ast.Constant(value=node.value)
    
    def visit_call(self, node: CallNode) -> ast.Call:
        """Visit call node"""
        func = node.callee.accept(self)
        args = [arg.accept(self) for arg in node.arguments]
        
        return ast.Call(func=func, args=args, keywords=[])
    
    def visit_binary_op(self, node: BinaryOpNode) -> Union[ast.BinOp, ast.Compare, ast.BoolOp, ast.Attribute, ast.Subscript]:
        """Visit binary operation node"""
        left = node.left.accept(self)
        right = node.right.accept(self)
        
        # Handle member access
        if node.operator == '.':
            return ast.Attribute(value=left, attr=right.id, ctx=ast.Load())
        
        # Handle array indexing
        if node.operator == '[]':
            return ast.Subscript(value=left, slice=right, ctx=ast.Load())
        
        # Handle comparison operators
        if node.operator in ['==', '!=', '<', '<=', '>', '>=']:
            op_map = {
                '==': ast.Eq(),
                '!=': ast.NotEq(),
                '<': ast.Lt(),
                '<=': ast.LtE(),
                '>': ast.Gt(),
                '>=': ast.GtE()
            }
            return ast.Compare(left=left, ops=[op_map[node.operator]], comparators=[right])
        
        # Handle logical operators
        if node.operator == '&&':
            return ast.BoolOp(op=ast.And(), values=[left, right])
        elif node.operator == '||':
            return ast.BoolOp(op=ast.Or(), values=[left, right])
        
        # Handle arithmetic operators
        op_map = {
            '+': ast.Add(),
            '-': ast.Sub(),
            '*': ast.Mult(),
            '/': ast.Div(),
            '%': ast.Mod(),
            '**': ast.Pow(),
            '&': ast.BitAnd(),
            '|': ast.BitOr(),
            '^': ast.BitXor(),
            '<<': ast.LShift(),
            '>>': ast.RShift()
        }
        
        if node.operator in op_map:
            return ast.BinOp(left=left, op=op_map[node.operator], right=right)
        
        raise TranspilerError(f"Unsupported binary operator: {node.operator}", node)
    
    def visit_unary_op(self, node: UnaryOpNode) -> ast.UnaryOp:
        """Visit unary operation node"""
        operand = node.operand.accept(self)
        
        op_map = {
            '-': ast.USub(),
            '+': ast.UAdd(),
            '!': ast.Not(),
            '~': ast.Invert()
        }
        
        if node.operator in op_map:
            return ast.UnaryOp(op=op_map[node.operator], operand=operand)
        
        raise TranspilerError(f"Unsupported unary operator: {node.operator}", node)
    
    def visit_assignment(self, node: AssignmentNode) -> ast.Assign:
        """Visit assignment node"""
        target = node.target.accept(self)
        value = node.value.accept(self)
        
        # Ensure target has Store context
        if isinstance(target, ast.Name):
            target.ctx = ast.Store()
        elif isinstance(target, ast.Attribute):
            target.ctx = ast.Store()
        elif isinstance(target, ast.Subscript):
            target.ctx = ast.Store()
        
        return ast.Assign(targets=[target], value=value)
    
    def visit_block(self, node: BlockNode) -> List[ast.AST]:
        """Visit block node"""
        statements = []
        for stmt in node.statements:
            stmt_node = stmt.accept(self)
            if stmt_node:
                if isinstance(stmt_node, list):
                    statements.extend(stmt_node)
                else:
                    statements.append(stmt_node)
        return statements
    
    def visit_return(self, node: ReturnNode) -> ast.Return:
        """Visit return node"""
        value = node.value.accept(self) if node.value else None
        return ast.Return(value=value)
    
    def visit_if(self, node: IfNode) -> ast.If:
        """Visit if node"""
        test = node.condition.accept(self)
        body = node.then_block.accept(self)
        orelse = node.else_block.accept(self) if node.else_block else []
        
        return ast.If(test=test, body=body, orelse=orelse)
    
    def visit_while(self, node: WhileNode) -> ast.While:
        """Visit while node"""
        test = node.condition.accept(self)
        body = node.body.accept(self)
        
        return ast.While(test=test, body=body, orelse=[])
    
    def visit_for(self, node: ForNode) -> ast.For:
        """Visit for node"""
        target = ast.Name(id=node.variable, ctx=ast.Store())
        iter_expr = node.iterable.accept(self)
        body = node.body.accept(self)
        
        return ast.For(target=target, iter=iter_expr, body=body, orelse=[])
    
    def visit_try(self, node: TryNode) -> ast.Try:
        """Visit try node"""
        # Try body
        body = []
        for stmt in node.try_block.statements:
            stmt_node = stmt.accept(self)
            if stmt_node:
                if isinstance(stmt_node, list):
                    body.extend(stmt_node)
                else:
                    body.append(stmt_node)
        
        # Catch handlers
        handlers = []
        for catch_clause in node.catch_clauses:
            handler = self._create_exception_handler(catch_clause)
            handlers.append(handler)
        
        # Finally block
        finalbody = []
        if node.finally_block:
            for stmt in node.finally_block.statements:
                stmt_node = stmt.accept(self)
                if stmt_node:
                    if isinstance(stmt_node, list):
                        finalbody.extend(stmt_node)
                    else:
                        finalbody.append(stmt_node)
        
        return ast.Try(body=body, handlers=handlers, orelse=[], finalbody=finalbody)
    
    def visit_catch(self, node: CatchNode) -> ast.ExceptHandler:
        """Visit catch node - this is handled by visit_try"""
        return self._create_exception_handler(node)
    
    def visit_throw(self, node: ThrowNode) -> ast.Raise:
        """Visit throw node"""
        exc = node.expression.accept(self)
        return ast.Raise(exc=exc, cause=None)
    
    def _create_exception_handler(self, catch_node: CatchNode) -> ast.ExceptHandler:
        """Create Python exception handler from catch node"""
        # Exception type
        exception_type = None
        if catch_node.exception_type:
            # Map PowerScript exception types to Python
            type_map = {
                'Error': 'Exception',
                'TypeError': 'TypeError', 
                'ValueError': 'ValueError',
                'RuntimeError': 'RuntimeError'
            }
            python_type = type_map.get(catch_node.exception_type, catch_node.exception_type)
            exception_type = ast.Name(id=python_type, ctx=ast.Load())
        
        # Exception name binding
        name = catch_node.exception_name
        
        # Handler body
        body = []
        for stmt in catch_node.body.statements:
            stmt_node = stmt.accept(self)
            if stmt_node:
                if isinstance(stmt_node, list):
                    body.extend(stmt_node)
                else:
                    body.append(stmt_node)
        
        if not body:
            body.append(ast.Pass())
        
        return ast.ExceptHandler(type=exception_type, name=name, body=body)
    
    def _get_type_annotation(self, type_str: Optional[str]) -> Optional[ast.AST]:
        """Convert PowerScript type annotation to Python AST"""
        if not type_str or not self.strict_typing:
            return None
        
        # Handle basic types
        type_map = {
            'string': 'str',
            'number': 'float',
            'integer': 'int', 
            'boolean': 'bool',
            'void': 'None'
        }
        
        if type_str in type_map:
            return ast.Name(id=type_map[type_str], ctx=ast.Load())
        
        # Handle generic types
        if '<' in type_str and '>' in type_str:
            self.type_imports.append('List')
            # Simple handling for List<T>
            base_type = type_str.split('<')[0]
            inner_type = type_str.split('<')[1].split('>')[0]
            
            if base_type.lower() == 'array' or base_type.lower() == 'list':
                return ast.Subscript(
                    value=ast.Name(id='List', ctx=ast.Load()),
                    slice=self._get_type_annotation(inner_type),
                    ctx=ast.Load()
                )
        
        # Handle optional types
        if type_str.endswith('?'):
            self.type_imports.append('Optional')
            base_type = type_str[:-1]
            return ast.Subscript(
                value=ast.Name(id='Optional', ctx=ast.Load()),
                slice=self._get_type_annotation(base_type),
                ctx=ast.Load()
            )
        
        # Default to the type name as is
        return ast.Name(id=type_str, ctx=ast.Load())
    
    def _get_class_decorators(self, node: ClassNode) -> List[ast.AST]:
        """Get decorators for class"""
        decorators = []
        
        if self.runtime_checks_enabled:
            decorators.append(ast.Name(id='beartype', ctx=ast.Load()))
        
        return decorators
    
    def _get_function_decorators(self, node: FunctionNode) -> List[ast.AST]:
        """Get decorators for function"""
        decorators = []
        
        # Add access modifier decorators
        if node.access_modifier == AccessModifier.PRIVATE:
            # Use name mangling for private methods
            pass  # Python handles this with __ prefix
        elif node.access_modifier == AccessModifier.PROTECTED:
            # Use single underscore convention
            pass
        
        if self.runtime_checks_enabled and not node.is_constructor:
            decorators.append(ast.Name(id='beartype', ctx=ast.Load()))
        
        return decorators


def transpile_file(powerscript_source: str, filename: str = "") -> str:
    """Convenience function to transpile PowerScript source to Python"""
    from .lexer import Lexer
    from .parser import Parser
    
    # Lex and parse
    lexer = Lexer(powerscript_source, filename)
    lexer.tokenize()
    
    parser = Parser(lexer)
    ast_nodes = parser.parse()
    
    # Transpile
    transpiler = Transpiler()
    return transpiler.transpile_to_code(ast_nodes)