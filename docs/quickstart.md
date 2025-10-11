# ⚡ Quick Start Guide# ⚡ Quick Start Guide# Quick Start Guide



Get started with PowerScript in 5 minutes!



---Get started with PowerScript in 5 minutes!Get started with PowerScript in just 5 minutes!



## 🎯 Your First Program



### Step 1: Install TPS## 🎯 Your First Program## Prerequisites



```bash

pip install tps

```### Step 1: Install TPS- Python 3.8 or higher



### Step 2: Create a File- pip (Python package manager)



Create `hello.ps`:```bash



```powerscriptpip install tps## Step 1: Install PowerScript

function main(): void {

    console.log("Hello, PowerScript!");```

}

``````bash



### Step 3: Compile and Run### Step 2: Create a Filepip install tps



```bash```

# Compile to Python

tps-compile hello.psCreate `hello.ps`:



# Run the outputVerify installation:

python hello.py

``````powerscript



**Output:**function main(): void {```bash

```

Hello, PowerScript!    console.log("Hello, PowerScript!");tps --version

```

}# Output: PowerScript v1.0.0

🎉 **Congratulations!** You just ran your first PowerScript program!

``````

---



## 🚀 5-Minute Tutorial

### Step 3: Compile and Run## Step 2: Your First Program

### Variables and Types



```powerscript

function main(): void {```bashCreate a file named `hello.ps`:

    // Type declarations ✅

    let name: string = "PowerScript";# Compile to Python

    let version: number = 1.0;

    let isAwesome: boolean = true;tps-compile hello.ps```powerscript

    

    // Type inference ✅// hello.ps

    let auto = "Automatically typed!";

    # Run the outputconsole.log("Hello, PowerScript!");

    console.log(name);

    console.log("Version: " + version);python hello.py

}

``````let name: string = "World";



### Functionsconsole.log(f"Welcome to PowerScript, {name}!");



```powerscript**Output:**```

// Function with types ✅

function greet(name: string): string {```

    return "Hello, " + name + "!";

}Hello, PowerScript!Run it:



function add(a: number, b: number): number {```

    return a + b;

}```bash



function main(): void {🎉 **Congratulations!** You just ran your first PowerScript program!tps-run hello.ps

    console.log(greet("World"));

    console.log("2 + 3 = " + add(2, 3));```

}

```## 🚀 5-Minute Tutorial



### ArraysOutput:



```powerscript### Variables and Types```

function main(): void {

    // Typed arrays ✅Hello, PowerScript!

    let numbers: number[] = [1, 2, 3, 4, 5];

    let names: string[] = ["Alice", "Bob", "Charlie"];```powerscriptWelcome to PowerScript, World!

    

    // Array operations ✅function main(): void {```

    console.log(numbers[0]);        // 1

    console.log(names.length);       // 3    // Type declarations ✅

    

    // Iteration ✅    let name: string = "PowerScript";## Step 3: Functions and Types

    for (let i = 0; i < numbers.length; i++) {

        console.log(numbers[i]);    let version: number = 1.0;

    }

}    let isAwesome: boolean = true;Create `functions.ps`:

```

    

### Classes

    // Type inference ✅```powerscript

```powerscript

// Class with constructor ✅    let auto = "Automatically typed!";// Function with type annotations

class Person {

    constructor(public name: string, public age: number) {}    function add(a: number, b: number): number {

    

    greet(): string {    console.log(name);    return a + b;

        return "Hi, I'm " + this.name;

    }    console.log("Version: " + version);}

}

}

function main(): void {

    let person = new Person("Alice", 30);```// Arrow function

    console.log(person.greet());

    console.log(person.age);const multiply = (a: number, b: number): number => a * b;

}

```### Functions



### Control Flow// Use functions



```powerscript```powerscriptlet sum = add(5, 3);

function main(): void {

    // If-else ✅// Function with types ✅let product = multiply(4, 7);

    let score: number = 85;

    function greet(name: string): string {

    if (score >= 90) {

        console.log("Grade: A");    return "Hello, " + name + "!";console.log(f"Sum: {sum}");

    } else if (score >= 80) {

        console.log("Grade: B");}console.log(f"Product: {product}");

    } else {

        console.log("Grade: C");```

    }

    function add(a: number, b: number): number {

    // While loop ✅

    let count: number = 0;    return a + b;Run:

    while (count < 3) {

        console.log("Count: " + count);}```bash

        count++;

    }tps-run functions.ps

    

    // For loop ✅function main(): void {```

    for (let i = 0; i < 5; i++) {

        console.log("i = " + i);    console.log(greet("World"));

    }

}    console.log("2 + 3 = " + add(2, 3));## Step 4: Classes

