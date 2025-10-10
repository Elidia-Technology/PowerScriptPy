# PowerScript Documentation

## Overview

PowerScript is a fully-featured programming language that transpiles to Python, designed specifically for AI and machine learning development. It combines the expressiveness of TypeScript with the power of Python's ecosystem.

## Table of Contents

- [Language Specification](#language-specification)
- [Type System](#type-system)
- [Classes and Objects](#classes-and-objects)
- [Functions and Methods](#functions-and-methods)
- [Async Programming](#async-programming)
- [Modules and Imports](#modules-and-imports)
- [CLI Reference](#cli-reference)
- [VS Code Extension](#vs-code-extension)
- [API Reference](#api-reference)

## Language Specification

### Basic Syntax

PowerScript uses curly-brace syntax similar to JavaScript/TypeScript:

```powerscript
// Variables
let name: string = "PowerScript";
const version: number = 1.0;

// Functions
function greet(name: string): string {
    return `Hello, ${name}!`;
}

// Classes
class Person {
    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
    
    greet(): string {
        return `Hi, I'm ${this.name}`;
    }
}
```

### Keywords

PowerScript supports the following keywords:

**Declarations:**
- `class` - Class declaration
- `function` - Function declaration
- `constructor` - Constructor method
- `let` - Variable declaration
- `const` - Constant declaration
- `var` - Variable declaration (legacy)

**Control Flow:**
- `if`, `else` - Conditional statements
- `while` - While loop
- `for`, `in` - For loops
- `break`, `continue` - Loop control
- `return` - Function return
- `try`, `catch`, `finally` - Exception handling
- `throw` - Exception throwing

**Modifiers:**
- `public` - Public access
- `private` - Private access
- `protected` - Protected access
- `static` - Static member
- `async` - Async function
- `await` - Await expression

**Other:**
- `this` - Current instance
- `super` - Parent class
- `new` - Object creation
- `import`, `export`, `from` - Module system
- `true`, `false`, `null` - Literals
- `typeof`, `instanceof` - Type checking

## Type System

### Primitive Types

```powerscript
let str: string = "Hello";
let num: number = 42;
let bool: boolean = true;
let nothing: null = null;
let anything: any = "flexible";
let empty: void = undefined;
```

### Array Types

```powerscript
let numbers: Array<number> = [1, 2, 3];
let strings: string[] = ["a", "b", "c"];
let mixed: any[] = [1, "hello", true];
```

### Optional Types

```powerscript
let optional: string? = null;
let result: string = optional ?? "default";

// Optional chaining
let length: number? = optional?.length;
```

### Generic Types

```powerscript
function identity<T>(value: T): T {
    return value;
}

class Container<T> {
    private value: T;
    
    constructor(value: T) {
        this.value = value;
    }
    
    getValue(): T {
        return this.value;
    }
}
```

### Union Types

```powerscript
function process(value: string | number): string {
    if (typeof value === "string") {
        return value.toUpperCase();
    }
    return value.toString();
}
```

## Classes and Objects

### Class Declaration

```powerscript
class Animal {
    protected name: string;
    private age: number;
    
    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
    
    public speak(): string {
        return `${this.name} makes a sound`;
    }
    
    protected getAge(): number {
        return this.age;
    }
}
```

### Inheritance

```powerscript
class Dog extends Animal {
    private breed: string;
    
    constructor(name: string, age: number, breed: string) {
        super(name, age);
        this.breed = breed;
    }
    
    public speak(): string {
        return `${this.name} barks!`;
    }
    
    public getBreed(): string {
        return this.breed;
    }
}
```

### Access Modifiers

- `public` - Accessible from anywhere (default)
- `private` - Accessible only within the same class
- `protected` - Accessible within the class and subclasses

## Functions and Methods

### Function Declaration

```powerscript
// Basic function
function add(a: number, b: number): number {
    return a + b;
}

// Optional parameters
function greet(name: string, title?: string): string {
    return title ? `Hello, ${title} ${name}` : `Hello, ${name}`;
}

// Default parameters
function multiply(a: number, b: number = 1): number {
    return a * b;
}

// Rest parameters
function sum(...numbers: number[]): number {
    return numbers.reduce((a, b) => a + b, 0);
}
```

### Arrow Functions

```powerscript
let square = (x: number): number => x * x;
let log = (message: string): void => console.log(message);
```

### Generic Functions

```powerscript
function map<T, U>(array: T[], fn: (item: T) => U): U[] {
    let result: U[] = [];
    for (let item of array) {
        result.push(fn(item));
    }
    return result;
}
```

## Async Programming

PowerScript has first-class support for asynchronous programming:

```powerscript
// Async function
async function fetchData(url: string): Promise<string> {
    // Simulate async operation
    await sleep(1000);
    return "data from " + url;
}

// Using async/await
async function processData(): Promise<void> {
    try {
        let data = await fetchData("https://api.example.com");
        console.log(data);
    } catch (error) {
        console.error("Failed to fetch data:", error);
    }
}

// Promise creation
function delay(ms: number): Promise<void> {
    return new Promise<void>((resolve) => {
        setTimeout(resolve, ms);
    });
}
```

## Modules and Imports

### Exports

```powerscript
// Named exports
export function calculate(x: number): number {
    return x * 2;
}

export class Calculator {
    add(a: number, b: number): number {
        return a + b;
    }
}

// Default export
export default class MathUtils {
    static PI: number = 3.14159;
}
```

### Imports

```powerscript
// Named imports
import { calculate, Calculator } from "./math";

// Default import
import MathUtils from "./math";

// Namespace import
import * as Math from "./math";

// Mixed imports
import MathUtils, { calculate } from "./math";
```

## CLI Reference

### Commands

#### `powerscriptc` - Compile PowerScript to Python

```bash
# Compile single file
powerscriptc src/main.ps

# Compile directory
powerscriptc src/ -o build/

# Watch mode
powerscriptc src/ -w -o build/

# Strict mode
powerscriptc src/ --strict
```

Options:
- `-o, --output` - Output directory
- `-w, --watch` - Watch for changes
- `--strict` - Enable strict mode
- `--no-runtime-checks` - Disable runtime validation

#### `ps-run` - Run PowerScript directly

```bash
# Run PowerScript file
ps-run src/main.ps

# Run with arguments
ps-run src/app.ps --arg1 value1 --arg2 value2
```

#### `ps-create` - Create new project

```bash
# Create new project
ps-create my-project

# Create with template
ps-create my-ai-project --template ai

# Available templates
ps-create --list-templates
```

#### `psc` - Type checker

```bash
# Check types in file
psc src/main.ps

# Check entire project
psc src/

# Configuration
psc src/ --config powerscript.toml
```

### Configuration

PowerScript projects are configured using `powerscript.toml`:

```toml
[project]
name = "my-project"
version = "1.0.0"
main = "src/main.ps"

[compiler]
output_dir = "build"
strict_typing = true
runtime_checks = true
target_python_version = "3.8"

[runtime]
async_enabled = true
access_modifiers = true
type_validation = "strict"  # "strict", "warn", "off"

[lsp]
enabled = true
port = 8080
```

## VS Code Extension

### Features

- **Syntax Highlighting** - Full PowerScript syntax support
- **IntelliSense** - Auto-completion, hover docs, signature help
- **Error Diagnostics** - Real-time type checking and error reporting
- **Go to Definition** - Navigate to symbol definitions
- **Debugging** - Integrated debugging with source maps
- **Snippets** - Code templates for common patterns

### Installation

1. Install from VS Code Marketplace (coming soon)
2. Or install from VSIX file:
   ```bash
   code --install-extension powerscript-0.1.0.vsix
   ```

### Commands

- `PowerScript: Transpile to Python` (`Ctrl+Shift+T`)
- `PowerScript: Run PowerScript File` (`Ctrl+Shift+R`) 
- `PowerScript: Check Types`
- `PowerScript: Create New Project`

### Settings

```json
{
  "powerscript.pythonPath": "python",
  "powerscript.outputDirectory": "build",
  "powerscript.strictTyping": true,
  "powerscript.runtimeChecks": true,
  "powerscript.lsp.enabled": true,
  "powerscript.lsp.port": 8080
}
```

## API Reference

### Compiler API

```python
from powerscript.compiler import Lexer, Parser, Transpiler

# Lexical analysis
lexer = Lexer(source_code)
tokens = lexer.tokenize()

# Parsing
parser = Parser(lexer)
ast_nodes = parser.parse()

# Transpilation
transpiler = Transpiler()
python_code = transpiler.transpile(ast_nodes)
```

### Type Checker API

```python
from powerscript.typechecker import TypeChecker

type_checker = TypeChecker()
result = type_checker.check(ast_nodes)

if result.success:
    print("Type checking passed!")
else:
    for error in result.errors:
        print(f"Error: {error.message} at line {error.line}")
```

### Runtime API

```python
from powerscript.runtime import RuntimeValidator, AccessModifiers

# Runtime type validation
@RuntimeValidator.validate_types
def my_function(x: int, y: str) -> str:
    return f"{x}: {y}"

# Access modifier enforcement
class MyClass:
    @AccessModifiers.private
    def _private_method(self):
        pass
```

## Examples

### Basic Application

```powerscript
// main.ps
class Application {
    private name: string;
    
    constructor(name: string) {
        this.name = name;
    }
    
    public run(): void {
        console.log(`Starting ${this.name}...`);
        this.processData();
    }
    
    private async processData(): Promise<void> {
        let data = await this.fetchData();
        console.log("Processing:", data);
    }
    
    private async fetchData(): Promise<string[]> {
        // Simulate async data fetching
        return ["item1", "item2", "item3"];
    }
}

// Create and run application
let app = new Application("PowerScript Demo");
app.run();
```

### AI/ML Example

```powerscript
// ml_model.ps
import { numpy as np } from "numpy";
import { sklearn } from "scikit-learn";

class MLModel<T> {
    private model: any;
    private trained: boolean = false;
    
    constructor(private modelType: string) {
        this.model = this.createModel(modelType);
    }
    
    private createModel(type: string): any {
        switch (type) {
            case "linear":
                return sklearn.linear_model.LinearRegression();
            case "tree":
                return sklearn.tree.DecisionTreeClassifier();
            default:
                throw new Error(`Unknown model type: ${type}`);
        }
    }
    
    public async train(X: number[][], y: number[]): Promise<void> {
        console.log("Training model...");
        this.model.fit(X, y);
        this.trained = true;
        console.log("Training completed!");
    }
    
    public predict(X: number[][]): number[] {
        if (!this.trained) {
            throw new Error("Model must be trained before prediction");
        }
        return this.model.predict(X);
    }
}

// Usage
async function main(): Promise<void> {
    let model = new MLModel<number>("linear");
    
    // Sample data
    let X = [[1, 2], [2, 3], [3, 4], [4, 5]];
    let y = [1, 2, 3, 4];
    
    await model.train(X, y);
    let predictions = model.predict([[5, 6], [6, 7]]);
    
    console.log("Predictions:", predictions);
}

main();
```

This documentation provides a comprehensive guide to PowerScript development, from basic syntax to advanced features and tooling.