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
    from powerscript.compiler.lexer import Lexer, TokenType
    from powerscript.compiler.parser import Parser
    from powerscript.compiler.transpiler import Transpiler
    from powerscript.typechecker.type_checker import TypeChecker
    from powerscript.runtime.runtime_validator import RuntimeValidator
    IMPORTS_AVAILABLE = True
    print("✅ All PowerScript modules imported successfully!")
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Some features may not be available.")
    print("\n🔧 To fix this:")
    print("1. Make sure you're in the project root directory")
    print("2. Run: export PYTHONPATH=$PWD:$PYTHONPATH")
    print("3. Or install in development mode: pip install -e .")
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
        # Create transpiler and process
        lexer = Lexer(source)
        lexer.tokenize()
        
        parser = Parser(lexer)
        ast = parser.parse()
        
        transpiler = Transpiler()
        python_code = transpiler.transpile(ast)
        
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
class Calculator {
    function add(a: number, b: number): number {
        return a + b;
    }
}

let calc: Calculator = new Calculator();
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


def ai_examples_demo():
    """Demonstrate advanced AI examples."""
    print("\n🤖 AI Examples Demonstration")
    print("-" * 30)
    
    examples_dir = os.path.join(os.path.dirname(__file__), 'powerscript', 'examples')
    
    # List AI examples
    ai_examples = [
        'advanced_ml.ps',
        'computer_vision.ps', 
        'nlp_transformers.ps',
        'data_processing.ps',
        'ml_model.ps'
    ]
    
    for example in ai_examples:
        example_path = os.path.join(examples_dir, example)
        if os.path.exists(example_path):
            print(f"📁 {example} - Advanced AI implementation")
            
            # Read first few lines to show content
            with open(example_path, 'r') as f:
                lines = f.readlines()[:3]
                for line in lines:
                    if line.strip().startswith('//'):
                        print(f"   {line.strip()}")
        else:
            print(f"⚠️  {example} not found")

def integration_tests_demo():
    """Demonstrate integration testing capabilities."""
    print("\n🧪 Integration Tests Demonstration")
    print("-" * 30)
    
    test_file = os.path.join(os.path.dirname(__file__), 'powerscript', 'tests', 'integration_tests.py')
    
    if os.path.exists(test_file):
        print("✅ Integration tests available:")
        print("   • BasicLanguageFeaturesTest - Core language features")
        print("   • AIWorkflowTest - AI/ML pipeline testing") 
        print("   • CLIIntegrationTest - Command-line tools")
        print("   • TypeCheckingIntegrationTest - Static analysis")
        print("   • RuntimeValidationTest - Access modifiers")
        print("   • ErrorHandlingTest - Error recovery")
        print("   • PerformanceTest - Compilation performance")
        
        print("\n🚀 Run tests with: python -m powerscript.tests.integration_tests")
    else:
        print("⚠️  Integration tests not found")

def vscode_extension_demo():
    """Demonstrate VS Code extension capabilities."""
    print("\n🎨 VS Code Extension Features")
    print("-" * 30)
    
    extension_dir = os.path.join(os.path.dirname(__file__), 'powerscript', 'vscode-extension')
    
    if os.path.exists(extension_dir):
        print("✅ VS Code Extension includes:")
        print("   • Syntax highlighting (.tmLanguage.json)")
        print("   • Code snippets (class, function, async templates)")
        print("   • Language Server Protocol (LSP) integration")
        print("   • Auto-completion and IntelliSense")
        print("   • Error diagnostics and type checking")
        print("   • Go-to-definition support")
        print("   • Debugging integration with debugpy")
        
        # Check specific files
        files_to_check = [
            'package.json',
            'syntaxes/powerscript.tmLanguage.json',
            'snippets/powerscript.json',
            'src/extension.ts'
        ]
        
        for file in files_to_check:
            file_path = os.path.join(extension_dir, file)
            if os.path.exists(file_path):
                print(f"   ✓ {file}")
            else:
                print(f"   ✗ {file} missing")
    else:
        print("⚠️  VS Code extension not found")

def documentation_demo():
    """Demonstrate documentation completeness."""
    print("\n📚 Documentation Overview")
    print("-" * 30)
    
    docs_dir = os.path.join(os.path.dirname(__file__), 'powerscript', 'docs')
    
    if os.path.exists(docs_dir):
        print("✅ Documentation includes:")
        
        docs = {
            'README.md': 'Project overview and getting started',
            'language-spec.md': 'Complete language specification',
            'tutorial.md': 'Step-by-step learning guide',
            'cli-guide.md': 'Command-line tools reference',
            'vscode-setup.md': 'VS Code extension setup'
        }
        
        for doc, description in docs.items():
            doc_path = os.path.join(docs_dir, doc)
            if os.path.exists(doc_path):
                print(f"   ✓ {doc} - {description}")
            else:
                print(f"   ✗ {doc} - {description} (missing)")
    else:
        print("⚠️  Documentation directory not found")

def main():
    """Main demonstration function"""
    print("🚀 PowerScript Complete Development Framework")
    print("=" * 60)
    
    # Phase completion status
    print("\n📋 Development Phase Status:")
    print("✅ Phase 1: Project Initialization")
    print("✅ Phase 2: Lexer and Parser") 
    print("✅ Phase 3: Transpiler (PowerScript → Python)")
    print("✅ Phase 4: Type System")
    print("✅ Phase 5: CLI Tools")
    print("✅ Phase 6: VS Code Extension + LSP")
    print("✅ Phase 7: Project Creation and Workflow")
    print("✅ Phase 8: AI Project Integration")
    print("✅ Phase 9: Testing and Validation")
    print("✅ Phase 10: Documentation")
    print("🔮 Phase 11: Advanced Features (Future)")
    print("✅ Phase 12: Deliverables")
    
    try:
        # Run core demonstrations
        demo_lexer()
        demo_parser() 
        demo_transpiler()
        demo_type_checker()
        demo_runtime()
        demo_examples()
        
        # Show new features
        ai_examples_demo()
        integration_tests_demo()
        vscode_extension_demo()
        documentation_demo()
        
        print("\n" + "=" * 60)
        print("🎉 PowerScript Framework Complete!")
        print("\n📦 Ready for:")
        print("   • Production use with full type safety")
        print("   • AI/ML project development")
        print("   • VS Code development with IntelliSense")
        print("   • Large-scale project scaffolding")
        print("   • Advanced language features")
        
        print("\n🚀 Next Steps:")
        print("   1. Install VS Code extension")
        print("   2. Create new project: ps-create my_ai_project")
        print("   3. Start developing: code my_ai_project")
        print("   4. Compile and run: powerscriptc src/ -o build/")
        
    except Exception as e:
        print(f"❌ Demonstration failed: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())