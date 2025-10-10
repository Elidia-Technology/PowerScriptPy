# PowerScript Language Specification

## Table of Contents
1. [Introduction](#introduction)
2. [Syntax Overview](#syntax-overview)
3. [Types](#types)
4. [Classes](#classes)
5. [Functions](#functions)
6. [Variables](#variables)
7. [Control Flow](#control-flow)
8. [Async/Await](#asyncawait)
9. [Generics](#generics)
10. [Modules](#modules)
11. [File Handling](#file-handling)
12. [Built-in Functions](#built-in-functions)
13. [Compilation](#compilation)

## Introduction

PowerScript is a statically-typed language that transpiles to Python, designed specifically for AI and machine learning development. It combines the familiar syntax of TypeScript/JavaScript with the power of Python's ecosystem.

## Syntax Overview

PowerScript uses curly-brace syntax similar to TypeScript:

```powerscript
// Single line comment
/* Multi-line
   comment */

class MyClass {
    private value: number;
    
    constructor(value: number) {
        this.value = value;
    }
    
    public getValue(): number {
        return this.value;
    }
}
```

## Types

### Basic Types
- `string` - Text data
- `number` - Numeric data (int/float)
- `boolean` - True/false values
- `any` - Dynamic type (Python object)
- `void` - No return value
- `Array<T>` - Array of type T
- `Promise<T>` - Async return type

### Type Annotations
```powerscript
let name: string = "PowerScript";
let count: number = 42;
let active: boolean = true;
let items: Array<string> = ["a", "b", "c"];
```

### Optional Types
```powerscript
let optional: string? = null;
let result = optional ?? "default";  // Null coalescing
```

## Classes

### Basic Class Definition
```powerscript
class Person {
    private name: string;
    protected age: number;
    public email: string;
    
    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
        this.email = "";
    }
    
    public getName(): string {
        return this.name;
    }
    
    protected getAge(): number {
        return this.age;
    }
}
```

### Inheritance
```powerscript
class Employee extends Person {
    private salary: number;
    
    constructor(name: string, age: number, salary: number) {
        super(name, age);
        this.salary = salary;
    }
    
    public getSalary(): number {
        return this.salary;
    }
}
```

## Functions

### Function Declaration
```powerscript
function add(a: number, b: number): number {
    return a + b;
}

function greet(name: string): void {
    console.log(`Hello, ${name}!`);
}
```

### Arrow Functions
```powerscript
let multiply = (a: number, b: number): number => {
    return a * b;
};

let square = (x: number): number => x * x;
```

### Async Functions
```powerscript
async function fetchData(url: string): Promise<any> {
    let response = await fetch(url);
    return await response.json();
}
```

## Variables

### Variable Declarations
```powerscript
let mutable: string = "can change";
const immutable: number = 42;
var legacy: boolean = true;  // Function-scoped
```

### Destructuring
```powerscript
let [first, second] = ["a", "b"];
let {name, age} = {name: "John", age: 30};
```

## Control Flow

### Conditionals
```powerscript
if (condition) {
    // code
} else if (otherCondition) {
    // code
} else {
    // code
}

// Ternary operator
let result = condition ? "yes" : "no";
```

### Loops
```powerscript
// For loop
for (let i = 0; i < 10; i++) {
    console.log(i);
}

// For-in loop
for (let item in items) {
    console.log(item);
}

// While loop
while (condition) {
    // code
}
```

### Switch Statement
```powerscript
switch (value) {
    case "a":
        console.log("A");
        break;
    case "b":
        console.log("B");
        break;
    default:
        console.log("Other");
}
```

## Async/Await

PowerScript fully supports async/await patterns:

```powerscript
async function processData(): Promise<Array<number>> {
    let data = await loadData();
    let processed = await transformData(data);
    return processed;
}

// Parallel execution
async function parallelProcessing(): Promise<void> {
    let [result1, result2] = await Promise.all([
        fetchData("url1"),
        fetchData("url2")
    ]);
}
```

## Generics

### Generic Functions
```powerscript
function identity<T>(arg: T): T {
    return arg;
}

let result = identity<string>("hello");
```

### Generic Classes
```powerscript
class Container<T> {
    private value: T;
    
    constructor(value: T) {
        this.value = value;
    }
    
    public getValue(): T {
        return this.value;
    }
}

let stringContainer = new Container<string>("test");
let numberContainer = new Container<number>(42);
```

## Modules

### Import/Export
```powerscript
// Export
export class MyClass { }
export function myFunction() { }
export const myConstant = 42;

// Import
import { MyClass, myFunction } from "./myModule";
import * as Utils from "./utils";
import MyDefault from "./default";
```

### Python Library Integration
```powerscript
import numpy as np;
import pandas as pd;
import torch from "torch";

// Use Python libraries directly
let array = np.array([1, 2, 3]);
let df = pd.DataFrame({"a": [1, 2], "b": [3, 4]});
```

## Compilation

### PowerScript to Python Mapping

| PowerScript | Python |
|-------------|--------|
| `class MyClass { }` | `class MyClass:` |
| `constructor(x: number)` | `def __init__(self, x: int):` |
| `private value: string` | `self._value: str` |
| `public getValue(): string` | `def get_value(self) -> str:` |
| `let x: number = 5` | `x: int = 5` |
| `const PI = 3.14` | `PI: Final[float] = 3.14` |
| `async function f()` | `async def f():` |
| `Array<string>` | `List[str]` |
| `Promise<number>` | `Awaitable[int]` |

### Compilation Process

1. **Lexical Analysis**: Source code → tokens
2. **Parsing**: Tokens → Abstract Syntax Tree (AST)  
3. **Type Checking**: Validate types and semantics
4. **Code Generation**: AST → Python AST → Python code
5. **Runtime Integration**: Add PowerScript runtime helpers

### CLI Usage
```bash
# Compile PowerScript to Python
powerscriptc src/ -o build/

# Run PowerScript directly
ps-run src/main.ps

# Type check only
psc src/

# Watch mode
powerscriptc -w src/ -o build/
```

## Error Handling

PowerScript provides comprehensive error reporting:

### Compile-time Errors
- Syntax errors with line/column information
- Type mismatches with suggestions
- Undefined variable/function usage
- Access modifier violations

### Runtime Integration
- Source maps for debugging compiled Python
- PowerScript stack traces
- Runtime type validation (optional)

## File Handling

PowerScript provides comprehensive file I/O operations through built-in functions and classes.

### Basic File Operations

```powerscript
// Write text to file
file_write("data.txt", "Hello, World!")

// Read text from file
let content = file_read("data.txt")

// Check if file exists
if file_exists("data.txt") {
    console.log("File exists!")
}

// Append to file
file_append("data.txt", "\nNew line")

// Delete file
file_delete("data.txt")
```

### File Class

```powerscript
let file = File("document.txt")
file.write("Content")
let content = file.read()
let lines = file.read_lines()
console.log("Size:", file.size())
```

### Directory Operations

```powerscript
// Create directory
dir_create("new_folder")

// List directory contents
let files = dir_list(".")

// Directory class
let dir = Directory("folder")
dir.create_subdir("subfolder")
let contents = dir.list_files()
```

### JSON and CSV Support

```powerscript
// JSON operations
let data = { "name": "PowerScript", "version": "1.0" }
json_write("config.json", data)
let config = json_read("config.json")

// CSV operations
let csv_data = [["Name", "Age"], ["Alice", "25"]]
csv_write("data.csv", csv_data)
let loaded = csv_read("data.csv")
```

### File Streaming

```powerscript
// For large files
let stream = file_stream("large.txt", "w")
stream.write("data")
stream.close()
```

## Built-in Functions

PowerScript provides a rich set of built-in functions and classes:

### Console Operations
- `console.log()` - Print to console
- `console.error()` - Print error
- `console.warn()` - Print warning

### Math Functions
- `Math.abs()`, `Math.max()`, `Math.min()`
- `Math.sqrt()`, `Math.pow()`, `Math.floor()`, `Math.ceil()`
- `Math.sin()`, `Math.cos()`, `Math.tan()`
- `Math.random()` - Random number generation

### String Utilities
- `str()` - Convert to string
- `len()` - Get length
- `range()` - Generate number sequence

### Type Conversion
- `int()`, `float()`, `bool()`
- `list()`, `dict()`, `set()`

### Date and Time
- `DateTime.now()` - Current date/time
- `DateTime.format()` - Format date

## Best Practices

1. **Use Type Annotations**: Always specify types for better tooling
2. **Access Modifiers**: Use private/protected/public appropriately
3. **Async Operations**: Prefer async/await over callbacks
4. **Error Handling**: Use try/catch for error management
5. **Generics**: Use generics for reusable code
6. **Module Organization**: Keep modules focused and cohesive
7. **File Operations**: Always handle file I/O errors with try/catch
8. **Resource Management**: Close file streams and clean up resources

## IDE Integration

PowerScript provides full IDE support through:
- Syntax highlighting
- Auto-completion
- Type checking
- Go-to-definition
- Hover documentation
- Error diagnostics
- Debugging support