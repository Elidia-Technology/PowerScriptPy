"""
Abstract Syntax Tree Node definitions for PowerScript
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any, Union
from dataclasses import dataclass
from enum import Enum


class NodeType(Enum):
    """AST Node types"""
    CLASS = "class"
    FUNCTION = "function"
    CONSTRUCTOR = "constructor"
    VARIABLE = "variable"
    EXPRESSION = "expression"
    BLOCK = "block"
    PARAMETER = "parameter"
    IDENTIFIER = "identifier"
    LITERAL = "literal"
    CALL = "call"
    ASSIGNMENT = "assignment"
    BINARY_OP = "binary_op"
    UNARY_OP = "unary_op"
    RETURN = "return"
    IF = "if"
    WHILE = "while"
    FOR = "for"


class AccessModifier(Enum):
    """Access modifier types"""
    PUBLIC = "public"
    PRIVATE = "private"
    PROTECTED = "protected"


@dataclass
class SourceLocation:
    """Source code location information"""
    line: int
    column: int
    filename: str = ""


class ASTNode(ABC):
    """Base class for all AST nodes"""
    
    def __init__(self, node_type: NodeType, location: Optional[SourceLocation] = None):
        self.node_type = node_type
        self.location = location
        self.parent: Optional['ASTNode'] = None
        self.children: List['ASTNode'] = []
    
    @abstractmethod
    def accept(self, visitor):
        """Accept a visitor for the visitor pattern"""
        pass
    
    def add_child(self, child: 'ASTNode'):
        """Add a child node"""
        child.parent = self
        self.children.append(child)
    
    def get_children(self) -> List['ASTNode']:
        """Get all child nodes"""
        return self.children.copy()


class ClassNode(ASTNode):
    """AST node for class declarations"""
    
    def __init__(self, name: str, base_classes: List[str] = None, 
                 generic_params: List[str] = None, location: Optional[SourceLocation] = None):
        super().__init__(NodeType.CLASS, location)
        self.name = name
        self.base_classes = base_classes or []
        self.generic_params = generic_params or []
        self.constructor: Optional['FunctionNode'] = None
        self.methods: List['FunctionNode'] = []
        self.fields: List['VariableNode'] = []
    
    def accept(self, visitor):
        return visitor.visit_class(self)


class FunctionNode(ASTNode):
    """AST node for function declarations"""
    
    def __init__(self, name: str, parameters: List['ParameterNode'] = None,
                 return_type: Optional[str] = None, is_async: bool = False,
                 access_modifier: AccessModifier = AccessModifier.PUBLIC,
                 is_constructor: bool = False, location: Optional[SourceLocation] = None):
        super().__init__(NodeType.CONSTRUCTOR if is_constructor else NodeType.FUNCTION, location)
        self.name = name
        self.parameters = parameters or []
        self.return_type = return_type
        self.is_async = is_async
        self.access_modifier = access_modifier
        self.is_constructor = is_constructor
        self.body: Optional['BlockNode'] = None
        self.generic_params: List[str] = []
    
    def accept(self, visitor):
        return visitor.visit_function(self)


class ParameterNode(ASTNode):
    """AST node for function parameters"""
    
    def __init__(self, name: str, param_type: Optional[str] = None,
                 default_value: Optional['ExpressionNode'] = None,
                 location: Optional[SourceLocation] = None):
        super().__init__(NodeType.PARAMETER, location)
        self.name = name
        self.param_type = param_type
        self.default_value = default_value
    
    def accept(self, visitor):
        return visitor.visit_parameter(self)


class VariableNode(ASTNode):
    """AST node for variable declarations"""
    
    def __init__(self, name: str, var_type: Optional[str] = None,
                 initializer: Optional['ExpressionNode'] = None,
                 is_const: bool = False, access_modifier: AccessModifier = AccessModifier.PUBLIC,
                 location: Optional[SourceLocation] = None):
        super().__init__(NodeType.VARIABLE, location)
        self.name = name
        self.var_type = var_type
        self.initializer = initializer
        self.is_const = is_const
        self.access_modifier = access_modifier
    
    def accept(self, visitor):
        return visitor.visit_variable(self)


class ExpressionNode(ASTNode):
    """Base class for expression nodes"""
    
    def __init__(self, node_type: NodeType = NodeType.EXPRESSION, location: Optional[SourceLocation] = None):
        super().__init__(node_type, location)


class IdentifierNode(ExpressionNode):
    """AST node for identifiers"""
    
    def __init__(self, name: str, location: Optional[SourceLocation] = None):
        super().__init__(NodeType.IDENTIFIER, location)
        self.name = name
    
    def accept(self, visitor):
        return visitor.visit_identifier(self)


class LiteralNode(ExpressionNode):
    """AST node for literal values"""
    
    def __init__(self, value: Any, literal_type: str, location: Optional[SourceLocation] = None):
        super().__init__(NodeType.LITERAL, location)
        self.value = value
        self.literal_type = literal_type  # "string", "number", "boolean", "null"
    
    def accept(self, visitor):
        return visitor.visit_literal(self)


class CallNode(ExpressionNode):
    """AST node for function calls"""
    
    def __init__(self, callee: ExpressionNode, arguments: List[ExpressionNode] = None,
                 location: Optional[SourceLocation] = None):
        super().__init__(NodeType.CALL, location)
        self.callee = callee
        self.arguments = arguments or []
    
    def accept(self, visitor):
        return visitor.visit_call(self)


class BinaryOpNode(ExpressionNode):
    """AST node for binary operations"""
    
    def __init__(self, left: ExpressionNode, operator: str, right: ExpressionNode,
                 location: Optional[SourceLocation] = None):
        super().__init__(NodeType.BINARY_OP, location)
        self.left = left
        self.operator = operator
        self.right = right
    
    def accept(self, visitor):
        return visitor.visit_binary_op(self)


class UnaryOpNode(ExpressionNode):
    """AST node for unary operations"""
    
    def __init__(self, operator: str, operand: ExpressionNode,
                 location: Optional[SourceLocation] = None):
        super().__init__(NodeType.UNARY_OP, location)
        self.operator = operator
        self.operand = operand
    
    def accept(self, visitor):
        return visitor.visit_unary_op(self)


class AssignmentNode(ExpressionNode):
    """AST node for assignments"""
    
    def __init__(self, target: ExpressionNode, value: ExpressionNode,
                 location: Optional[SourceLocation] = None):
        super().__init__(NodeType.ASSIGNMENT, location)
        self.target = target
        self.value = value
    
    def accept(self, visitor):
        return visitor.visit_assignment(self)


class BlockNode(ASTNode):
    """AST node for code blocks"""
    
    def __init__(self, statements: List[ASTNode] = None, location: Optional[SourceLocation] = None):
        super().__init__(NodeType.BLOCK, location)
        self.statements = statements or []
    
    def accept(self, visitor):
        return visitor.visit_block(self)


class ReturnNode(ASTNode):
    """AST node for return statements"""
    
    def __init__(self, value: Optional[ExpressionNode] = None, location: Optional[SourceLocation] = None):
        super().__init__(NodeType.RETURN, location)
        self.value = value
    
    def accept(self, visitor):
        return visitor.visit_return(self)


class IfNode(ASTNode):
    """AST node for if statements"""
    
    def __init__(self, condition: ExpressionNode, then_block: BlockNode,
                 else_block: Optional[BlockNode] = None, location: Optional[SourceLocation] = None):
        super().__init__(NodeType.IF, location)
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block
    
    def accept(self, visitor):
        return visitor.visit_if(self)


class WhileNode(ASTNode):
    """AST node for while loops"""
    
    def __init__(self, condition: ExpressionNode, body: BlockNode,
                 location: Optional[SourceLocation] = None):
        super().__init__(NodeType.WHILE, location)
        self.condition = condition
        self.body = body
    
    def accept(self, visitor):
        return visitor.visit_while(self)


class ForNode(ASTNode):
    """AST node for for loops"""
    
    def __init__(self, variable: str, iterable: ExpressionNode, body: BlockNode,
                 location: Optional[SourceLocation] = None):
        super().__init__(NodeType.FOR, location)
        self.variable = variable
        self.iterable = iterable
        self.body = body
    
    def accept(self, visitor):
        return visitor.visit_for(self)


# Visitor interface
class ASTVisitor(ABC):
    """Abstract base class for AST visitors"""
    
    @abstractmethod
    def visit_class(self, node: ClassNode): pass
    
    @abstractmethod  
    def visit_function(self, node: FunctionNode): pass
    
    @abstractmethod
    def visit_parameter(self, node: ParameterNode): pass
    
    @abstractmethod
    def visit_variable(self, node: VariableNode): pass
    
    @abstractmethod
    def visit_identifier(self, node: IdentifierNode): pass
    
    @abstractmethod
    def visit_literal(self, node: LiteralNode): pass
    
    @abstractmethod
    def visit_call(self, node: CallNode): pass
    
    @abstractmethod
    def visit_binary_op(self, node: BinaryOpNode): pass
    
    @abstractmethod
    def visit_unary_op(self, node: UnaryOpNode): pass
    
    @abstractmethod
    def visit_assignment(self, node: AssignmentNode): pass
    
    @abstractmethod
    def visit_block(self, node: BlockNode): pass
    
    @abstractmethod
    def visit_return(self, node: ReturnNode): pass
    
    @abstractmethod
    def visit_if(self, node: IfNode): pass
    
    @abstractmethod
    def visit_while(self, node: WhileNode): pass
    
    @abstractmethod
    def visit_for(self, node: ForNode): pass