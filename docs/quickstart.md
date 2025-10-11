# ⚡ Quick Start Guide# Quick Start Guide



Get started with PowerScript in 5 minutes!Get started with PowerScript in just 5 minutes!



## 🎯 Your First Program## Prerequisites



### Step 1: Install TPS- Python 3.8 or higher

- pip (Python package manager)

```bash

pip install tps## Step 1: Install PowerScript

```

```bash

### Step 2: Create a Filepip install tps

```

Create `hello.ps`:

Verify installation:

```powerscript

function main(): void {```bash

    console.log("Hello, PowerScript!");tps --version

}# Output: PowerScript v1.0.0

``````



### Step 3: Compile and Run## Step 2: Your First Program



```bashCreate a file named `hello.ps`:

# Compile to Python

tps-compile hello.ps```powerscript

// hello.ps

# Run the outputconsole.log("Hello, PowerScript!");

python hello.py

```let name: string = "World";

console.log(f"Welcome to PowerScript, {name}!");

**Output:**```

```

Hello, PowerScript!Run it:

```

```bash

🎉 **Congratulations!** You just ran your first PowerScript program!tps-run hello.ps

```

## 🚀 5-Minute Tutorial

Output:

### Variables and Types```

Hello, PowerScript!

```powerscriptWelcome to PowerScript, World!

function main(): void {```

    // Type declarations ✅

    let name: string = "PowerScript";## Step 3: Functions and Types

    let version: number = 1.0;

    let isAwesome: boolean = true;Create `functions.ps`:

    

    // Type inference ✅```powerscript

    let auto = "Automatically typed!";// Function with type annotations

    function add(a: number, b: number): number {

    console.log(name);    return a + b;

    console.log("Version: " + version);}

}

```// Arrow function

const multiply = (a: number, b: number): number => a * b;

### Functions

// Use functions

```powerscriptlet sum = add(5, 3);

// Function with types ✅let product = multiply(4, 7);

function greet(name: string): string {

    return "Hello, " + name + "!";console.log(f"Sum: {sum}");

}console.log(f"Product: {product}");

```

function add(a: number, b: number): number {

    return a + b;Run:

}```bash

tps-run functions.ps

