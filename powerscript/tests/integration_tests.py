#!/usr/bin/env python3
"""
MIT License

Copyright (c) 2025 Saleem Ahmad (Elite India Org Team)
Email: team@eliteindia.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import unittest
import tempfile
import os
import shutil
import subprocess
import sys
from pathlib import Path

# Add powerscript to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from powerscript.compiler.lexer import PowerScriptLexer
from powerscript.compiler.parser import PowerScriptParser
from powerscript.compiler.transpiler import PowerScriptTranspiler
from powerscript.cli.commands import PowerScriptCommands
from powerscript.typechecker.type_checker import TypeChecker
from powerscript.runtime.runtime_validator import RuntimeValidator


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests with common setup."""
    
    def setUp(self):
        """Set up temporary directory for test files."""
        self.test_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.test_dir)
        
        # Create test project structure
        self.src_dir = os.path.join(self.test_dir, 'src')
        self.build_dir = os.path.join(self.test_dir, 'build')
        os.makedirs(self.src_dir)
        os.makedirs(self.build_dir)
        
        # Initialize components
        self.lexer = PowerScriptLexer()
        self.parser = PowerScriptParser()
        self.transpiler = PowerScriptTranspiler()
        self.type_checker = TypeChecker()
        self.commands = PowerScriptCommands()
    
    def create_test_file(self, filename: str, content: str) -> str:
        """Create a test PowerScript file."""
        filepath = os.path.join(self.src_dir, filename)
        with open(filepath, 'w') as f:
            f.write(content)
        return filepath
    
    def compile_and_run(self, ps_content: str) -> tuple:
        """Compile PowerScript code and return the generated Python code and execution result."""
        # Create test file
        ps_file = self.create_test_file('test.ps', ps_content)
        
        # Compile
        tokens = self.lexer.tokenize(ps_content)
        ast = self.parser.parse(tokens)
        python_code = self.transpiler.transpile(ast)
        
        # Write Python file
        py_file = os.path.join(self.build_dir, 'test.py')
        with open(py_file, 'w') as f:
            f.write(python_code)
        
        # Execute Python code
        try:
            result = subprocess.run(
                [sys.executable, py_file],
                capture_output=True,
                text=True,
                timeout=30,
                cwd=self.build_dir
            )
            return python_code, result
        except subprocess.TimeoutExpired:
            return python_code, None


class BasicLanguageFeaturesTest(IntegrationTestCase):
    """Test basic PowerScript language features end-to-end."""
    
    def test_class_compilation_and_execution(self):
        """Test class definition, instantiation, and method calls."""
        ps_code = """
        class Calculator {
            private value: number;
            
            constructor(initialValue: number) {
                this.value = initialValue;
            }
            
            add(x: number): number {
                this.value = this.value + x;
                return this.value;
            }
            
            get(): number {
                return this.value;
            }
        }
        
        let calc = new Calculator(10);
        calc.add(5);
        console.log(calc.get()); // Should print 15
        """
        
        python_code, result = self.compile_and_run(ps_code)
        
        # Check compilation
        self.assertIn('class Calculator', python_code)
        self.assertIn('def __init__', python_code)
        self.assertIn('def add', python_code)
        
        # Check execution
        self.assertIsNotNone(result)
        self.assertEqual(result.returncode, 0)
        self.assertIn('15', result.stdout)
    
    def test_async_functions(self):
        """Test async function compilation and execution."""
        ps_code = """
        async function fetchData(url: string): Promise<string> {
            // Simulate async operation
            await new Promise(resolve => setTimeout(resolve, 100));
            return "Data from " + url;
        }
        
        async function main(): Promise<void> {
            const data = await fetchData("https://api.example.com");
            console.log(data);
        }
        
        main();
        """
        
        python_code, result = self.compile_and_run(ps_code)
        
        # Check compilation
        self.assertIn('async def fetchData', python_code)
        self.assertIn('await', python_code)
        self.assertIn('asyncio', python_code)
        
        # Check execution
        self.assertIsNotNone(result)
        self.assertEqual(result.returncode, 0)
        self.assertIn('Data from https://api.example.com', result.stdout)
    
    def test_generics_and_types(self):
        """Test generic types and type annotations."""
        ps_code = """
        class Container<T> {
            private items: T[];
            
            constructor() {
                this.items = [];
            }
            
            add(item: T): void {
                this.items.push(item);
            }
            
            get(index: number): T {
                return this.items[index];
            }
            
            size(): number {
                return this.items.length;
            }
        }
        
        let stringContainer = new Container<string>();
        stringContainer.add("hello");
        stringContainer.add("world");
        console.log(stringContainer.get(0));
        console.log(stringContainer.size());
        """
        
        python_code, result = self.compile_and_run(ps_code)
        
        # Check compilation
        self.assertIn('from typing import', python_code)
        self.assertIn('TypeVar', python_code)
        self.assertIn('Generic', python_code)
        
        # Check execution
        self.assertIsNotNone(result)
        self.assertEqual(result.returncode, 0)
        self.assertIn('hello', result.stdout)
        self.assertIn('2', result.stdout)


