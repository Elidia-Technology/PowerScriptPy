"""
PowerScript Parser - Builds AST from tokens
"""

from typing import List, Optional, Dict, Any, Union
from .lexer import Lexer, Token, TokenType
from .ast_nodes import *


class ParseError(Exception):
    """Exception raised during parsing"""
    
    def __init__(self, message: str, token: Token):
        self.message = message
        self.token = token
        super().__init__(f"{message} at line {token.location.line}, column {token.location.column}")


class Parser:
    """PowerScript recursive descent parser"""
    
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.tokens = lexer.get_tokens()
        self.current = 0
    
    def parse(self) -> List[ASTNode]:
        """Parse tokens into AST"""
        statements = []
        
        while not self._is_at_end():
            stmt = self._declaration()
            if stmt:
                statements.append(stmt)
        
        return statements
    
    def _declaration(self) -> Optional[ASTNode]:
        """Parse top-level declarations"""
        try:
            if self._match(TokenType.CLASS):
                return self._class_declaration()
            elif self._match(TokenType.FUNCTION):
                return self._function_declaration()
            elif self._match(TokenType.ASYNC):
                if self._check(TokenType.FUNCTION):
                    return self._function_declaration(is_async=True)
                else:
                    self._error("Expected 'function' after 'async'")
            elif self._match(TokenType.LET, TokenType.CONST):
                return self._variable_declaration()
            else:
                return self._statement()
        except ParseError as e:
            self._synchronize()
            raise e
    
    def _class_declaration(self) -> ClassNode:
        """Parse class declaration"""
        name_token = self._consume(TokenType.IDENTIFIER, "Expected class name")
        name = name_token.value
        
        # Generic parameters
        generic_params = []
        if self._check(TokenType.LESS_THAN):
            generic_params = self._generic_parameters()
        
        # Base classes
        base_classes = []
        if self._match(TokenType.COLON):  # Using : for inheritance
            base_classes.append(self._consume(TokenType.IDENTIFIER, "Expected base class name").value)
            while self._match(TokenType.COMMA):
                base_classes.append(self._consume(TokenType.IDENTIFIER, "Expected base class name").value)
        
        self._consume(TokenType.LEFT_BRACE, "Expected '{' after class declaration")
        
        class_node = ClassNode(name, base_classes, generic_params, name_token.location)
        
        # Parse class body
        while not self._check(TokenType.RIGHT_BRACE) and not self._is_at_end():
            access_modifier = AccessModifier.PUBLIC
            
            # Check for access modifiers
            if self._match(TokenType.PRIVATE):
                access_modifier = AccessModifier.PRIVATE
            elif self._match(TokenType.PROTECTED):
                access_modifier = AccessModifier.PROTECTED
            elif self._match(TokenType.PUBLIC):
                access_modifier = AccessModifier.PUBLIC
            
            if self._check(TokenType.CONSTRUCTOR):
                constructor = self._constructor_declaration(access_modifier)
                class_node.constructor = constructor
            elif self._check(TokenType.FUNCTION) or self._check(TokenType.ASYNC):
                method = self._method_declaration(access_modifier)
                class_node.methods.append(method)
            elif self._check(TokenType.LET) or self._check(TokenType.CONST):
                field = self._field_declaration(access_modifier)
                class_node.fields.append(field)
            else:
                self._error("Expected constructor, method, or field declaration")
        
        self._consume(TokenType.RIGHT_BRACE, "Expected '}' after class body")
        return class_node
    
    def _constructor_declaration(self, access_modifier: AccessModifier) -> FunctionNode:
        """Parse constructor declaration"""
        self._consume(TokenType.CONSTRUCTOR, "Expected 'constructor'")
        
        parameters = self._parameters()
        
        self._consume(TokenType.LEFT_BRACE, "Expected '{' after constructor parameters")
        body = self._block()
        
        constructor = FunctionNode("__init__", parameters, None, False, access_modifier, True, self._previous().location)
        constructor.body = body
        return constructor
    
    def _method_declaration(self, access_modifier: AccessModifier) -> FunctionNode:
        """Parse method declaration"""
        is_async = self._match(TokenType.ASYNC)
        self._consume(TokenType.FUNCTION, "Expected 'function'")
        
        name_token = self._consume(TokenType.IDENTIFIER, "Expected method name")
        name = name_token.value
        
        # Generic parameters
        generic_params = []
        if self._check(TokenType.LESS_THAN):
            generic_params = self._generic_parameters()
        
        parameters = self._parameters()
        
        # Return type
        return_type = None
        if self._match(TokenType.COLON):
            return_type = self._type_annotation()
        
        self._consume(TokenType.LEFT_BRACE, "Expected '{' after method signature")
        body = self._block()
        
        method = FunctionNode(name, parameters, return_type, is_async, access_modifier, False, name_token.location)
        method.generic_params = generic_params
        method.body = body
        return method
    
    def _field_declaration(self, access_modifier: AccessModifier) -> VariableNode:
        """Parse field declaration"""
        is_const = self._match(TokenType.CONST)
        if not is_const:
            self._consume(TokenType.LET, "Expected 'let' or 'const'")
        
        name_token = self._consume(TokenType.IDENTIFIER, "Expected field name")
        name = name_token.value
        
        # Type annotation
        field_type = None
        if self._match(TokenType.COLON):
            field_type = self._type_annotation()
        
        # Initializer
        initializer = None
        if self._match(TokenType.ASSIGN):
            initializer = self._expression()
        
        self._consume(TokenType.SEMICOLON, "Expected ';' after field declaration")
        
        return VariableNode(name, field_type, initializer, is_const, access_modifier, name_token.location)
    
    def _function_declaration(self, is_async: bool = False) -> FunctionNode:
        """Parse function declaration"""
        if not is_async:
            self._consume(TokenType.FUNCTION, "Expected 'function'")
        
        name_token = self._consume(TokenType.IDENTIFIER, "Expected function name")
        name = name_token.value
        
        # Generic parameters
        generic_params = []
        if self._check(TokenType.LESS_THAN):
            generic_params = self._generic_parameters()
        
        parameters = self._parameters()
        
        # Return type
        return_type = None
        if self._match(TokenType.COLON):
            return_type = self._type_annotation()
        
        self._consume(TokenType.LEFT_BRACE, "Expected '{' after function signature")
        body = self._block()
        
        function = FunctionNode(name, parameters, return_type, is_async, AccessModifier.PUBLIC, False, name_token.location)
        function.generic_params = generic_params
        function.body = body
        return function
    
    def _variable_declaration(self) -> VariableNode:
        """Parse variable declaration"""
        is_const = self._previous().type == TokenType.CONST
        
        name_token = self._consume(TokenType.IDENTIFIER, "Expected variable name")
        name = name_token.value
        
        # Type annotation
        var_type = None
        if self._match(TokenType.COLON):
            var_type = self._type_annotation()
        
        # Initializer
        initializer = None
        if self._match(TokenType.ASSIGN):
            initializer = self._expression()
        elif is_const:
            self._error("Const variables must be initialized")
        
        self._consume(TokenType.SEMICOLON, "Expected ';' after variable declaration")
        
        return VariableNode(name, var_type, initializer, is_const, AccessModifier.PUBLIC, name_token.location)
    
    def _parameters(self) -> List[ParameterNode]:
        """Parse function parameters"""
        self._consume(TokenType.LEFT_PAREN, "Expected '(' before parameters")
        
        parameters = []
        if not self._check(TokenType.RIGHT_PAREN):
            parameters.append(self._parameter())
            while self._match(TokenType.COMMA):
                parameters.append(self._parameter())
        
        self._consume(TokenType.RIGHT_PAREN, "Expected ')' after parameters")
        return parameters
    
    def _parameter(self) -> ParameterNode:
        """Parse single parameter"""
        name_token = self._consume(TokenType.IDENTIFIER, "Expected parameter name")
        name = name_token.value
        
        # Type annotation
        param_type = None
        if self._match(TokenType.COLON):
            param_type = self._type_annotation()
        
        # Default value
        default_value = None
        if self._match(TokenType.ASSIGN):
            default_value = self._expression()
        
        return ParameterNode(name, param_type, default_value, name_token.location)
    
    def _generic_parameters(self) -> List[str]:
        """Parse generic type parameters"""
        self._consume(TokenType.LESS_THAN, "Expected '<' for generic parameters")
        
        params = []
        params.append(self._consume(TokenType.IDENTIFIER, "Expected generic parameter name").value)
        
        while self._match(TokenType.COMMA):
            params.append(self._consume(TokenType.IDENTIFIER, "Expected generic parameter name").value)
        
        self._consume(TokenType.GREATER_THAN, "Expected '>' after generic parameters")
        return params
    
    def _type_annotation(self) -> str:
        """Parse type annotation"""
        type_name = self._consume(TokenType.IDENTIFIER, "Expected type name").value
        
        # Handle generic types like Array<T>
        if self._match(TokenType.LESS_THAN):
            type_name += "<"
            type_name += self._type_annotation()
            while self._match(TokenType.COMMA):
                type_name += ", " + self._type_annotation()
            self._consume(TokenType.GREATER_THAN, "Expected '>' after generic type parameters")
            type_name += ">"
        
        # Handle array types
        while self._match(TokenType.LEFT_BRACKET):
            self._consume(TokenType.RIGHT_BRACKET, "Expected ']' after '['")
            type_name += "[]"
        
        # Handle optional types
        if self._match(TokenType.QUESTION):
            type_name += "?"
        
        return type_name
    
    def _statement(self) -> ASTNode:
        """Parse statement"""
        if self._match(TokenType.IF):
            return self._if_statement()
        elif self._match(TokenType.WHILE):
            return self._while_statement()
        elif self._match(TokenType.FOR):
            return self._for_statement()
        elif self._match(TokenType.RETURN):
            return self._return_statement()
        elif self._match(TokenType.LEFT_BRACE):
            return BlockNode(self._block().statements, self._previous().location)
        else:
            return self._expression_statement()
    
    def _if_statement(self) -> IfNode:
        """Parse if statement"""
        self._consume(TokenType.LEFT_PAREN, "Expected '(' after 'if'")
        condition = self._expression()
        self._consume(TokenType.RIGHT_PAREN, "Expected ')' after if condition")
        
        then_block = self._statement_as_block()
        
        else_block = None
        if self._match(TokenType.ELSE):
            else_block = self._statement_as_block()
        
        return IfNode(condition, then_block, else_block, condition.location)
    
    def _while_statement(self) -> WhileNode:
        """Parse while statement"""
        self._consume(TokenType.LEFT_PAREN, "Expected '(' after 'while'")
        condition = self._expression()
        self._consume(TokenType.RIGHT_PAREN, "Expected ')' after while condition")
        
        body = self._statement_as_block()
        return WhileNode(condition, body, condition.location)
    
    def _for_statement(self) -> ForNode:
        """Parse for statement"""
        self._consume(TokenType.LEFT_PAREN, "Expected '(' after 'for'")
        
        variable = self._consume(TokenType.IDENTIFIER, "Expected variable name in for loop").value
        self._consume(TokenType.IN, "Expected 'in' in for loop")
        iterable = self._expression()
        
        self._consume(TokenType.RIGHT_PAREN, "Expected ')' after for clause")
        
        body = self._statement_as_block()
        return ForNode(variable, iterable, body, iterable.location)
    
    def _return_statement(self) -> ReturnNode:
        """Parse return statement"""
        location = self._previous().location
        
        value = None
        if not self._check(TokenType.SEMICOLON) and not self._is_at_end():
            value = self._expression()
        
        self._consume(TokenType.SEMICOLON, "Expected ';' after return value")
        return ReturnNode(value, location)
    
    def _statement_as_block(self) -> BlockNode:
        """Convert statement to block if needed"""
        if self._check(TokenType.LEFT_BRACE):
            self._advance()
            return self._block()
        else:
            stmt = self._statement()
            return BlockNode([stmt], stmt.location)
    
    def _block(self) -> BlockNode:
        """Parse block statement (assumes { already consumed)"""
        statements = []
        location = self._previous().location
        
        while not self._check(TokenType.RIGHT_BRACE) and not self._is_at_end():
            stmt = self._declaration()
            if stmt:
                statements.append(stmt)
        
        self._consume(TokenType.RIGHT_BRACE, "Expected '}' after block")
        return BlockNode(statements, location)
    
    def _expression_statement(self) -> ASTNode:
        """Parse expression statement"""
        expr = self._expression()
        self._consume(TokenType.SEMICOLON, "Expected ';' after expression")
        return expr
    
    def _expression(self) -> ExpressionNode:
        """Parse expression"""
        return self._assignment()
    
    def _assignment(self) -> ExpressionNode:
        """Parse assignment expression"""
        expr = self._or()
        
        if self._match(TokenType.ASSIGN, TokenType.PLUS_ASSIGN, TokenType.MINUS_ASSIGN):
            operator = self._previous()
            value = self._assignment()
            
            if isinstance(expr, IdentifierNode):
                return AssignmentNode(expr, value, operator.location)
            
            self._error("Invalid assignment target")
        
        return expr
    
    def _or(self) -> ExpressionNode:
        """Parse logical OR expression"""
        expr = self._and()
        
        while self._match(TokenType.OR):
            operator = self._previous()
            right = self._and()
            expr = BinaryOpNode(expr, operator.value, right, operator.location)
        
        return expr
    
    def _and(self) -> ExpressionNode:
        """Parse logical AND expression"""
        expr = self._equality()
        
        while self._match(TokenType.AND):
            operator = self._previous()
            right = self._equality()
            expr = BinaryOpNode(expr, operator.value, right, operator.location)
        
        return expr
    
    def _equality(self) -> ExpressionNode:
        """Parse equality expression"""
        expr = self._comparison()
        
        while self._match(TokenType.EQUAL, TokenType.NOT_EQUAL):
            operator = self._previous()
            right = self._comparison()
            expr = BinaryOpNode(expr, operator.value, right, operator.location)
        
        return expr
    
    def _comparison(self) -> ExpressionNode:
        """Parse comparison expression"""
        expr = self._term()
        
        while self._match(TokenType.GREATER_THAN, TokenType.GREATER_EQUAL, 
                          TokenType.LESS_THAN, TokenType.LESS_EQUAL):
            operator = self._previous()
            right = self._term()
            expr = BinaryOpNode(expr, operator.value, right, operator.location)
        
        return expr
    
    def _term(self) -> ExpressionNode:
        """Parse term expression (+ -)"""
        expr = self._factor()
        
        while self._match(TokenType.MINUS, TokenType.PLUS):
            operator = self._previous()
            right = self._factor()
            expr = BinaryOpNode(expr, operator.value, right, operator.location)
        
        return expr
    
    def _factor(self) -> ExpressionNode:
        """Parse factor expression (* / %)"""
        expr = self._unary()
        
        while self._match(TokenType.DIVIDE, TokenType.MULTIPLY, TokenType.MODULO):
            operator = self._previous()
            right = self._unary()
            expr = BinaryOpNode(expr, operator.value, right, operator.location)
        
        return expr
    
    def _unary(self) -> ExpressionNode:
        """Parse unary expression"""
        if self._match(TokenType.NOT, TokenType.MINUS, TokenType.PLUS):
            operator = self._previous()
            right = self._unary()
            return UnaryOpNode(operator.value, right, operator.location)
        
        return self._call()
    
    def _call(self) -> ExpressionNode:
        """Parse function call expression"""
        expr = self._primary()
        
        while True:
            if self._match(TokenType.LEFT_PAREN):
                expr = self._finish_call(expr)
            elif self._match(TokenType.DOT):
                name = self._consume(TokenType.IDENTIFIER, "Expected property name after '.'")
                expr = BinaryOpNode(expr, ".", IdentifierNode(name.value, name.location), name.location)
            elif self._match(TokenType.LEFT_BRACKET):
                index = self._expression()
                self._consume(TokenType.RIGHT_BRACKET, "Expected ']' after index")
                expr = BinaryOpNode(expr, "[]", index, expr.location)
            else:
                break
        
        return expr
    
    def _finish_call(self, callee: ExpressionNode) -> CallNode:
        """Finish parsing function call"""
        arguments = []
        
        if not self._check(TokenType.RIGHT_PAREN):
            arguments.append(self._expression())
            while self._match(TokenType.COMMA):
                if len(arguments) >= 255:
                    self._error("Can't have more than 255 arguments")
                arguments.append(self._expression())
        
        paren = self._consume(TokenType.RIGHT_PAREN, "Expected ')' after arguments")
        return CallNode(callee, arguments, paren.location)
    
    def _primary(self) -> ExpressionNode:
        """Parse primary expression"""
        if self._match(TokenType.BOOLEAN):
            value = self._previous().value == "true"
            return LiteralNode(value, "boolean", self._previous().location)
        
        if self._match(TokenType.NULL):
            return LiteralNode(None, "null", self._previous().location)
        
        if self._match(TokenType.NUMBER):
            value = self._previous().value
            # Convert to int or float
            if '.' in value:
                return LiteralNode(float(value), "number", self._previous().location)
            else:
                return LiteralNode(int(value), "number", self._previous().location)
        
        if self._match(TokenType.STRING):
            value = self._previous().value
            # Remove quotes
            value = value[1:-1]
            return LiteralNode(value, "string", self._previous().location)
        
        if self._match(TokenType.IDENTIFIER):
            return IdentifierNode(self._previous().value, self._previous().location)
        
        if self._match(TokenType.LEFT_PAREN):
            expr = self._expression()
            self._consume(TokenType.RIGHT_PAREN, "Expected ')' after expression")
            return expr
        
        raise self._error("Expected expression")
    
    # Helper methods
    def _match(self, *types: TokenType) -> bool:
        """Check if current token matches any of the given types"""
        for token_type in types:
            if self._check(token_type):
                self._advance()
                return True
        return False
    
    def _check(self, token_type: TokenType) -> bool:
        """Check if current token is of given type"""
        if self._is_at_end():
            return False
        return self._peek().type == token_type
    
    def _advance(self) -> Token:
        """Consume and return current token"""
        if not self._is_at_end():
            self.current += 1
        return self._previous()
    
    def _is_at_end(self) -> bool:
        """Check if we're at end of tokens"""
        return self._peek().type == TokenType.EOF
    
    def _peek(self) -> Token:
        """Return current token without consuming"""
        return self.tokens[self.current]
    
    def _previous(self) -> Token:
        """Return previous token"""
        return self.tokens[self.current - 1]
    
    def _consume(self, token_type: TokenType, message: str) -> Token:
        """Consume token of expected type or raise error"""
        if self._check(token_type):
            return self._advance()
        
        current_token = self._peek()
        raise ParseError(f"{message}. Got {current_token.type.name}", current_token)
    
    def _error(self, message: str) -> ParseError:
        """Create parse error"""
        return ParseError(message, self._peek())
    
    def _synchronize(self):
        """Synchronize after parse error"""
        self._advance()
        
        while not self._is_at_end():
            if self._previous().type == TokenType.SEMICOLON:
                return
            
            if self._peek().type in [TokenType.CLASS, TokenType.FUNCTION, TokenType.LET, 
                                   TokenType.CONST, TokenType.FOR, TokenType.IF, 
                                   TokenType.WHILE, TokenType.RETURN]:
                return
            
            self._advance()