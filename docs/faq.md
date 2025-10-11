# ❓ Frequently Asked Questions (FAQ)# ❓ Frequently Asked Questions (FAQ)# ❓ Frequently Asked Questions (FAQ)



Common questions about PowerScript answered.



## 🎯 General QuestionsCommon questions about PowerScript (TPS).Common questions about PowerScript answered.



### What is PowerScript?



PowerScript (TPS) is a modern typed programming language that transpiles to clean Python code. It combines modern syntax (like JavaScript) with Python's powerful ecosystem.------



### Why use PowerScript instead of Python?



PowerScript offers:## 📖 General Questions## 🎯 General Questions

- ✅ **Type Safety** - Catch errors before runtime

- ✅ **Modern Syntax** - Clean, familiar syntax

- ✅ **Python Power** - Full access to Python libraries

- ✅ **Better Tooling** - VS Code integration with syntax highlighting### What is PowerScript?### What is PowerScript?



### Why use PowerScript instead of TypeScript?



PowerScript:PowerScript (TPS — **T**yped **P**ower**S**cript) is a modern programming language that transpiles to clean Python code. It combines JavaScript-familiar syntax with Python's powerful ecosystem, adding static type checking and modern language features.PowerScript (TPS - Typed PowerScript) is a modern programming language that transpiles to Python. It provides JavaScript-like syntax with static typing while giving you full access to Python's ecosystem.

- ✅ **Python Ecosystem** - Use NumPy, TensorFlow, Django, etc.

- ✅ **No Node.js** - Runs on Python runtime

- ✅ **Data Science** - Perfect for AI/ML/Data Science

- ✅ **Simpler Deployment** - Transpiles to standard Python### Why use PowerScript instead of Python?### Why use PowerScript instead of Python?



### Is PowerScript production-ready?



**Yes!** PowerScript v1.0 Beta is production-ready with:- **Modern Syntax** - Cleaner, more familiar syntax for developers coming from JavaScript/TypeScript**PowerScript offers:**

- ✅ Complete core language features

- ✅ Comprehensive type system- **Type Safety** - Static type checking catches errors before runtime- ✅ Modern, familiar syntax (inspired by JavaScript/TypeScript)

- ✅ Full runtime libraries

- ✅ CLI tools and VS Code extension- **Better Tooling** - VS Code extension with syntax highlighting and snippets- ✅ Static type checking with runtime validation

- ✅ 100% passing core tests

- **Python Ecosystem** - Full access to all Python libraries (NumPy, TensorFlow, Django, etc.)- ✅ Better tooling (VS Code extension with IntelliSense coming soon)

## 🔧 Installation & Setup

- **Easy Learning** - If you know JavaScript or Python, you'll learn PowerScript quickly- ✅ Cleaner, more expressive code

### How do I install PowerScript?

- ✅ Full Python ecosystem access (NumPy, TensorFlow, Django, etc.)

Simple one-line install:

### Why use PowerScript instead of JavaScript?

```bash

pip install tps**Use PowerScript when:**

```

- **Python Ecosystem** - Access to Python's vast library ecosystem (AI/ML, data science, etc.)- You prefer JavaScript-style syntax

See [Installation Guide](installation.md) for detailed instructions.

- **Type Safety** - Built-in type checking from the start- You want static type safety

### What are the system requirements?

- **Simpler Async** - Cleaner async/await without Promise complexity- You're building large, maintainable projects

**Minimum:**

- Python 3.8+- **Server-Side** - Perfect for backend development with Python's strengths- You want modern language features with Python's power

- pip package manager

- 512 MB RAM

- 50 MB disk space

### Is PowerScript production-ready?### Is PowerScript production-ready?

**Recommended:**

- Python 3.9+

- VS Code with PowerScript extension

- 2 GB RAMYes! **PowerScript v1.0.0 Beta** is production-ready with:**Yes!** PowerScript v1.0.0 Beta is production-ready with:



### Can I use PowerScript with virtual environments?- ✅ Complete core language features- ✅ Stable compiler



**Yes!** Recommended approach:- ✅ Full type system- ✅ Complete type system



