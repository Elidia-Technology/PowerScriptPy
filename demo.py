#!/usr/bin/env python3
"""
PowerScript Demo Script

Demonstrates the PowerScript compiler, transpiler, and runtime system
"""

import sys
import os
from pathlib import Path

# Add the powerscript package to the path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from powerscript.compiler import Lexer, Parser, Transpiler
    from powerscript.compiler.transpiler import transpile_file
    from powerscript.typechecker import TypeChecker
    IMPORTS_AVAILABLE = True
except ImportError as e:
    print(f"Import error: {e}")
    print("Some features may not be available.")
    IMPORTS_AVAILABLE = False


def demo_lexer():
    """Demonstrate the lexer"""
    print("🔍 LEXER DEMO")
    print("=" * 50)
    
    if not IMPORTS_AVAILABLE:
        print("❌ Lexer not available due to import errors")
        return
    
    source = '''
    class Person {
        let name: string = "Alice";
        function greet(): void {
            print("Hello!");
        }
    }
    '''
    
    print("PowerScript Source:")
    print(source)
    
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    print("\nTokens:")
    for token in tokens[:15]:  # Show first 15 tokens
        print(f"  {token.type.name:<15} {token.value!r}")
    
    if len(tokens) > 15:
        print(f"  ... and {len(tokens) - 15} more tokens")
    
    print(f"\nTotal tokens: {len(tokens)}")
    print()


def demo_parser():
    """Demonstrate the parser"""
    print("🌳 PARSER DEMO")
    print("=" * 50)
    
    if not IMPORTS_AVAILABLE:
        print("❌ Parser not available due to import errors")
        return
    
    source = '''
    class Calculator {
        constructor(name: string) {
            this.name = name;
        }
        
        function add(a: number, b: number): number {
            return a + b;
        }
    }
    '''
    
    print("PowerScript Source:")
    print(source)
    
    lexer = Lexer(source)
    lexer.tokenize()
    
    parser = Parser(lexer)
    ast_nodes = parser.parse()
    
    print("\nAST Structure:")
    for node in ast_nodes:
        if hasattr(node, 'name'):
            print(f"  📦 {node.__class__.__name__}: {node.name}")
            
            if hasattr(node, 'constructor') and node.constructor:
                print(f"    🏗️  Constructor with {len(node.constructor.parameters)} parameters")
                for param in node.constructor.parameters:
                    print(f"      📥 {param.name}: {param.param_type}")
            
            if hasattr(node, 'methods'):
                for method in node.methods:
                    print(f"    🔧 Method: {method.name}")
                    print(f"      📥 Parameters: {len(method.parameters)}")
                    print(f"      📤 Returns: {method.return_type}")
    
    print(f"\nTotal AST nodes: {len(ast_nodes)}")
    print()


def demo_transpiler():
    """Demonstrate the transpiler"""
    print("🔄 TRANSPILER DEMO")
    print("=" * 50)
    
    if not IMPORTS_AVAILABLE:
        print("❌ Transpiler not available due to import errors")
        return
    
    source = '''
    class Greeter {
        private message: string;
        
        constructor(message: string) {
            this.message = message;
        }
        
        public function greet(name: string): string {
            return this.message + ", " + name + "!";
        }
    }
    
    let greeter: Greeter = new Greeter("Hello");
    let result: string = greeter.greet("World");
    '''
    
    print("PowerScript Source:")
    print(source)
    
    try:
        python_code = transpile_file(source)
        
        print("\nTranspiled Python Code:")
        print("-" * 30)
        print(python_code)
        print("-" * 30)
        
        # Try to execute the generated Python code
        print("\nExecuting generated Python code:")
        try:
            # Create a safe namespace for execution
            namespace = {'print': print}
            exec(python_code, namespace)
            print("✅ Code executed successfully!")
        except Exception as e:
            print(f"❌ Execution error: {e}")
    
    except Exception as e:
        print(f"❌ Transpilation error: {e}")
    
    print()


