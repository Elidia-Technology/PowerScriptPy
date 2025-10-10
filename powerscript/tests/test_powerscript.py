"""
PowerScript Tests

Unit tests for the PowerScript compiler, transpiler, and runtime
"""

import pytest
import tempfile
import os
from pathlib import Path
from powerscript.compiler import Lexer, Parser, Transpiler
from powerscript.compiler.lexer import TokenType
from powerscript.typechecker import TypeChecker
from powerscript.runtime import AccessModifiers, RuntimeValidator


class TestLexer:
    """Test the PowerScript lexer"""
    
    def test_basic_tokens(self):
        """Test basic token recognition"""
        source = """
        class MyClass {
            let x: number = 42;
        }
        """
        
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        token_types = [t.type for t in tokens if t.type != TokenType.EOF]
        expected_types = [
            TokenType.CLASS, TokenType.IDENTIFIER, TokenType.LEFT_BRACE,
            TokenType.LET, TokenType.IDENTIFIER, TokenType.COLON, TokenType.IDENTIFIER,
            TokenType.ASSIGN, TokenType.NUMBER, TokenType.SEMICOLON,
            TokenType.RIGHT_BRACE
        ]
        
        assert len(token_types) >= len(expected_types)
        for expected, actual in zip(expected_types, token_types):
            assert actual == expected
    
    def test_string_literals(self):
        """Test string literal tokenization"""
        lexer = Lexer('"Hello, World!"')
        tokens = lexer.tokenize()
        
        string_token = tokens[0]
        assert string_token.type == TokenType.STRING
        assert string_token.value == '"Hello, World!"'
    
    def test_numbers(self):
        """Test number tokenization"""
        lexer = Lexer('42 3.14 .5 2.')
        tokens = lexer.tokenize()
        
        number_tokens = [t for t in tokens if t.type == TokenType.NUMBER]
        assert len(number_tokens) == 4
        assert number_tokens[0].value == '42'
        assert number_tokens[1].value == '3.14'
        assert number_tokens[2].value == '.5'
        assert number_tokens[3].value == '2.'
    
    def test_keywords(self):
        """Test keyword recognition"""
        lexer = Lexer('class function async await let const if else')
        tokens = lexer.tokenize()
        
        keyword_types = [t.type for t in tokens if t.type != TokenType.EOF]
        expected = [
            TokenType.CLASS, TokenType.FUNCTION, TokenType.ASYNC, TokenType.AWAIT,
            TokenType.LET, TokenType.CONST, TokenType.IF, TokenType.ELSE
        ]
        
        assert keyword_types == expected


class TestParser:
    """Test the PowerScript parser"""
    
    def test_simple_class(self):
        """Test parsing a simple class"""
        source = """
        class Person {
            constructor(name: string) {
                this.name = name;
            }
        }
        """
        
        lexer = Lexer(source)
        lexer.tokenize()
        
        parser = Parser(lexer)
        ast_nodes = parser.parse()
        
        assert len(ast_nodes) == 1
        class_node = ast_nodes[0]
        assert class_node.name == "Person"
        assert class_node.constructor is not None
        assert len(class_node.constructor.parameters) == 1
        assert class_node.constructor.parameters[0].name == "name"
    
    def test_function_declaration(self):
        """Test parsing function declarations"""
        source = """
        function add(a: number, b: number): number {
            return a + b;
        }
        """
        
        lexer = Lexer(source)
        lexer.tokenize()
        
        parser = Parser(lexer)
        ast_nodes = parser.parse()
        
        assert len(ast_nodes) == 1
        func_node = ast_nodes[0]
        assert func_node.name == "add"
        assert len(func_node.parameters) == 2
        assert func_node.return_type == "number"
    
    def test_variable_declaration(self):
        """Test parsing variable declarations"""
        source = """
        let x: number = 42;
        const message: string = "Hello";
        """
        
        lexer = Lexer(source)
        lexer.tokenize()
        
        parser = Parser(lexer)
        ast_nodes = parser.parse()
        
        assert len(ast_nodes) == 2
        assert ast_nodes[0].name == "x"
        assert ast_nodes[0].var_type == "number"
        assert ast_nodes[1].name == "message"
        assert ast_nodes[1].is_const == True