```

}

---

```Create `classes.ps`:

## 💼 Practical Examples



### Example 1: Calculator

### Arrays```powerscript

```powerscript

class Calculator {class Person {

    add(a: number, b: number): number {

        return a + b;```powerscript    private name: string;

    }

    function main(): void {    public age: number;

    subtract(a: number, b: number): number {

        return a - b;    // Typed arrays ✅    

    }

        let numbers: number[] = [1, 2, 3, 4, 5];    constructor(name: string, age: number) {

    multiply(a: number, b: number): number {

        return a * b;    let names: string[] = ["Alice", "Bob", "Charlie"];        this.name = name;

    }

                this.age = age;

    divide(a: number, b: number): number {

        if (b == 0) {    // Array operations ✅    }

            console.log("Error: Division by zero");

            return 0;    console.log(numbers[0]);        // 1    

        }

        return a / b;    console.log(names.length);       // 3    public greet(): void {

    }

}            console.log(f"Hi, I'm {this.name}, age {this.age}!");



function main(): void {    // Iteration ✅    }

    let calc = new Calculator();

        for (let i = 0; i < numbers.length; i++) {}

    console.log("10 + 5 = " + calc.add(10, 5));

    console.log("10 - 5 = " + calc.subtract(10, 5));        console.log(numbers[i]);

    console.log("10 * 5 = " + calc.multiply(10, 5));

    console.log("10 / 5 = " + calc.divide(10, 5));    }let person = new Person("Alice", 25);

}

```}person.greet();



### Example 2: Todo List``````



```powerscript

class TodoItem {

    constructor(### Classes## Step 5: Async/Await

        public id: number,

        public title: string,

        public completed: boolean

    ) {}```powerscriptCreate `async.ps`:

}

// Class with constructor ✅

class TodoList {

    private items: TodoItem[] = [];class Person {```powerscript

    private nextId: number = 1;

        constructor(public name: string, public age: number) {}async function fetchData(): Promise<string> {

    add(title: string): void {

        let item = new TodoItem(this.nextId, title, false);        // Simulate async operation

        this.items.push(item);

        this.nextId++;    greet(): string {    console.log("Fetching data...");

        console.log("Added: " + title);

    }        return "Hi, I'm " + this.name;    return "Data loaded!";

    

    complete(id: number): void {    }}

        for (let i = 0; i < this.items.length; i++) {

            if (this.items[i].id == id) {}

                this.items[i].completed = true;

                console.log("Completed: " + this.items[i].title);async function main(): Promise<void> {

                return;

            }function main(): void {    let data = await fetchData();

        }

    }    let person = new Person("Alice", 30);    console.log(data);

    

    listAll(): void {    console.log(person.greet());}

        console.log("Todo List:");

        for (let i = 0; i < this.items.length; i++) {    console.log(person.age);

            let status = this.items[i].completed ? "✓" : " ";

            console.log("[" + status + "] " + this.items[i].title);}main();

        }

    }``````

}



function main(): void {

    let todos = new TodoList();### Control Flow## Next Steps

    

    todos.add("Learn PowerScript");

    todos.add("Build a project");

    todos.add("Share with friends");```powerscript- 📖 Read the [Language Reference](language_reference.md)

    

    todos.complete(1);function main(): void {- 🎨 Install the [VS Code Extension](vscode_extension.md)

    todos.listAll();

}    // If-else ✅- 💡 Check out [Best Practices](best_practices.md)

```

    let score: number = 85;- 🤖 Try AI/ML examples in `test_suits/`

### Example 3: File Operations

    

```powerscript

import { FileSystem } from "powerscript/runtime";    if (score >= 90) {## Common Commands



function main(): void {        console.log("Grade: A");

    // Write to file ✅

    FileSystem.writeFile("output.txt", "Hello from PowerScript!");    } else if (score >= 80) {```bash

    console.log("File written successfully");

            console.log("Grade: B");# Compile to Python

    // Read from file ✅

    let content: string = FileSystem.readFile("output.txt");    } else {tps-compile file.ps

    console.log("Content: " + content);

            console.log("Grade: C");

    // Check if file exists ✅

    if (FileSystem.exists("output.txt")) {    }# Run directly

        console.log("File exists!");

    }    tps-run file.ps

}