def demo_type_checker():
    """Demonstrate the type checker"""
    print("🔍 TYPE CHECKER DEMO")
    print("=" * 50)
    
    if not IMPORTS_AVAILABLE:
        print("❌ Type checker not available due to import errors")
        return    # Valid code
    valid_source = '''
    function add(a: number, b: number): number {
        return a + b;
    }
    
    let result: number = add(10, 20);
    '''
    
    print("Valid PowerScript Code:")
    print(valid_source)
    
    lexer = Lexer(valid_source)
    lexer.tokenize()
    
    parser = Parser(lexer)
    ast_nodes = parser.parse()
    
    type_checker = TypeChecker()
    result = type_checker.check(ast_nodes)
    
    print(f"\nType Check Result: {'✅ PASS' if result.success else '❌ FAIL'}")
    print(f"Errors: {len(result.errors)}")
    print(f"Warnings: {len(result.warnings)}")
    
    # Invalid code
    print("\n" + "-" * 50)
    
    invalid_source = '''
    function add(a: number, b: number): number {
        return a + b;
    }
    
    let result: string = add(10, 20);  // Type error!
    '''
    
    print("Invalid PowerScript Code (type error):")
    print(invalid_source)
    
    lexer = Lexer(invalid_source)
    lexer.tokenize()
    
    parser = Parser(lexer)
    ast_nodes = parser.parse()
    
    type_checker = TypeChecker()
    result = type_checker.check(ast_nodes)
    
    print(f"\nType Check Result: {'✅ PASS' if result.success else '❌ FAIL'}")
    print(f"Errors: {len(result.errors)}")
    print(f"Warnings: {len(result.warnings)}")
    
    if result.errors:
        print("\nErrors found:")
        for error in result.errors:
            print(f"  ❌ Line {error.line}: {error.message}")
    
    print()


def demo_runtime():
    """Demonstrate runtime features"""
    print("⚡ RUNTIME DEMO")
    print("=" * 50)
    
    if not IMPORTS_AVAILABLE:
        print("❌ Runtime features not available due to import errors")
        return
    
    print("1. Runtime Type Validation:")
    
    try:
        from powerscript.runtime.runtime_validator import validate_type
        
        # Valid validations
        validate_type(42, int, "number_var")
        print("  ✅ validate_type(42, int) - PASS")
        
        validate_type("hello", str, "string_var") 
        print("  ✅ validate_type('hello', str) - PASS")
        
        validate_type([1, 2, 3], list, "list_var")
        print("  ✅ validate_type([1, 2, 3], list) - PASS")
        
        # Invalid validation
        try:
            validate_type("not a number", int, "invalid_var")
        except Exception as e:
            print(f"  ❌ validate_type('not a number', int) - FAIL: {e}")
    
    except ImportError as e:
        print(f"  ⚠️  Runtime validation not available: {e}")
    
    print("\n2. Access Modifier Demo:")
    
    try:
        from powerscript.runtime.access_modifiers import private, protected, public
        
        class DemoClass:
            @public
            def public_method(self):
                return "This is public"
            
            @protected
            def protected_method(self):
                return "This is protected"
            
            @private
            def private_method(self):
                return "This is private"
        
        obj = DemoClass()
        print(f"  ✅ Public method: {obj.public_method()}")
        print(f"  ✅ Protected method: {obj.protected_method()}")
        print(f"  ✅ Private method: {obj.private_method()}")
        
    except ImportError as e:
        print(f"  ⚠️  Access modifiers not available: {e}")
    
    print()


def demo_examples():
    """Show available examples"""
    print("📚 EXAMPLES DEMO")
    print("=" * 50)
    
    examples_dir = Path(__file__).parent / "powerscript" / "examples"
    
    if examples_dir.exists():
        example_files = list(examples_dir.glob("*.ps"))
        
        print(f"Available PowerScript examples ({len(example_files)} files):")
        for example_file in example_files:
            print(f"  📄 {example_file.name}")
        
        # Show a snippet from the basic example
        basic_example = examples_dir / "basic.ps"
        if basic_example.exists():
            print(f"\nSnippet from {basic_example.name}:")
            print("-" * 30)
            with open(basic_example, 'r') as f:
                lines = f.readlines()[:15]  # First 15 lines
                print(''.join(lines))
            if len(lines) == 15:
                print("... (truncated)")
            print("-" * 30)
    else:
        print("Examples directory not found")
    
    print()


def main():
    """Run all demonstrations"""
    print("🚀 POWERSCRIPT DEMONSTRATION")
    print("=" * 60)
    print("PowerScript - A fully structured development language")
    print("Version: 0.1.0")
    print("=" * 60)
    print()
    
    try:
        demo_lexer()
        demo_parser()
        demo_transpiler() 
        demo_type_checker()
        demo_runtime()
        demo_examples()
        
        print("🎉 DEMONSTRATION COMPLETE!")
        print("=" * 60)
        print()
        print("Next steps:")
        print("1. pip install -e . (to install PowerScript)")
        print("2. ps-create my_project (to create a new project)")
        print("3. powerscript run examples/basic.ps (to run examples)")
        print("4. powerscript compile src/ -o build/ (to compile projects)")
        print()
        
    except Exception as e:
        print(f"❌ Demonstration failed: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())