class TestTranspiler:
    """Test the PowerScript to Python transpiler"""
    
    def test_simple_class_transpilation(self):
        """Test transpiling a simple class"""
        source = """
        class Person {
            constructor(name: string) {
                this.name = name;
            }
            
            function greet(): string {
                return "Hello, " + this.name;
            }
        }
        """
        
        from powerscript.compiler.transpiler import transpile_file
        python_code = transpile_file(source)
        
        assert "class Person" in python_code
        assert "def __init__(self, name)" in python_code
        assert "def greet(self)" in python_code
    
    def test_function_transpilation(self):
        """Test transpiling functions"""
        source = """
        function add(a: number, b: number): number {
            return a + b;
        }
        """
        
        from powerscript.compiler.transpiler import transpile_file
        python_code = transpile_file(source)
        
        assert "def add(a, b)" in python_code
        assert "return a + b" in python_code
    
    def test_async_function_transpilation(self):
        """Test transpiling async functions"""
        source = """
        async function fetchData(): string {
            return "data";
        }
        """
        
        from powerscript.compiler.transpiler import transpile_file
        python_code = transpile_file(source)
        
        assert "async def fetchData()" in python_code


class TestTypeChecker:
    """Test the PowerScript type checker"""
    
    def test_basic_type_checking(self):
        """Test basic type checking"""
        source = """
        let x: number = 42;
        let y: string = "hello";
        """
        
        lexer = Lexer(source)
        lexer.tokenize()
        
        parser = Parser(lexer)
        ast_nodes = parser.parse()
        
        type_checker = TypeChecker()
        result = type_checker.check(ast_nodes)
        
        assert result.success
        assert len(result.errors) == 0
    
    def test_type_error_detection(self):
        """Test type error detection"""
        source = """
        let x: number = "not a number";
        """
        
        lexer = Lexer(source)
        lexer.tokenize()
        
        parser = Parser(lexer)
        ast_nodes = parser.parse()
        
        type_checker = TypeChecker()
        result = type_checker.check(ast_nodes)
        
        assert not result.success
        assert len(result.errors) > 0
    
    def test_function_type_checking(self):
        """Test function type checking"""
        source = """
        function add(a: number, b: number): number {
            return a + b;
        }
        
        let result: number = add(1, 2);
        let error: string = add(1, 2);
        """
        
        lexer = Lexer(source)
        lexer.tokenize()
        
        parser = Parser(lexer)
        ast_nodes = parser.parse()
        
        type_checker = TypeChecker()
        result = type_checker.check(ast_nodes)
        
        # Should have error for assigning number to string
        assert len(result.errors) > 0


class TestRuntime:
    """Test PowerScript runtime features"""
    
    def test_access_modifiers(self):
        """Test access modifier enforcement"""
        from powerscript.runtime.access_modifiers import private, AccessViolationError
        
        class TestClass:
            @private
            def private_method(self):
                return "private"
        
        obj = TestClass()
        
        # This should work (same instance)
        result = obj.private_method()
        assert result == "private"
        
        # This should fail (external access) - but we can't easily test this
        # without more complex setup
    
    def test_runtime_validator(self):
        """Test runtime type validation"""
        from powerscript.runtime.runtime_validator import validate_type, TypeValidationError
        
        # Valid types
        assert validate_type(42, int, "test_var")
        assert validate_type("hello", str, "test_var")
        assert validate_type([1, 2, 3], list, "test_var")
        
        # Invalid types
        with pytest.raises(TypeValidationError):
            validate_type("not a number", int, "test_var")
        
        with pytest.raises(TypeValidationError):
            validate_type(42, str, "test_var")


class TestIntegration:
    """Integration tests for the full PowerScript pipeline"""
    
    def test_full_pipeline(self):
        """Test the complete compilation pipeline"""
        source = """
        class Calculator {
            function add(a: number, b: number): number {
                return a + b;
            }
        }
        
        let calc: Calculator = new Calculator();
        let result: number = calc.add(10, 20);
        """
        
        # Lexical analysis
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        assert len(tokens) > 0
        
        # Parsing
        parser = Parser(lexer)
        ast_nodes = parser.parse()
        assert len(ast_nodes) > 0
        
        # Type checking
        type_checker = TypeChecker()
        check_result = type_checker.check(ast_nodes)
        assert check_result.success
        
        # Transpilation
        transpiler = Transpiler()
        python_code = transpiler.transpile_to_code(ast_nodes)
        assert "class Calculator" in python_code
        assert "def add" in python_code
    
    def test_file_compilation(self):
        """Test compiling PowerScript files"""
        source = """
        function greet(name: string): string {
            return "Hello, " + name + "!";
        }
        
        let message: string = greet("PowerScript");
        """
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.ps', delete=False) as f:
            f.write(source)
            temp_file = f.name
        
        try:
            from powerscript.compiler.transpiler import transpile_file
            
            with open(temp_file, 'r') as f:
                file_source = f.read()
            
            python_code = transpile_file(file_source, temp_file)
            
            assert "def greet(name)" in python_code
            assert "message = greet('PowerScript')" in python_code or "message = greet(\"PowerScript\")" in python_code
            
        finally:
            os.unlink(temp_file)


if __name__ == "__main__":
    pytest.main([__file__])