```    // While loop ✅



---    let count: number = 0;# Create new project



## 🛠️ CLI Commands    while (count < 3) {tps-create my-project



### Compile Only        console.log("Count: " + count);



```bash        count++;# Watch mode (auto-recompile)

tps-compile myfile.ps

# Generates: myfile.py    }tps-compile file.ps --watch

```

    ```

### Compile and Run

    // For loop ✅

```bash

tps-run myfile.ps    for (let i = 0; i < 5; i++) {🚀 **Happy coding with PowerScript!**

# Compiles and executes immediately

```        console.log("i = " + i);

    }

### Type Check}

```

```bash

tps-check myfile.ps## 💼 Practical Examples

# Validates types without compiling

```### Example 1: Calculator



### Create New Project```powerscript

class Calculator {

```bash    add(a: number, b: number): number {

tps-create my-project        return a + b;

cd my-project    }

# Creates project structure with examples    

```    subtract(a: number, b: number): number {

        return a - b;

📚 **[Complete CLI Reference →](cli_reference.md)**    }

    

---    multiply(a: number, b: number): number {

        return a * b;

## 📂 Project Structure    }

    

### Basic Project    divide(a: number, b: number): number {

        if (b == 0) {

```            console.log("Error: Division by zero");

my-project/            return 0;

├── src/        }

│   └── main.ps          # Your code        return a / b;

├── build/    }

│   └── main.py          # Compiled output}

└── powerscript.toml     # Configuration

```function main(): void {

    let calc = new Calculator();

### powerscript.toml    

    console.log("10 + 5 = " + calc.add(10, 5));

```toml    console.log("10 - 5 = " + calc.subtract(10, 5));

[project]    console.log("10 * 5 = " + calc.multiply(10, 5));

name = "my-project"    console.log("10 / 5 = " + calc.divide(10, 5));

version = "1.0.0"}

entry = "src/main.ps"```



[compiler]### Example 2: Todo List

output_dir = "build"

strict_types = true```powerscript

```class TodoItem {

    constructor(

---        public id: number,

        public title: string,

## 🎨 VS Code Integration        public completed: boolean

    ) {}

### Install Extension}



1. Open VS Codeclass TodoList {

2. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)    private items: TodoItem[] = [];

3. Type: "Extensions: Install from VSIX"    private nextId: number = 1;

4. Select `powerscript-1.0.0.vsix`    

    add(title: string): void {

### Features        let item = new TodoItem(this.nextId, title, false);

        this.items.push(item);

- ✅ Syntax highlighting        this.nextId++;

- ✅ Code snippets (13 snippets)        console.log("Added: " + title);

- ✅ Error detection    }

- ✅ Auto-formatting    

- 🔄 IntelliSense (coming soon)    complete(id: number): void {

        for (let i = 0; i < this.items.length; i++) {

### Useful Snippets            if (this.items[i].id == id) {

                this.items[i].completed = true;

Type these and press Tab:                console.log("Completed: " + this.items[i].title);

                return;

- `func` → Function declaration            }

- `class` → Class with constructor        }

- `if` → If-else statement    }

- `for` → For loop    

- `while` → While loop    listAll(): void {

- `import` → Import statement        console.log("Todo List:");

        for (let i = 0; i < this.items.length; i++) {

📚 **[Complete VS Code Guide →](vscode_extension.md)**            let status = this.items[i].completed ? "✓" : " ";

            console.log("[" + status + "] " + this.items[i].title);

---        }

    }

## 🔍 Common Patterns}



### Error Handlingfunction main(): void {

    let todos = new TodoList();

```powerscript    

function divide(a: number, b: number): number {    todos.add("Learn PowerScript");

    if (b == 0) {    todos.add("Build a project");

        console.log("Error: Cannot divide by zero");    todos.add("Share with friends");

        return 0;    

    }    todos.complete(1);

    return a / b;    todos.listAll();

}}

``````



### Array Processing### Example 3: File Operations



```powerscript```powerscript

function sumArray(numbers: number[]): number {import { FileSystem } from "powerscript/runtime";

    let total: number = 0;

    for (let i = 0; i < numbers.length; i++) {function main(): void {

        total = total + numbers[i];    // Write to file ✅

    }    FileSystem.writeFile("output.txt", "Hello from PowerScript!");

    return total;    console.log("File written successfully");

}    

    // Read from file ✅

function main(): void {    let content: string = FileSystem.readFile("output.txt");

    let nums: number[] = [1, 2, 3, 4, 5];    console.log("Content: " + content);

    console.log("Sum: " + sumArray(nums));  // Sum: 15    

}    // Check if file exists ✅

```    if (FileSystem.exists("output.txt")) {

        console.log("File exists!");

### String Operations    }

}

```powerscript```

function main(): void {

    let text: string = "PowerScript";## 🛠️ CLI Commands

    

    console.log(text.length);           // 11### Compile Only

    console.log(text.toUpperCase());    // POWERSCRIPT

    console.log(text.substring(0, 5));  // Power```bash

}tps-compile myfile.ps

```# Generates: myfile.py

```

---

### Compile and Run

## ⚡ Performance Tips

```bash

1. **Use Type Declarations** - Helps compiler optimizetps-run myfile.ps

2. **Avoid Global Variables** - Use function scope# Compiles and executes immediately

3. **Preallocate Arrays** - When size is known```

4. **Use Built-in Functions** - They're optimized

### Type Check

---

```bash

## 🚨 Common Mistakestps-check myfile.ps

# Validates types without compiling

### ❌ Wrong```



```powerscript### Create New Project

// Missing type

function add(a, b) {```bash

    return a + b;tps-create my-project

}cd my-project

```# Creates project structure with examples

```

### ✅ Correct

## 📂 Project Structure

```powerscript

// With types### Basic Project

function add(a: number, b: number): number {

    return a + b;```

}my-project/

```├── src/

│   └── main.ps          # Your code

### ❌ Wrong├── build/

│   └── main.py          # Compiled output

```powerscript└── powerscript.toml     # Configuration

// Untyped array```

let items = [];

```### powerscript.toml



### ✅ Correct```toml

[project]

```powerscriptname = "my-project"

// Typed arrayversion = "1.0.0"

let items: string[] = [];entry = "src/main.ps"

```

[compiler]

---output_dir = "build"

strict_types = true

## 🎓 Next Steps```



Now that you know the basics:## 🎨 VS Code Integration



1. **[CLI Reference](cli_reference.md)** - Master the command-line tools### Install Extension

2. **[VS Code Extension](vscode_extension.md)** - Setup your development environment

3. **[FAQ](faq.md)** - Common questions answered1. Open VS Code

2. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)

---3. Type: "Extensions: Install from VSIX"

4. Select `powerscript-1.0.0.vsix`

## 💡 Tips for Success

### Features

- ✅ **Always declare types** - Catch errors early

- ✅ **Use meaningful names** - Code is read more than written- ✅ Syntax highlighting

- ✅ **Start small** - Master basics before advanced features- ✅ Code snippets

- ✅ **Read examples** - Learn from working code- ✅ Error detection

- ✅ **Practice daily** - Consistency builds skill- ✅ Auto-formatting

- ✅ IntelliSense (coming soon 🔄)

---

### Useful Snippets

## 🆘 Getting Help

Type these and press Tab:

**Stuck?** Check:

- `func` → Function declaration

- **[FAQ](faq.md)** - Common questions- `class` → Class with constructor

- **[GitHub Issues](https://github.com/SaleemLww/Python-PowerScript/issues)** - Report bugs- `if` → If-else statement

- **[GitHub Discussions](https://github.com/SaleemLww/Python-PowerScript/discussions)** - Ask community- `for` → For loop

- `while` → While loop

---- `import` → Import statement



**Ready for more? Explore [CLI Reference](cli_reference.md) and [VS Code Extension](vscode_extension.md)! 🚀**## 🔍 Common Patterns


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