class AIWorkflowTest(IntegrationTestCase):
    """Test AI-specific PowerScript features and workflows."""
    
    def test_data_processing_pipeline(self):
        """Test data processing with NumPy-like operations."""
        ps_code = """
        import { numpy as np } from "numpy";
        
        class DataProcessor {
            processArray(data: number[]): number[] {
                // Simulate numpy operations
                let result = [];
                for (let i = 0; i < data.length; i++) {
                    result.push(data[i] * 2);
                }
                return result;
            }
            
            calculateMean(data: number[]): number {
                let sum = 0;
                for (let item of data) {
                    sum += item;
                }
                return sum / data.length;
            }
        }
        
        let processor = new DataProcessor();
        let data = [1, 2, 3, 4, 5];
        let processed = processor.processArray(data);
        let mean = processor.calculateMean(processed);
        
        console.log("Processed:", processed);
        console.log("Mean:", mean);
        """
        
        python_code, result = self.compile_and_run(ps_code)
        
        # Check compilation
        self.assertIn('class DataProcessor', python_code)
        self.assertIn('def processArray', python_code)
        self.assertIn('def calculateMean', python_code)
        
        # Check execution
        self.assertIsNotNone(result)
        self.assertEqual(result.returncode, 0)
        self.assertIn('[2, 4, 6, 8, 10]', result.stdout)
        self.assertIn('6.0', result.stdout)
    
    def test_ml_model_structure(self):
        """Test ML model class structure compilation."""
        ps_code = """
        interface MLModel<T> {
            train(data: T): Promise<void>;
            predict(input: T): Promise<any>;
        }
        
        class SimpleModel implements MLModel<number[]> {
            private weights: number[];
            
            constructor() {
                this.weights = [0.1, 0.2, 0.3];
            }
            
            async train(data: number[]): Promise<void> {
                // Simulate training
                console.log("Training with data length:", data.length);
                this.weights = this.weights.map(w => w * 1.1);
            }
            
            async predict(input: number[]): Promise<number> {
                let result = 0;
                for (let i = 0; i < Math.min(input.length, this.weights.length); i++) {
                    result += input[i] * this.weights[i];
                }
                return result;
            }
        }
        
        async function runModel(): Promise<void> {
            let model = new SimpleModel();
            await model.train([1, 2, 3, 4, 5]);
            let prediction = await model.predict([1, 1, 1]);
            console.log("Prediction:", prediction);
        }
        
        runModel();
        """
        
        python_code, result = self.compile_and_run(ps_code)
        
        # Check compilation
        self.assertIn('class SimpleModel', python_code)
        self.assertIn('async def train', python_code)
        self.assertIn('async def predict', python_code)
        
        # Check execution
        self.assertIsNotNone(result)
        self.assertEqual(result.returncode, 0)
        self.assertIn('Training with data length: 5', result.stdout)
        self.assertIn('Prediction:', result.stdout)


