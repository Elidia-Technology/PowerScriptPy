# Quick Start Guide

Get started with PowerScript in just 5 minutes!

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Step 1: Install PowerScript

```bash
pip install tps
```

Verify installation:

```bash
tps --version
# Output: PowerScript v1.0.0
```

## Step 2: Your First Program

Create a file named `hello.ps`:

```powerscript
// hello.ps
console.log("Hello, PowerScript!");

let name: string = "World";
console.log(f"Welcome to PowerScript, {name}!");
```

Run it:

```bash
tps-run hello.ps
```

Output:
```
Hello, PowerScript!
Welcome to PowerScript, World!
```

## Step 3: Functions and Types

Create `functions.ps`:

```powerscript
// Function with type annotations
function add(a: number, b: number): number {
    return a + b;
}

// Arrow function
const multiply = (a: number, b: number): number => a * b;

// Use functions
let sum = add(5, 3);
let product = multiply(4, 7);

console.log(f"Sum: {sum}");
console.log(f"Product: {product}");
```

Run:
```bash
tps-run functions.ps
```

## Step 4: Classes

Create `classes.ps`:

```powerscript
class Person {
    private name: string;
    public age: number;
    
    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
    
    public greet(): void {
        console.log(f"Hi, I'm {this.name}, age {this.age}!");
    }
}

let person = new Person("Alice", 25);
person.greet();
```

## Step 5: Async/Await

Create `async.ps`:

```powerscript
async function fetchData(): Promise<string> {
    // Simulate async operation
    console.log("Fetching data...");
    return "Data loaded!";
}

async function main(): Promise<void> {
    let data = await fetchData();
    console.log(data);
}

main();
```

## Next Steps

- 📖 Read the [Language Reference](language_reference.md)
- 🎨 Install the [VS Code Extension](vscode_extension.md)
- 💡 Check out [Best Practices](best_practices.md)
- 🤖 Try AI/ML examples in `test_suits/`

## Common Commands

```bash
# Compile to Python
tps-compile file.ps

# Run directly
tps-run file.ps

# Create new project
tps-create my-project

# Watch mode (auto-recompile)
tps-compile file.ps --watch
```

🚀 **Happy coding with PowerScript!**