```bash- ✅ Runtime libraries- ✅ Runtime libraries

python -m venv myenv

source myenv/bin/activate  # On Windows: myenv\Scripts\activate- ✅ CLI tools- ✅ CLI tools

pip install tps

```- ✅ VS Code extension- ✅ VS Code extension



### How do I install the VS Code extension?- ✅ Extensive testing (15/15 core tests passing)- ✅ Comprehensive testing



```bash

cd vscode-extension

code --install-extension powerscript-1.0.0.vsixBeta status means we're still gathering feedback and may make minor API improvements.### What's the relationship between PowerScript and Python?

```



See [VS Code Extension Guide](vscode_extension.md) for details.

### What license is PowerScript under?PowerScript transpiles to clean Python code. This means:

## 💻 Usage Questions

- PowerScript code → Compiles to → Python code → Runs on Python interpreter

### How do I compile PowerScript files?

PowerScript is released under the **MIT License**, which is very permissive. You can use it freely in personal and commercial projects.- Full access to Python libraries

```bash

tps-compile myfile.ps- Same performance as Python

# Creates: myfile.py

```---- Can import Python modules directly



### How do I run PowerScript programs?- No runtime overhead



Two ways:## 🚀 Getting Started



**Option 1: Compile then run**---

```bash

tps-compile hello.ps### How do I install PowerScript?

python hello.py

```## 📦 Installation & Setup



**Option 2: Compile and run (one command)**Simple! Just install via pip:

```bash

tps-run hello.ps### How do I install PowerScript?

```

```bash

### Can I use Python libraries in PowerScript?

pip install tps```bash

**Yes!** Full Python ecosystem access:

```# Simple installation via pip

```powerscript

import { numpy as np, pandas as pd } from "python";pip install tps



function analyze(data: any): void {For detailed instructions, see the [Installation Guide](installation.md).

    let df = pd.DataFrame(data);

    console.log(df.describe());# Verify

}

```### What are the system requirements?tps --version



### How do I create a new project?```



```bash**Minimum:**

tps-create my-project

cd my-project- Python 3.8+**See:** [Installation Guide](installation.md)

```

- pip package manager

This creates a complete project structure.

- 512 MB RAM### What are the system requirements?

### Do I need to compile every time?

- 50 MB disk space

Yes, PowerScript transpiles to Python. But it's fast:

**Minimum:**

```bash

# Quick workflow**Recommended:**- Python 3.8+

tps-run app.ps  # Compiles and runs in one command

```- Python 3.9+- 512 MB RAM



## 🎨 Language Features- VS Code with PowerScript extension- 50 MB disk space



### What types does PowerScript support?- 2 GB RAM



**Basic Types:**- 200 MB disk space**Recommended:**

- `string` - Text values

- `number` - Numbers (int/float)- Python 3.9+

- `boolean` - true/false

- `void` - No return value### How do I compile a PowerScript file?- 2 GB RAM

- `any` - Any type

- `null`, `undefined`- 200 MB disk space



**Complex Types:**```bash- VS Code with PowerScript extension

- Arrays: `string[]`, `number[]`

- Functions: `(a: number) => string`# Compile

- Union types: `string | number`

tps-compile myfile.ps### Do I need to install Python separately?

### Does PowerScript support classes?



**Yes!** Full OOP support:

# This generates myfile.py**Yes.** PowerScript requires Python 3.8+ to be installed since it transpiles to Python code.

```powerscript

class Person {```

    constructor(public name: string, public age: number) {}

    ### Can I use PowerScript with my existing Python projects?

    greet(): string {

        return "Hello, I'm " + this.name;### How do I run a PowerScript program?

    }

}**Yes!** PowerScript can:

```

Two ways:- Import existing Python modules

### Does PowerScript support async/await?

- Call Python functions

**Yes!** Full async support:

**Method 1: Compile then run**- Use Python classes

```powerscript

async function fetchData(): Promise<any> {```bash- Mix with Python code in the same project

    let response = await fetch("https://api.example.com");

    return response.json();tps-compile hello.ps

}

```python hello.py---



### Does PowerScript have interfaces?```



**Yes!** Basic interface support:## 💻 Language Features



```powerscript**Method 2: Direct execution**

interface User {

    name: string;```bash### What types does PowerScript support?

    age: number;

    email: string;tps-run hello.ps

}