class CLIIntegrationTest(IntegrationTestCase):
    """Test CLI commands integration."""
    
    def test_compile_command(self):
        """Test powerscriptc compilation command."""
        # Create test PowerScript file
        ps_content = """
        class HelloWorld {
            sayHello(): void {
                console.log("Hello from PowerScript!");
            }
        }
        
        let greeter = new HelloWorld();
        greeter.sayHello();
        """
        
        ps_file = self.create_test_file('hello.ps', ps_content)
        
        # Test compilation
        result = self.commands.compile([self.src_dir], self.build_dir)
        
        # Check that Python file was generated
        py_file = os.path.join(self.build_dir, 'hello.py')
        self.assertTrue(os.path.exists(py_file))
        
        # Check Python file content
        with open(py_file, 'r') as f:
            python_code = f.read()
            self.assertIn('class HelloWorld', python_code)
            self.assertIn('def sayHello', python_code)
    
    def test_project_creation(self):
        """Test ps-create project scaffolding."""
        project_name = "test_ai_project"
        project_path = os.path.join(self.test_dir, project_name)
        
        # Create project
        self.commands.create_project(project_name, self.test_dir)
        
        # Check project structure
        self.assertTrue(os.path.exists(project_path))
        self.assertTrue(os.path.exists(os.path.join(project_path, 'src')))
        self.assertTrue(os.path.exists(os.path.join(project_path, 'tests')))
        self.assertTrue(os.path.exists(os.path.join(project_path, 'data')))
        self.assertTrue(os.path.exists(os.path.join(project_path, 'models')))
        self.assertTrue(os.path.exists(os.path.join(project_path, 'powerscript.toml')))
        self.assertTrue(os.path.exists(os.path.join(project_path, 'requirements.txt')))
        
        # Check powerscript.toml content
        with open(os.path.join(project_path, 'powerscript.toml'), 'r') as f:
            config = f.read()
            self.assertIn('name = "test_ai_project"', config)
            self.assertIn('[project]', config)
            self.assertIn('[compiler]', config)


class TypeCheckingIntegrationTest(IntegrationTestCase):
    """Test type checking integration."""
    
    def test_type_error_detection(self):
        """Test that type errors are properly detected."""
        ps_code = """
        function add(a: number, b: number): number {
            return a + b;
        }
        
        let result: string = add(1, 2); // Type error: number assigned to string
        """
        
        tokens = self.lexer.tokenize(ps_code)
        ast = self.parser.parse(tokens)
        
        # Run type checker
        errors = self.type_checker.check(ast)
        
        # Should detect type mismatch
        self.assertTrue(len(errors) > 0)
        self.assertTrue(any('type mismatch' in error.lower() or 'cannot assign' in error.lower() 
                           for error in errors))
    
    def test_valid_typing(self):
        """Test that valid code passes type checking."""
        ps_code = """
        function multiply(a: number, b: number): number {
            return a * b;
        }
        
        let x: number = 5;
        let y: number = 10;
        let result: number = multiply(x, y);
        console.log(result);
        """
        
        tokens = self.lexer.tokenize(ps_code)
        ast = self.parser.parse(tokens)
        
        # Run type checker
        errors = self.type_checker.check(ast)
        
        # Should have no errors
        self.assertEqual(len(errors), 0)