function main(): void {```

    console.log(greet("World"));

    console.log("2 + 3 = " + add(2, 3));## Step 4: Classes

}

```Create `classes.ps`:



### Arrays```powerscript

class Person {

```powerscript    private name: string;

function main(): void {    public age: number;

    // Typed arrays ✅    

    let numbers: number[] = [1, 2, 3, 4, 5];    constructor(name: string, age: number) {

    let names: string[] = ["Alice", "Bob", "Charlie"];        this.name = name;

            this.age = age;

    // Array operations ✅    }

    console.log(numbers[0]);        // 1    

    console.log(names.length);       // 3    public greet(): void {

            console.log(f"Hi, I'm {this.name}, age {this.age}!");

    // Iteration ✅    }

    for (let i = 0; i < numbers.length; i++) {}

        console.log(numbers[i]);

    }let person = new Person("Alice", 25);

}person.greet();

``````



### Classes## Step 5: Async/Await



```powerscriptCreate `async.ps`:

// Class with constructor ✅

class Person {```powerscript

    constructor(public name: string, public age: number) {}async function fetchData(): Promise<string> {

        // Simulate async operation

    greet(): string {    console.log("Fetching data...");

        return "Hi, I'm " + this.name;    return "Data loaded!";

    }}

}

async function main(): Promise<void> {

function main(): void {    let data = await fetchData();

    let person = new Person("Alice", 30);    console.log(data);

    console.log(person.greet());}

    console.log(person.age);

}main();

``````



### Control Flow## Next Steps



```powerscript- 📖 Read the [Language Reference](language_reference.md)

function main(): void {- 🎨 Install the [VS Code Extension](vscode_extension.md)

    // If-else ✅- 💡 Check out [Best Practices](best_practices.md)

    let score: number = 85;- 🤖 Try AI/ML examples in `test_suits/`

    

    if (score >= 90) {## Common Commands

        console.log("Grade: A");

    } else if (score >= 80) {```bash

        console.log("Grade: B");# Compile to Python

    } else {tps-compile file.ps

        console.log("Grade: C");

    }# Run directly

    tps-run file.ps

    // While loop ✅

    let count: number = 0;# Create new project

    while (count < 3) {tps-create my-project

        console.log("Count: " + count);

        count++;# Watch mode (auto-recompile)

    }tps-compile file.ps --watch

    ```

    // For loop ✅

    for (let i = 0; i < 5; i++) {🚀 **Happy coding with PowerScript!**

        console.log("i = " + i);
    }
}
```

## 💼 Practical Examples

### Example 1: Calculator

```powerscript
class Calculator {
    add(a: number, b: number): number {
        return a + b;
    }
    
    subtract(a: number, b: number): number {
        return a - b;
    }
    
    multiply(a: number, b: number): number {
        return a * b;
    }
    
    divide(a: number, b: number): number {
        if (b == 0) {
            console.log("Error: Division by zero");
            return 0;
        }
        return a / b;
    }
}

function main(): void {
    let calc = new Calculator();
    
    console.log("10 + 5 = " + calc.add(10, 5));
    console.log("10 - 5 = " + calc.subtract(10, 5));
    console.log("10 * 5 = " + calc.multiply(10, 5));
    console.log("10 / 5 = " + calc.divide(10, 5));
}
```

### Example 2: Todo List

```powerscript
class TodoItem {
    constructor(
        public id: number,
        public title: string,
        public completed: boolean
    ) {}
}

class TodoList {
    private items: TodoItem[] = [];
    private nextId: number = 1;
    
    add(title: string): void {
        let item = new TodoItem(this.nextId, title, false);
        this.items.push(item);
        this.nextId++;
        console.log("Added: " + title);
    }
    
    complete(id: number): void {
        for (let i = 0; i < this.items.length; i++) {
            if (this.items[i].id == id) {
                this.items[i].completed = true;
                console.log("Completed: " + this.items[i].title);
                return;
            }
        }
    }
    
    listAll(): void {
        console.log("Todo List:");
        for (let i = 0; i < this.items.length; i++) {
            let status = this.items[i].completed ? "✓" : " ";
            console.log("[" + status + "] " + this.items[i].title);
        }
    }
}

function main(): void {
    let todos = new TodoList();
    
    todos.add("Learn PowerScript");
    todos.add("Build a project");
    todos.add("Share with friends");
    
    todos.complete(1);
    todos.listAll();
}
```

### Example 3: File Operations

```powerscript
import { FileSystem } from "powerscript/runtime";

function main(): void {
    // Write to file ✅
    FileSystem.writeFile("output.txt", "Hello from PowerScript!");
    console.log("File written successfully");
    
    // Read from file ✅
    let content: string = FileSystem.readFile("output.txt");
    console.log("Content: " + content);
    
    // Check if file exists ✅
    if (FileSystem.exists("output.txt")) {
        console.log("File exists!");
    }
}
```

## 🛠️ CLI Commands

### Compile Only

```bash
tps-compile myfile.ps
# Generates: myfile.py
```

### Compile and Run

```bash
tps-run myfile.ps
# Compiles and executes immediately
```

### Type Check

```bash
tps-check myfile.ps
# Validates types without compiling
```

### Create New Project

```bash
tps-create my-project
cd my-project
# Creates project structure with examples
```

## 📂 Project Structure

### Basic Project

```
my-project/
├── src/
│   └── main.ps          # Your code
├── build/
│   └── main.py          # Compiled output
└── powerscript.toml     # Configuration
```

### powerscript.toml

```toml
[project]
name = "my-project"
version = "1.0.0"
entry = "src/main.ps"

[compiler]
output_dir = "build"
strict_types = true
```

## 🎨 VS Code Integration

### Install Extension

1. Open VS Code
2. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)
3. Type: "Extensions: Install from VSIX"
4. Select `powerscript-1.0.0.vsix`

### Features

- ✅ Syntax highlighting
- ✅ Code snippets
- ✅ Error detection
- ✅ Auto-formatting
- ✅ IntelliSense (coming soon 🔄)

### Useful Snippets

Type these and press Tab:

- `func` → Function declaration
- `class` → Class with constructor
- `if` → If-else statement
- `for` → For loop
- `while` → While loop
- `import` → Import statement

## 🔍 Common Patterns

### Error Handling

```powerscript
function divide(a: number, b: number): number {
    if (b == 0) {
        console.log("Error: Cannot divide by zero");
        return 0;
    }
    return a / b;
}
```

### Array Processing

```powerscript
function sumArray(numbers: number[]): number {
    let total: number = 0;
    for (let i = 0; i < numbers.length; i++) {
        total = total + numbers[i];
    }
    return total;
}

function main(): void {
    let nums: number[] = [1, 2, 3, 4, 5];
    console.log("Sum: " + sumArray(nums));  // Sum: 15
}
```

### String Operations

```powerscript
function main(): void {
    let text: string = "PowerScript";
    
    console.log(text.length);           // 11
    console.log(text.toUpperCase());    // POWERSCRIPT
    console.log(text.substring(0, 5));  // Power
}
```

## ⚡ Performance Tips

1. **Use Type Declarations** - Helps compiler optimize
2. **Avoid Global Variables** - Use function scope
3. **Preallocate Arrays** - When size is known
4. **Use Built-in Functions** - They're optimized

## 🚨 Common Mistakes

### ❌ Wrong

```powerscript
// Missing type
function add(a, b) {
    return a + b;
}
```

### ✅ Correct

```powerscript
// With types
function add(a: number, b: number): number {
    return a + b;
}
```

### ❌ Wrong

```powerscript
// Untyped array
let items = [];
```

### ✅ Correct

```powerscript
// Typed array
let items: string[] = [];
```

## 🎓 Next Steps

Now that you know the basics:

1. **[Language Reference](language_reference.md)** - Complete syntax guide
2. **[Type System](type_system.md)** - Master types
3. **[Tutorial](tutorial.md)** - Build real projects
4. **[API Reference](api_reference.md)** - Explore built-in libraries

## 💡 Tips for Success

- ✅ **Always declare types** - Catch errors early
- ✅ **Use meaningful names** - Code is read more than written
- ✅ **Start small** - Master basics before advanced features
- ✅ **Read examples** - Learn from working code
- ✅ **Practice daily** - Consistency builds skill

## 🆘 Getting Help

**Stuck?** Check:
- [FAQ](faq.md) - Common questions
- [Troubleshooting](troubleshooting.md) - Fix issues
- [GitHub Discussions](https://github.com/SaleemLww/Python-PowerScript/discussions) - Ask community

---

**Ready for more? Continue to [Tutorial](tutorial.md) for in-depth learning! 📚**