```**Basic Types:**

class Admin implements User {

    constructor(- `string`, `number`, `boolean`

        public name: string,

        public age: number,### Do I need to learn Python first?- `void`, `any`, `null`, `undefined`

        public email: string

    ) {}

}

```No! If you know JavaScript or any C-style language, you can start with PowerScript immediately. However, understanding Python basics helps when using Python libraries.**Complex Types:**



### Can I use enums?- Arrays: `string[]`, `number[]`



**Yes!** Enum support included:---- Union types: `string | number`



```powerscript- Function types

enum Color {

    Red,## 💻 Language Features- Class types

    Green,

    Blue- Interface types

}

### What types does PowerScript support?

let favorite: Color = Color.Blue;

```**See:** [Quick Start - Types](quickstart.md)



## 🐛 Troubleshooting**Basic Types:**



### "tps: command not found"- `string` - Text values### Does PowerScript support async/await?



**Solution:**- `number` - Numeric values (int and float)



```bash- `boolean` - true/false**Yes!** PowerScript fully supports:

# Ensure TPS is installed

pip list | grep tps- `void` - No return value- ✅ `async` functions



# Add to PATH (macOS/Linux)- `any` - Any type (use sparingly)- ✅ `await` keyword

export PATH="$HOME/.local/bin:$PATH"

- `null` / `undefined` - Null values- ✅ Promises

# Or use full path

python -m powerscript.cli.cli --version- ✅ Asynchronous operations

```

**Complex Types:**

### "ModuleNotFoundError: No module named 'powerscript'"

- Arrays: `string[]`, `number[]`, etc.Example:

**Solution:**

- Function types: `(a: number, b: number) => number````powerscript

```bash

# Reinstall TPS- Union types: `string | number`async function fetchData(): Promise<string> {

pip install --force-reinstall tps

- Custom classes and interfaces    let response = await fetch("https://api.example.com");

# Activate virtual environment if used

source .venv/bin/activate    return response.text();

```

### Does PowerScript support classes?}

### VS Code extension not highlighting

```

**Solution:**

Yes! Full OOP support:

1. Reload VS Code: `Cmd/Ctrl+Shift+P` → "Reload Window"

2. Check language mode (bottom right) → Select "PowerScript"### Can I use Python libraries in PowerScript?

3. Reinstall extension from VSIX

```powerscript

### Compilation errors

class Person {**Absolutely!** Import any Python library:

**Common issues:**

    constructor(public name: string, public age: number) {}

1. **Missing type annotations**

   ```powerscript    ```powerscript

   // ❌ Wrong

   function add(a, b) { return a + b; }    greet(): string {import { numpy as np, pandas as pd } from "python";

   

   // ✅ Correct        return "Hello, I'm " + this.name;

   function add(a: number, b: number): number { return a + b; }

   ```    }function main(): void {



2. **Type mismatches**}    let arr = np.array([1, 2, 3, 4, 5]);

   ```powerscript

   // ❌ Wrong```    console.log(arr.mean());

   let age: number = "30";

   }

   // ✅ Correct

   let age: number = 30;Features:```

   ```

- ✅ Constructor methods

### Runtime errors

- ✅ Public/private properties### Does PowerScript have classes and OOP?

Check:

1. Python version (must be 3.8+)- ✅ Class methods

2. Required libraries installed

3. Compiled output is recent- ✅ Inheritance (extends)**Yes!** Full OOP support:



## 🚀 Performance & Production- ✅ Static members- ✅ Classes



### How fast is PowerScript?- ✅ Abstract classes- ✅ Constructors



PowerScript transpiles to standard Python, so:- ✅ Inheritance (`extends`)

- **Compilation:** Very fast (< 1 second for most files)

- **Runtime:** Same speed as Python### Does PowerScript support async/await?- ✅ Access modifiers (`public`, `private`, `protected`)

- **No overhead:** Direct Python execution

- ✅ Static members

### Can I deploy PowerScript apps?

Yes! Full async support:- ✅ Abstract classes

**Yes!** Deploy the generated Python files:

- ✅ Interfaces (basic)

```bash

# Compile for production```powerscript