class RuntimeValidationTest(IntegrationTestCase):
    """Test runtime validation and access modifiers."""
    
    def test_access_modifier_enforcement(self):
        """Test that private members are properly enforced."""
        ps_code = """
        class TestClass {
            private secretValue: number;
            public publicValue: number;
            
            constructor() {
                this.secretValue = 42;
                this.publicValue = 24;
            }
            
            getSecret(): number {
                return this.secretValue; // Valid access
            }
        }
        
        let obj = new TestClass();
        console.log(obj.publicValue); // Valid
        console.log(obj.getSecret()); // Valid
        // obj.secretValue would cause runtime error
        """
        
        python_code, result = self.compile_and_run(ps_code)
        
        # Check compilation includes access modifier decorators
        self.assertIn('@private', python_code)
        self.assertIn('@public', python_code)
        
        # Check execution
        self.assertIsNotNone(result)
        self.assertEqual(result.returncode, 0)
        self.assertIn('24', result.stdout)
        self.assertIn('42', result.stdout)


class ErrorHandlingTest(IntegrationTestCase):
    """Test error handling and recovery."""
    
    def test_syntax_error_reporting(self):
        """Test that syntax errors are properly reported."""
        ps_code = """
        class MissingBrace {
            method(): void {
                console.log("missing closing brace");
            // Missing closing brace here
        """
        
        try:
            tokens = self.lexer.tokenize(ps_code)
            ast = self.parser.parse(tokens)
            self.fail("Expected syntax error")
        except Exception as e:
            self.assertIn('syntax', str(e).lower())
    
    def test_compilation_error_recovery(self):
        """Test that compilation continues after recoverable errors."""
        ps_code = """
        class ValidClass {
            validMethod(): void {
                console.log("This should compile");
            }
        }
        
        // This has an error but shouldn't stop compilation of ValidClass
        function invalidFunction(: void {
            console.log("Invalid syntax");
        }
        """
        
        # Should handle errors gracefully
        try:
            tokens = self.lexer.tokenize(ps_code)
            # Parser should either succeed partially or fail gracefully
            ast = self.parser.parse(tokens)
        except Exception as e:
            # Error should be informative
            self.assertIsInstance(e, (SyntaxError, ValueError))


class PerformanceTest(IntegrationTestCase):
    """Test performance of compilation and execution."""
    
    def test_large_file_compilation(self):
        """Test compilation performance with larger files."""
        # Generate a large PowerScript file
        ps_code = """
        class LargeClass {
            private data: number[];
            
            constructor() {
                this.data = [];
            }
        """
        
        # Add many methods
        for i in range(100):
            ps_code += f"""
            method{i}(): number {{
                return {i} * 2;
            }}
            """
        
        ps_code += "}"
        
        # Add instantiation and calls
        ps_code += """
        let obj = new LargeClass();
        """
        
        for i in range(10):
            ps_code += f"console.log(obj.method{i}());\n"
        
        # Time compilation
        import time
        start_time = time.time()
        
        tokens = self.lexer.tokenize(ps_code)
        ast = self.parser.parse(tokens)
        python_code = self.transpiler.transpile(ast)
        
        compilation_time = time.time() - start_time
        
        # Should compile in reasonable time (less than 5 seconds)
        self.assertLess(compilation_time, 5.0)
        
        # Check that output is reasonable
        self.assertIn('class LargeClass', python_code)
        self.assertIn('def method0', python_code)
        self.assertIn('def method99', python_code)


def run_integration_tests():
    """Run all integration tests."""
    # Create test suite
    test_classes = [
        BasicLanguageFeaturesTest,
        AIWorkflowTest,
        CLIIntegrationTest,
        TypeCheckingIntegrationTest,
        RuntimeValidationTest,
        ErrorHandlingTest,
        PerformanceTest
    ]
    
    suite = unittest.TestSuite()
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return success status
    return result.wasSuccessful()


if __name__ == '__main__':
    print("Running PowerScript Integration Tests...")
    print("=" * 60)
    
    success = run_integration_tests()
    
    print("=" * 60)
    if success:
        print("✅ All integration tests passed!")
        sys.exit(0)
    else:
        print("❌ Some integration tests failed!")
        sys.exit(1)