<div align="center">

# 🚀 PowerScript (TPS)

### *Modern Typed Syntax Meets Python's Power*

[![PyPI Version](https://img.shields.io/badge/pypi-v1.0.0--beta-blue?style=for-the-badge&logo=pypi)](https://pypi.org/project/tps/)
[![Python Version](https://img.shields.io/badge/python-3.8+-green?style=for-the-badge&logo=python)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-orange?style=for-the-badge)](LICENSE.txt)
[![Status](https://img.shields.io/badge/status-beta-yellow?style=for-the-badge)](https://github.com/SaleemLww/Python-PowerScript)

**A Modern Typed Programming Language that Transpiles to Python**

[📦 Install](#-installation) • [📚 Docs](docs/) • [🎯 Quick Start](docs/quickstart.md) • [💡 Examples](test_suits/) • [🤝 Contribute](#-contributing)

> **✅ Status: v1.0.0 Beta** — Production-ready with comprehensive feature set, full VS Code support, and extensive testing!

</div>

---

## 🌟 What is PowerScript?

PowerScript (TPS — **T**yped **P**ower**S**cript) is a modern programming language that transpiles to clean Python code.  
Write with JavaScript-familiar syntax, get Python's power!

```powerscript
// Clean, modern syntax with type safety
class NeuralNetwork {
    private model: any;

    constructor(layers: number[]) {
        this.model = this.buildModel(layers);
    }

    async train(data: any[], labels: any[]): Promise<void> {
        await this.model.fit(data, labels, {
            epochs: 10,
            batchSize: 32
        });
    }
}
```

---

## 🎯 Why PowerScript?

| Feature | PowerScript | Python | JavaScript |
|---------|-------------|--------|------------|
| 🎨 Modern Syntax | ✅ Clean & Familiar | ❌ Verbose | ✅ Modern |
| 🔒 Type Safety | ✅ Static + Runtime | ❌ Dynamic Only | ⚠️ Optional |
| 🐍 Python Ecosystem | ✅ Full Access | ✅ Native | ❌ No Access |
| ⚡ Performance | ✅ Python Speed | ✅ Native | ⚠️ V8 Engine |
| 🛠️ Tooling | ✅ VS Code Ext | ✅ Mature | ✅ Excellent |
| 📦 Easy Install | ✅ pip install | ✅ Built-in | ✅ npm install |

### ✨ Key Benefits

- **🎨 Modern Syntax** — Clean, familiar syntax inspired by JavaScript and modern languages  
- **🔒 Type Safety** — Static type checking with runtime validation  
- **🚀 Python Power** — Full access to Python's ecosystem (NumPy, TensorFlow, Django, etc.)  
- **🛠️ Production Ready** — Complete compiler toolchain with VS Code integration  
- **⚡ Zero Runtime** — Transpiles to clean Python, no runtime overhead  
- **🎓 Easy Learning** — If you know JavaScript or Python, you'll love PowerScript!

---

## 📦 Installation

### Quick Start (PyPI)

```bash
# Install TPS
pip install tps

# Verify installation
tps --version
```

### From Source

```bash
# Clone repository
git clone https://github.com/SaleemLww/Python-PowerScript.git
cd Python-PowerScript

# Install
pip install -e .
```

### VS Code Extension

```bash
# Install from VSIX
code --install-extension vscode-extension/powerscript-1.0.0.vsix
```

📚 **[Complete Installation Guide →](docs/installation.md)**

---

## ⚡ Quick Start

### Hello World

Create `hello.ps`:

```powerscript
function main(): void {
    console.log("Hello, PowerScript!");
}
```

Compile and run:

```bash
tps-compile hello.ps
python hello.py
# Output: Hello, PowerScript!
```

### Complete Example

```powerscript
// Calculator with type safety
class Calculator {
    add(a: number, b: number): number {
        return a + b;
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
    console.log("10 / 5 = " + calc.divide(10, 5));
}
```

🚀 **[5-Minute Tutorial →](docs/quickstart.md)**

---

## ✅ Implemented Features

### Core Language (Production Ready)

<details>
<summary><b>Type System</b> ✅</summary>

- ✅ Basic types: string, number, boolean, void, any, null, undefined  
- ✅ Array types: string[], number[], etc.  
- ✅ Function types with parameters and return types  
- ✅ Union types: string \| number  
- ✅ Type inference  
- ✅ Type annotations  
- ✅ Runtime type validation  

</details>

<details>
<summary><b>Functions & Classes</b> ✅</summary>

- ✅ Function declarations with types  
- ✅ Arrow functions  
- ✅ Class declarations  
- ✅ Constructor methods  
- ✅ Class properties (public/private)  
- ✅ Class methods  
- ✅ Inheritance (extends)  
- ✅ Static members  
- ✅ Access modifiers (public, private, protected)  

</details>

<details>
<summary><b>Control Flow</b> ✅</summary>

- ✅ If-else statements  
- ✅ Switch-case statements  
- ✅ For loops  
- ✅ While loops  
- ✅ Break/continue  
- ✅ Return statements  
- ✅ Ternary operators  

</details>

<details>
<summary><b>Advanced Features</b> ✅</summary>

- ✅ Async/await support  
- ✅ Promises  
- ✅ Enums  
- ✅ Interfaces (basic)  
- ✅ Abstract classes  
- ✅ Modules (import/export)  
- ✅ Destructuring (basic)  

</details>

---

### Runtime Libraries (Production Ready)

<details>
<summary><b>Built-in Modules</b> ✅</summary>

- ✅ **Console** — console.log(), console.error(), etc.  
- ✅ **FileSystem** — Read/write files, directory operations  
- ✅ **JSON** — Parse and stringify JSON  
- ✅ **CSV** — Read and write CSV files  
- ✅ **Database** — SQLite integration  
- ✅ **GUI** — Basic GUI operations (tkinter wrapper)  
- ✅ **Networking** — HTTP requests, web scraping  
- ✅ **Math** — Mathematical utilities  
- ✅ **DateTime** — Date and time operations  

</details>

---

### Development Tools (Production Ready)

- ✅ **tps-compile** — Compile `.ps` to `.py`  
- ✅ **tps-run** — Compile and execute  
- ✅ **tps-create** — Project scaffolding  
- ✅ **tps-check** — Type checking  
- ✅ **VS Code Extension** — Syntax highlighting, snippets, error detection  
- ✅ **CLI Tools** — Complete command-line interface  

---

## 🔄 Coming Soon

### v1.1 (Q1 2026)

- 🔄 Advanced generics  
- 🔄 Decorators  
- 🔄 Namespace support  
- 🔄 Advanced destructuring  
- 🔄 Spread operator  
- 🔄 Optional chaining (?.)  
- 🔄 Nullish coalescing (??)  

### v1.2 (Q2 2026)

- 🔄 Language Server Protocol (LSP) with IntelliSense  
- 🔄 Code refactoring tools  
- 🔄 Debugger integration  
- 🔄 Package manager  
- 🔄 Build system  
- 🔄 Test framework  

### v2.0 (Q3 2026)

- 🔄 Advanced type inference  
- 🔄 Compile-time optimizations  
- 🔄 Source maps  
- 🔄 REPL environment  
- 🔄 Hot reloading  
- 🔄 Plugin system  

---

## 💼 Use Cases

### 1. AI & Machine Learning

```powerscript
import { numpy as np, tensorflow as tf } from "python";

class AIModel {
    private model: any;

    constructor() {
        this.model = tf.keras.Sequential([
            tf.keras.layers.Dense(128, activation: "relu"),
            tf.keras.layers.Dense(10, activation: "softmax")
        ]);
    }

    async train(X: any, y: any): Promise<void> {
        this.model.compile({
            optimizer: "adam",
            loss: "sparse_categorical_crossentropy"
        });
        await this.model.fit(X, y, { epochs: 10 });
    }
}
```

### 2. Data Science

```powerscript
import { pandas as pd, matplotlib.pyplot as plt } from "python";

class DataAnalyzer {
    analyze(csvPath: string): void {
        let df = pd.read_csv(csvPath);
        console.log("Shape:", df.shape);
        console.log("Summary:", df.describe());

        // Visualize
        df.plot(kind: "hist");
        plt.show();
    }
}
```

### 3. Web Development

```powerscript
import { Flask } from "python";

class WebApp {
    private app: any;

    constructor() {
        this.app = Flask(__name__);
        this.setupRoutes();
    }

    setupRoutes(): void {
        this.app.route("/")(function(): string {
            return "Hello from PowerScript!";
        });
    }

    run(): void {
        this.app.run(debug: true);
    }
}
```

### 4. GUI Applications

```powerscript
import { GUI } from "powerscript/runtime";

class CalculatorApp {
    private window: any;

    constructor() {
        this.window = GUI.createWindow("Calculator", 300, 200);
        this.setupUI();
    }

    setupUI(): void {
        let button = GUI.createButton(this.window, "Calculate");
        button.onClick(() => {
            console.log("Calculating...");
        });
    }
}
```

### 5. Automation

```powerscript
import { FileSystem } from "powerscript/runtime";

class FileOrganizer {
    organize(directory: string): void {
        let files = FileSystem.listFiles(directory);

        for (let i = 0; i < files.length; i++) {
            let file = files[i];
            if (file.endsWith(".jpg") || file.endsWith(".png")) {
                FileSystem.move(file, directory + "/images/");
            }
        }

        console.log("Organization complete!");
    }
}
```

---

## 🧪 Testing & Quality


### Build Status

```bash
# Run all tests
cd test_suits
python run_all_tests.py
# ✅ All tests passed!
```

---

## 📚 Documentation

- **[Installation Guide](docs/installation.md)**  
- **[Quick Start](docs/quickstart.md)**  
- **[CLI Reference](docs/cli_reference.md)**  
- **[VS Code Extension](docs/vscode_extension.md)**  
- **[FAQ](docs/faq.md)**  

---

## 🛠️ CLI Commands

| Command | Description | Example |
|---------|-------------|---------|
| `tps-compile` | Compile `.ps` to `.py` | `tps-compile app.ps` |
| `tps-run` | Compile and execute | `tps-run app.ps` |
| `tps-create` | Create new project | `tps-create my-app` |
| `tps-check` | Type check only | `tps-check app.ps` |

---

## 🤝 Contributing

We welcome contributions! PowerScript is open source and community-driven.

### How to Contribute

1. **Fork the repository**  
2. **Create a feature branch:**  
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**  
4. **Run tests:**  
   ```bash
   python test_suits/run_all_tests.py
   ```
5. **Commit and push:**  
   ```bash
   git commit -m "Add amazing feature"
   git push origin feature/amazing-feature
   ```
6. **Open a Pull Request**

### Development Setup

```bash
# Clone repository
git clone https://github.com/SaleemLww/Python-PowerScript.git
cd Python-PowerScript

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run tests
python test_suits/run_all_tests.py
```

### Areas for Contribution

- 🐛 **Bug Fixes**  
- ✨ **New Features**  
- 📝 **Documentation**  
- 🧪 **Tests**  
- 🎨 **VS Code Extension**  
- 🌐 **Examples**  

---

## 📄 License

PowerScript is released under the **MIT License**.  
See [LICENSE.txt](LICENSE.txt) for details.

```
MIT License

Copyright (c) 2024-2025 Elite India Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🌟 Support

- ⭐ **Star this repository** if you find it useful!  
- 🐛 **Report issues** on [GitHub Issues](https://github.com/SaleemLww/Python-PowerScript/issues)  
- 💬 **Join discussions** on [GitHub Discussions](https://github.com/SaleemLww/Python-PowerScript/discussions)  
- 📧 **Contact:** [GitHub Profile](https://github.com/SaleemLww)

---

## 🎯 Roadmap

### ✅ Completed (v1.0 Beta)

- ✅ Core language  
- ✅ Type system  
- ✅ Classes & inheritance  
- ✅ Async/await  
- ✅ Runtime libs  
- ✅ CLI tools  
- ✅ VS Code extension  
- ✅ Tests  

### 🚧 In Progress

- 🔄 Generics  
- 🔄 LSP integration  
- 🔄 Package manager  
- 🔄 Better errors  

### 📅 Future

- 🔮 Compile-time optimizations  
- 🔮 Plugin system  
- 🔮 REPL environment  
- 🔮 Hot reloading  

---

<div align="center">

**Built with ❤️ by Elite India Team**

[⬆️ Back to Top](#-powerscript-tps)

</div>