tps-compile src/*.ps --output-dir dist/

async function fetchData(): Promise<any> {### What about generics?

# Deploy dist/ folder with Python files

```    let response = await fetch("https://api.example.com");



### Do I need TPS installed in production?    return await response.json();**Coming in v1.1!** Basic generics work, but advanced generics are planned for Q1 2026.



**No!** Only for development/compilation. Production only needs:}

- Python 3.8+

- Required Python libraries```---

- Your compiled `.py` files



### Can I use PowerScript with Docker?

### Can I use Python libraries in PowerScript?## 🛠️ Development

**Yes!**



```dockerfile

FROM python:3.9Absolutely! That's one of PowerScript's main strengths:### Which IDE should I use?



# Install TPS (for compilation)

RUN pip install tps

```powerscript**Recommended: VS Code** with the PowerScript extension.

# Copy source

COPY src/ /app/src/import { numpy as np, pandas as pd } from "python";



# Compile**Features:**

RUN tps-compile /app/src/*.ps --output-dir /app/dist/

function analyze(): void {- Syntax highlighting

# Run compiled Python

CMD ["python", "/app/dist/main.py"]    let data = np.array([1, 2, 3, 4, 5]);- Code snippets

```

    let df = pd.DataFrame(data);- Error detection

## 🤝 Contributing

    console.log(df.describe());- IntelliSense (coming soon)

### How can I contribute?

}

See [Contributing Guide](../README.md#-contributing) for:

- Bug reports```**See:** [VS Code Extension Guide](vscode_extension.md)

- Feature requests

- Pull requests

- Documentation improvements

### What's the difference between `let` and `const`?### How do I compile PowerScript code?

### Where can I report bugs?



[GitHub Issues](https://github.com/SaleemLww/Python-PowerScript/issues)

- `let` - Variable that can be reassigned```bash

### Can I request features?

- `const` - Variable that cannot be reassigned (but objects/arrays can be mutated)# Compile to Python

**Yes!** Open an issue or discussion on GitHub.

tps-compile myfile.ps

## 📚 Learning Resources

```powerscript

### Where should I start?

let x: number = 5;# Output: myfile.py

1. **[Installation Guide](installation.md)** - Install TPS

2. **[Quick Start](quickstart.md)** - Learn basics in 5 minutesx = 10; // OK```

3. **[CLI Reference](cli_reference.md)** - Master command-line tools



### Are there examples?

const y: number = 5;**See:** [CLI Reference](cli_reference.md)

**Yes!** Check:

- `test_suits/` folder - 58 test filesy = 10; // Error: Cannot reassign const

- [Quick Start Guide](quickstart.md) - Practical examples

- [README.md](../README.md) - Use case examples```### Can I run PowerScript directly?



### Is there a tutorial?



The **[Quick Start Guide](quickstart.md)** provides a comprehensive tutorial covering:### Does PowerScript have interfaces?**Yes!**

- Variables and types

- Functions and classes

- Control flow

- Practical examplesYes! Basic interface support:```bash



## 🔮 Future Plans# Compile and run in one step



### What features are coming?```powerscripttps-run myfile.ps



**v1.1 (Q1 2026):**interface User {```

- 🔄 Advanced generics

- 🔄 Decorators    name: string;

- 🔄 Spread operator

    age: number;### How do I debug PowerScript code?

**v1.2 (Q2 2026):**

- 🔄 LSP with IntelliSense    email: string;

- 🔄 Debugger integration

- 🔄 Package manager}Currently, debug the compiled Python code:



See [Roadmap](../README.md#-roadmap) for full details.



### Will PowerScript stay free?class Person implements User {1. Compile: `tps-compile app.ps`



**Yes!** PowerScript is open-source (MIT License) and will always be free.    constructor(2. Debug `app.py` using Python debugger



### Can PowerScript replace Python?        public name: string,3. Use VS Code's Python debugging features



PowerScript **complements** Python:        public age: number,

- Use PowerScript for new projects with type safety

- Use Python for existing codebases        public email: string**Direct PowerScript debugging coming in v1.2!**

- Mix both - PowerScript transpiles to clean Python

    ) {}

## 🆘 Still Have Questions?

}### Is there a REPL for PowerScript?

- 📖 **Documentation:** [docs/](README.md)

- 💬 **Discussions:** [GitHub Discussions](https://github.com/SaleemLww/Python-PowerScript/discussions)```

- 🐛 **Issues:** [GitHub Issues](https://github.com/SaleemLww/Python-PowerScript/issues)

**Not yet.** REPL environment is planned for v2.0 (Q3 2026).

---

---

**Questions answered? Start building with [Quick Start](quickstart.md)! 🚀**

For now, use:

## 🛠️ Development Tools```bash

# Quick execution

### What editor should I use?tps-run script.ps

```

**VS Code** is recommended with the PowerScript extension for:

- Syntax highlighting---

- Code snippets (13 snippets)

- Error detection## 🔧 Compilation & Build

- File recognition

### What does the compiler output look like?

See [VS Code Extension Guide](vscode_extension.md) for setup.

Clean, readable Python code:

### What CLI commands are available?

**PowerScript:**

Four main commands:```powerscript

function greet(name: string): string {

| Command | Purpose |    return "Hello, " + name;

|---------|---------|}

| `tps-compile` | Compile `.ps` to `.py` |```

| `tps-run` | Compile and execute |

| `tps-create` | Create new project |**Compiled Python:**

| `tps-check` | Type check only |```python

def greet(name: str) -> str:

See [CLI Reference](cli_reference.md) for details.    return "Hello, " + name

```

### How do I create a new project?

### Does PowerScript add runtime overhead?

```bash

tps-create my-project**No!** PowerScript compiles to clean Python with minimal runtime imports. The generated code runs at native Python speed.

cd my-project

```### Can I customize the compilation output?



This creates a project structure with:**Yes!** Use `powerscript.toml`:

- `src/main.ps` - Your code

- `build/` - Compiled output```toml

- `powerscript.toml` - Configuration[compiler]

- `README.md` - Documentationoutput_dir = "build"

strict_types = true

### Can I type check without compiling?target_version = "3.9"

optimize = true

Yes!```



```bash### What if I want to see the generated Python code?

tps-check myfile.ps

```The compiled `.py` file is automatically created:



This validates types without generating Python code.```bash

tps-compile app.ps

### How do I debug PowerScript code?# Check app.py to see the generated code

```

Since PowerScript compiles to Python, you can debug the generated Python code:

---

1. Compile with `tps-compile`

2. Use Python debugger (`pdb` or VS Code Python debugger)## 🚨 Errors & Troubleshooting

3. Set breakpoints in generated `.py` files

### I get "command not found" error

---

**Solution:**

## 🔧 Troubleshooting

Add pip scripts to PATH:

### Why do I get "command not found: tps"?

```bash

**Solution 1: Add pip scripts to PATH**# macOS/Linux

```bashexport PATH="$HOME/.local/bin:$PATH"

# macOS/Linux

export PATH="$HOME/.local/bin:$PATH"# Windows

# Add to PATH: %USERPROFILE%\AppData\Local\Programs\Python\Python39\Scripts

# Windows```

# Add to PATH: %USERPROFILE%\AppData\Local\Programs\Python\Python39\Scripts

```Or use:

```bash

**Solution 2: Use full path**python -m powerscript.cli.cli --version

```bash```

python -m powerscript.cli.cli --version

```### Type checking errors - should I worry?



**Solution 3: Reinstall****Yes!** Type errors catch bugs early. Fix them before running:

```bash

pip install --force-reinstall tps```bash

```# Check types

tps-check app.ps

### Why doesn't VS Code highlight my `.ps` files?

# Fix errors, then compile

**Solutions:**tps-compile app.ps

1. Check language mode (bottom right) - should show "PowerScript"```

2. Manually set: `Cmd/Ctrl+K M` → type "powerscript"

3. Reload VS Code: `Cmd/Ctrl+Shift+P` → "Reload Window"### My PowerScript file won't compile

4. Reinstall extension

**Common issues:**

### How do I fix "ModuleNotFoundError: No module named 'powerscript'"?

1. **Syntax errors** - Check for typos, missing semicolons, bracket mismatches

**Solutions:**2. **Type errors** - Ensure types match

1. Activate virtual environment if used:3. **Import errors** - Verify module names

```bash

source .venv/bin/activateUse verbose mode:

``````bash

tps-compile app.ps -v

2. Reinstall TPS:```

```bash

pip install --force-reinstall tps### VS Code doesn't highlight my `.ps` files

```

**Solutions:**

3. Check Python version (must be 3.8+):

```bash1. Install PowerScript extension

python --version2. Reload VS Code

```3. Manually set language: `Cmd/Ctrl+K M` → "powerscript"



### Why do I get type errors?**See:** [VS Code Extension Guide](vscode_extension.md)



PowerScript enforces type safety. Common issues:---



**Type mismatch:**## 📚 Learning & Resources

```powerscript

// ❌ Wrong### Where can I learn PowerScript?

let x: number = "hello"; // Error: string is not number

1. **[Quick Start](quickstart.md)** - 5-minute tutorial

// ✅ Correct2. **[CLI Reference](cli_reference.md)** - Command-line tools

let x: number = 42;3. **[VS Code Extension](vscode_extension.md)** - IDE setup

```4. **Examples in `test_suits/`** - Working code samples



**Missing type:**### Is there a tutorial?

```powerscript

// ❌ Wrong**Yes!** Start with [Quick Start Guide](quickstart.md) which covers:

function add(a, b) { // Error: Missing types- Hello World

    return a + b;- Variables and types

}- Functions

- Classes

// ✅ Correct- Control flow

function add(a: number, b: number): number {- Practical examples

    return a + b;

}### Where can I find code examples?

```

**In the repository:**

### How do I handle compilation errors?- `test_suits/` - 15 core tests (100% passing)

- `test_suits/w3c/` - 43 feature tests

1. **Read the error message** - It tells you exactly what's wrong

2. **Check line number** - Error location is specified### Can I contribute to PowerScript?

3. **Fix the issue** - Usually a syntax or type error

4. **Recompile** - Try again**Absolutely!** We welcome:

- 🐛 Bug fixes

Example error:- ✨ New features

```- 📝 Documentation

Error at line 5: Expected ';' after statement- 🧪 Tests

```- 🎨 VS Code extension improvements



### My program runs in Python but not PowerScript. Why?**See the README for contribution guidelines.**



PowerScript has stricter rules than Python:---

- **Types required** - All variables/functions need types

- **Semicolons** - Statements should end with `;`## 🔄 Version & Updates

- **Syntax differences** - Use `function` instead of `def`, etc.

### What version should I use?

---

**Current:** v1.0.0 Beta - Production-ready!

## 🌐 Compatibility

Install latest:

### What Python versions are supported?```bash

pip install tps

**Minimum:** Python 3.8  ```

**Recommended:** Python 3.9+  

**Tested:** Python 3.8, 3.9, 3.10, 3.11### How do I update PowerScript?



### Can I use PowerScript with Django/Flask?```bash

pip install --upgrade tps

Yes! PowerScript can import and use any Python framework:```



```powerscript### What's coming in future versions?

import { Flask } from "python";

**v1.1 (Q1 2026):**

let app = Flask(__name__);- Advanced generics

- Decorators

app.route("/")(function(): string {- Namespace support

    return "Hello from PowerScript!";- Spread operator

});- Optional chaining

```

**v1.2 (Q2 2026):**

### Can I use PowerScript with NumPy/Pandas?- LSP with IntelliSense

- Debugger integration

Absolutely! Full access to data science libraries:- Package manager

- Test framework

```powerscript

import { numpy as np, pandas as pd } from "python";**v2.0 (Q3 2026):**

- Advanced type inference

function analyzeData(): void {- Compile-time optimizations

    let data = np.array([1, 2, 3, 4, 5]);- REPL environment

    let df = pd.DataFrame({ values: data });- Hot reloading

    console.log(df.describe());

}### Will my code break in future versions?

```

We strive for backward compatibility. Breaking changes will be:

### Does PowerScript work on Windows/Mac/Linux?- Clearly documented

- Announced in advance

Yes! PowerScript works on all platforms that support Python 3.8+:- Provided with migration guides

- ✅ Windows 7+

- ✅ macOS 10.12+---

- ✅ Linux (all modern distros)

## 🤝 Community & Support

See [Installation Guide](installation.md) for platform-specific instructions.

### Where can I get help?

### Can I deploy PowerScript apps to production?

1. **[GitHub Issues](https://github.com/SaleemLww/Python-PowerScript/issues)** - Bug reports

Yes! Since PowerScript compiles to Python, you can:2. **[GitHub Discussions](https://github.com/SaleemLww/Python-PowerScript/discussions)** - Questions

- Deploy compiled `.py` files anywhere Python runs3. **[This FAQ](faq.md)** - Common questions

- Use standard Python deployment tools (Docker, Heroku, AWS Lambda, etc.)

- No special runtime needed - just Python 3.8+### How can I report a bug?



---[Open an issue on GitHub](https://github.com/SaleemLww/Python-PowerScript/issues) with:

- PowerScript version

## 🔄 Migration- Python version

- Operating system

### How do I convert Python code to PowerScript?- Code that reproduces the bug

- Expected vs actual behavior

**Main changes:**

1. Add type annotations### Is there a community chat?

2. Change `def` to `function`

3. Add semicolonsUse [GitHub Discussions](https://github.com/SaleemLww/Python-PowerScript/discussions) for now.

4. Change `self` to `this` in classes

Discord/Slack planned for v1.2+.

**Python:**

```python### Can I use PowerScript for commercial projects?

def greet(name):

    return f"Hello, {name}!"**Yes!** PowerScript is MIT licensed - use it freely in commercial projects.

```

---

**PowerScript:**

```powerscript## 🎯 Use Cases

function greet(name: string): string {

    return "Hello, " + name + "!";### Is PowerScript good for web development?

}

```**Yes!** Use with Python web frameworks:



### How do I convert JavaScript to PowerScript?```powerscript

import { Flask } from "python";

PowerScript syntax is very similar to JavaScript! Main changes:

1. Replace `console.log()` usage stays the same ✅class WebApp {

2. Import Python libraries instead of Node modules    private app: any;

3. Some runtime APIs differ    

    constructor() {

**JavaScript:**        this.app = Flask(__name__);

```javascript    }

const fs = require('fs');    

let data = fs.readFileSync('file.txt', 'utf8');    run(): void {

```        this.app.run(debug: true);

    }

**PowerScript:**}

```powerscript```

import { FileSystem } from "powerscript/runtime";

let data: string = FileSystem.readFile("file.txt");### Can I use PowerScript for data science?

```

**Absolutely!** Full access to NumPy, pandas, matplotlib, scikit-learn, TensorFlow, PyTorch, etc.

---

```powerscript

## 📚 Learning Resourcesimport { pandas as pd, numpy as np } from "python";



### Where can I find examples?function analyze(csvPath: string): void {

    let df = pd.read_csv(csvPath);

Check the `test_suits/` folder in the repository:    console.log(df.describe());

- 15 core tests (100% passing)}

- 43 W3C feature tests```

- Covers all implemented features

### Is PowerScript suitable for AI/ML?

### Where can I find documentation?

**Yes!** PowerScript works perfectly with AI/ML libraries:

Complete documentation at:

- [Installation Guide](installation.md)```powerscript

- [Quick Start](quickstart.md)import { tensorflow as tf } from "python";

- [CLI Reference](cli_reference.md)

- [VS Code Extension](vscode_extension.md)class NeuralNetwork {

- [Main README](../README.md)    private model: any;

    

### Are there tutorials available?    async train(data: any, labels: any): Promise<void> {

        await this.model.fit(data, labels);

Yes! Start with:    }

1. [Quick Start Guide](quickstart.md) - 5-minute tutorial}

2. Example programs in `test_suits/````

3. Use cases in main [README](../README.md)

### Can I build desktop apps with PowerScript?

### How can I get help?

**Yes!** Use GUI libraries:

- **GitHub Issues** - Report bugs or request features

- **GitHub Discussions** - Ask questions, share projects```powerscript

- **Documentation** - Check docs firstimport { GUI } from "powerscript/runtime";

- **Examples** - Look at test files

class DesktopApp {

---    private window: any;

    

## 🤝 Contributing    constructor() {

        this.window = GUI.createWindow("My App", 800, 600);

### How can I contribute to PowerScript?    }

}

We welcome contributions! Ways to help:```

- 🐛 Report bugs

- ✨ Suggest features---

- 📝 Improve documentation

- 🧪 Write tests## 🔐 Security & Performance

- 💻 Submit code

### Is PowerScript secure?

See main [README](../README.md) for contribution guidelines.

PowerScript is as secure as Python since it compiles to Python code. Follow Python security best practices.

### Where is the source code?

### How's the performance?

GitHub: [SaleemLww/Python-PowerScript](https://github.com/SaleemLww/Python-PowerScript)

**Same as Python!** PowerScript compiles to clean Python code with no runtime overhead.

### How do I report a bug?

### Can I optimize PowerScript code?

1. Check if bug already reported

2. Open [GitHub Issue](https://github.com/SaleemLww/Python-PowerScript/issues)**Yes!** Use:

3. Provide:- Type annotations (helps compiler)

   - PowerScript version- Python optimization techniques

   - Python version- Profiling tools on compiled Python

   - Code example- Native Python extensions for speed-critical code

   - Expected vs actual behavior

   - Error message (if any)---



### Can I request new features?## 📖 Miscellaneous



Yes! Open a [GitHub Issue](https://github.com/SaleemLww/Python-PowerScript/issues) with:### What's the file extension?

- Feature description

- Use case`.ps` or `.pscript` (`.ps` recommended)

- Example syntax (optional)

- Why it would be useful### Can I use PowerScript in existing Python projects?



---**Yes!** Compile PowerScript to Python, then import:



## 🔮 Future```python

# Python code

### What features are coming soon?from mymodule import MyPowerScriptClass

```

See the roadmap in main [README](../README.md):

### Does PowerScript work with virtual environments?

**v1.1 (Q1 2026):**

- Advanced generics**Yes!** Recommended workflow:

- Decorators

- Namespace support```bash

- Spread operatorpython -m venv myenv

source myenv/bin/activate

**v1.2 (Q2 2026):**pip install tps

- LSP with IntelliSense```

- Code refactoring tools

- Debugger integration### Can I transpile back from Python to PowerScript?

- Package manager

**Not currently.** PowerScript → Python only.

**v2.0 (Q3 2026):**

- Advanced type inferencePython → PowerScript transpiler is a potential future feature.

- Compile-time optimizations

- Source maps---

- REPL environment

## 🎓 Still Have Questions?

### Will PowerScript stay free?

- 📧 [Open a GitHub Discussion](https://github.com/SaleemLww/Python-PowerScript/discussions)

Yes! PowerScript will always be **free and open source** under the MIT License.- 🐛 [Report an Issue](https://github.com/SaleemLww/Python-PowerScript/issues)

- 📚 [Read the Docs](README.md)

### How can I stay updated?

---

- ⭐ Star the [GitHub repository](https://github.com/SaleemLww/Python-PowerScript)

- 👀 Watch for releases**Didn't find your answer? Ask on [GitHub Discussions](https://github.com/SaleemLww/Python-PowerScript/discussions)! 💬**

- 📰 Follow discussions
- 🐦 Check for announcements

---

## 💡 Best Practices

### Should I use `any` type?

Use sparingly! The `any` type disables type checking:

```powerscript
// ❌ Avoid when possible
let data: any = "hello";

// ✅ Prefer specific types
let data: string = "hello";
```

### When should I use strict mode?

Always for production code:

```bash
tps-compile app.ps --strict
```

Strict mode:
- Enforces all type declarations
- Catches more errors
- Improves code quality

### How should I organize my project?

Recommended structure:

```
my-project/
├── src/              # Source code
│   ├── main.ps
│   ├── models/
│   └── utils/
├── build/            # Compiled output
├── tests/            # Test files
├── docs/             # Documentation
└── powerscript.toml  # Config
```

---

## 🆘 Still Have Questions?

**Can't find your answer?**

- 📖 Check [Documentation](README.md)
- 🔍 Search [GitHub Issues](https://github.com/SaleemLww/Python-PowerScript/issues)
- 💬 Ask in [GitHub Discussions](https://github.com/SaleemLww/Python-PowerScript/discussions)
- 📧 Contact maintainers

---

<div align="center">

**Questions answered? Start building with [Quick Start](quickstart.md)! 🚀**

</div>
