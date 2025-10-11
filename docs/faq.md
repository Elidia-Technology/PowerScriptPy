# ❓ Frequently Asked Questions (FAQ)

Common questions about PowerScript answered.

---

## 🎯 General Questions

### What is PowerScript?

PowerScript (TPS - Typed PowerScript) is a modern programming language that transpiles to Python. It provides JavaScript-like syntax with static typing while giving you full access to Python's ecosystem.

### Why use PowerScript instead of Python?

**PowerScript offers:**
- ✅ Modern, familiar syntax (inspired by JavaScript/TypeScript)
- ✅ Static type checking with runtime validation
- ✅ Better tooling (VS Code extension with IntelliSense coming soon)
- ✅ Cleaner, more expressive code
- ✅ Full Python ecosystem access (NumPy, TensorFlow, Django, etc.)

**Use PowerScript when:**
- You prefer JavaScript-style syntax
- You want static type safety
- You're building large, maintainable projects
- You want modern language features with Python's power

### Is PowerScript production-ready?

**Yes!** PowerScript v1.0.0 Beta is production-ready with:
- ✅ Stable compiler
- ✅ Complete type system
- ✅ Runtime libraries
- ✅ CLI tools
- ✅ VS Code extension
- ✅ Comprehensive testing

### What's the relationship between PowerScript and Python?

PowerScript transpiles to clean Python code. This means:
- PowerScript code → Compiles to → Python code → Runs on Python interpreter
- Full access to Python libraries
- Same performance as Python
- Can import Python modules directly
- No runtime overhead

---

## 📦 Installation & Setup

### How do I install PowerScript?

```bash
# Simple installation via pip
pip install tps

# Verify
tps --version
```

**See:** [Installation Guide](installation.md)

### What are the system requirements?

**Minimum:**
- Python 3.8+
- 512 MB RAM
- 50 MB disk space

**Recommended:**
- Python 3.9+
- 2 GB RAM
- 200 MB disk space
- VS Code with PowerScript extension

### Do I need to install Python separately?

**Yes.** PowerScript requires Python 3.8+ to be installed since it transpiles to Python code.

### Can I use PowerScript with my existing Python projects?

**Yes!** PowerScript can:
- Import existing Python modules
- Call Python functions
- Use Python classes
- Mix with Python code in the same project

---

## 💻 Language Features

### What types does PowerScript support?

**Basic Types:**
- `string`, `number`, `boolean`
- `void`, `any`, `null`, `undefined`

**Complex Types:**
- Arrays: `string[]`, `number[]`
- Union types: `string | number`
- Function types
- Class types
- Interface types

**See:** [Quick Start - Types](quickstart.md)

### Does PowerScript support async/await?

**Yes!** PowerScript fully supports:
- ✅ `async` functions
- ✅ `await` keyword
- ✅ Promises
- ✅ Asynchronous operations

Example:
```powerscript
async function fetchData(): Promise<string> {
    let response = await fetch("https://api.example.com");
    return response.text();
}
```

### Can I use Python libraries in PowerScript?

**Absolutely!** Import any Python library:

```powerscript
import { numpy as np, pandas as pd } from "python";

function main(): void {
    let arr = np.array([1, 2, 3, 4, 5]);
    console.log(arr.mean());
}
```

### Does PowerScript have classes and OOP?

**Yes!** Full OOP support:
- ✅ Classes
- ✅ Constructors
- ✅ Inheritance (`extends`)
- ✅ Access modifiers (`public`, `private`, `protected`)
- ✅ Static members
- ✅ Abstract classes
- ✅ Interfaces (basic)

### What about generics?

**Coming in v1.1!** Basic generics work, but advanced generics are planned for Q1 2026.

---

## 🛠️ Development

### Which IDE should I use?

**Recommended: VS Code** with the PowerScript extension.

**Features:**
- Syntax highlighting
- Code snippets
- Error detection
- IntelliSense (coming soon)

**See:** [VS Code Extension Guide](vscode_extension.md)

### How do I compile PowerScript code?

```bash
# Compile to Python
tps-compile myfile.ps

# Output: myfile.py
```

**See:** [CLI Reference](cli_reference.md)

### Can I run PowerScript directly?

**Yes!**

```bash
# Compile and run in one step
tps-run myfile.ps
```

### How do I debug PowerScript code?

Currently, debug the compiled Python code:

1. Compile: `tps-compile app.ps`
2. Debug `app.py` using Python debugger
3. Use VS Code's Python debugging features

**Direct PowerScript debugging coming in v1.2!**

### Is there a REPL for PowerScript?

**Not yet.** REPL environment is planned for v2.0 (Q3 2026).

For now, use:
```bash
# Quick execution
tps-run script.ps
```

---

## 🔧 Compilation & Build

### What does the compiler output look like?

Clean, readable Python code:

**PowerScript:**
```powerscript
function greet(name: string): string {
    return "Hello, " + name;
}
```

**Compiled Python:**
```python
def greet(name: str) -> str:
    return "Hello, " + name
```

### Does PowerScript add runtime overhead?

**No!** PowerScript compiles to clean Python with minimal runtime imports. The generated code runs at native Python speed.

### Can I customize the compilation output?

**Yes!** Use `powerscript.toml`:

```toml
[compiler]
output_dir = "build"
strict_types = true
target_version = "3.9"
optimize = true
```

### What if I want to see the generated Python code?

The compiled `.py` file is automatically created:

```bash
tps-compile app.ps
# Check app.py to see the generated code
```

---

## 🚨 Errors & Troubleshooting

### I get "command not found" error

**Solution:**

Add pip scripts to PATH:

```bash
# macOS/Linux
export PATH="$HOME/.local/bin:$PATH"

# Windows
# Add to PATH: %USERPROFILE%\AppData\Local\Programs\Python\Python39\Scripts
```

Or use:
```bash
python -m powerscript.cli.cli --version
```

### Type checking errors - should I worry?

**Yes!** Type errors catch bugs early. Fix them before running:

```bash
# Check types
tps-check app.ps

# Fix errors, then compile
tps-compile app.ps
```

### My PowerScript file won't compile

**Common issues:**

1. **Syntax errors** - Check for typos, missing semicolons, bracket mismatches
2. **Type errors** - Ensure types match
3. **Import errors** - Verify module names

Use verbose mode:
```bash
tps-compile app.ps -v
```

### VS Code doesn't highlight my `.ps` files

**Solutions:**

1. Install PowerScript extension
2. Reload VS Code
3. Manually set language: `Cmd/Ctrl+K M` → "powerscript"

**See:** [VS Code Extension Guide](vscode_extension.md)

---

## 📚 Learning & Resources

### Where can I learn PowerScript?

1. **[Quick Start](quickstart.md)** - 5-minute tutorial
2. **[CLI Reference](cli_reference.md)** - Command-line tools
3. **[VS Code Extension](vscode_extension.md)** - IDE setup
4. **Examples in `test_suits/`** - Working code samples

### Is there a tutorial?

**Yes!** Start with [Quick Start Guide](quickstart.md) which covers:
- Hello World
- Variables and types
- Functions
- Classes
- Control flow
- Practical examples

### Where can I find code examples?

**In the repository:**
- `test_suits/` - 15 core tests (100% passing)
- `test_suits/w3c/` - 43 feature tests

### Can I contribute to PowerScript?

**Absolutely!** We welcome:
- 🐛 Bug fixes
- ✨ New features
- 📝 Documentation
- 🧪 Tests
- 🎨 VS Code extension improvements

**See the README for contribution guidelines.**

---

## 🔄 Version & Updates

### What version should I use?

**Current:** v1.0.0 Beta - Production-ready!

Install latest:
```bash
pip install tps
```

### How do I update PowerScript?

```bash
pip install --upgrade tps
```

### What's coming in future versions?

**v1.1 (Q1 2026):**
- Advanced generics
- Decorators
- Namespace support
- Spread operator
- Optional chaining

**v1.2 (Q2 2026):**
- LSP with IntelliSense
- Debugger integration
- Package manager
- Test framework

**v2.0 (Q3 2026):**
- Advanced type inference
- Compile-time optimizations
- REPL environment
- Hot reloading

### Will my code break in future versions?

We strive for backward compatibility. Breaking changes will be:
- Clearly documented
- Announced in advance
- Provided with migration guides

---

## 🤝 Community & Support

### Where can I get help?

1. **[GitHub Issues](https://github.com/SaleemLww/Python-PowerScript/issues)** - Bug reports
2. **[GitHub Discussions](https://github.com/SaleemLww/Python-PowerScript/discussions)** - Questions
3. **[This FAQ](faq.md)** - Common questions

### How can I report a bug?

[Open an issue on GitHub](https://github.com/SaleemLww/Python-PowerScript/issues) with:
- PowerScript version
- Python version
- Operating system
- Code that reproduces the bug
- Expected vs actual behavior

### Is there a community chat?

Use [GitHub Discussions](https://github.com/SaleemLww/Python-PowerScript/discussions) for now.

Discord/Slack planned for v1.2+.

### Can I use PowerScript for commercial projects?

**Yes!** PowerScript is MIT licensed - use it freely in commercial projects.

---

## 🎯 Use Cases

### Is PowerScript good for web development?

**Yes!** Use with Python web frameworks:

```powerscript
import { Flask } from "python";

class WebApp {
    private app: any;
    
    constructor() {
        this.app = Flask(__name__);
    }
    
    run(): void {
        this.app.run(debug: true);
    }
}
```

### Can I use PowerScript for data science?

**Absolutely!** Full access to NumPy, pandas, matplotlib, scikit-learn, TensorFlow, PyTorch, etc.

```powerscript
import { pandas as pd, numpy as np } from "python";

function analyze(csvPath: string): void {
    let df = pd.read_csv(csvPath);
    console.log(df.describe());
}
```

### Is PowerScript suitable for AI/ML?

**Yes!** PowerScript works perfectly with AI/ML libraries:

```powerscript
import { tensorflow as tf } from "python";

class NeuralNetwork {
    private model: any;
    
    async train(data: any, labels: any): Promise<void> {
        await this.model.fit(data, labels);
    }
}
```

### Can I build desktop apps with PowerScript?

**Yes!** Use GUI libraries:

```powerscript
import { GUI } from "powerscript/runtime";

class DesktopApp {
    private window: any;
    
    constructor() {
        this.window = GUI.createWindow("My App", 800, 600);
    }
}
```

---

## 🔐 Security & Performance

### Is PowerScript secure?

PowerScript is as secure as Python since it compiles to Python code. Follow Python security best practices.

### How's the performance?

**Same as Python!** PowerScript compiles to clean Python code with no runtime overhead.

### Can I optimize PowerScript code?

**Yes!** Use:
- Type annotations (helps compiler)
- Python optimization techniques
- Profiling tools on compiled Python
- Native Python extensions for speed-critical code

---

## 📖 Miscellaneous

### What's the file extension?

`.ps` or `.pscript` (`.ps` recommended)

### Can I use PowerScript in existing Python projects?

**Yes!** Compile PowerScript to Python, then import:

```python
# Python code
from mymodule import MyPowerScriptClass
```

### Does PowerScript work with virtual environments?

**Yes!** Recommended workflow:

```bash
python -m venv myenv
source myenv/bin/activate
pip install tps
```

### Can I transpile back from Python to PowerScript?

**Not currently.** PowerScript → Python only.

Python → PowerScript transpiler is a potential future feature.

---

## 🎓 Still Have Questions?

- 📧 [Open a GitHub Discussion](https://github.com/SaleemLww/Python-PowerScript/discussions)
- 🐛 [Report an Issue](https://github.com/SaleemLww/Python-PowerScript/issues)
- 📚 [Read the Docs](README.md)

---

**Didn't find your answer? Ask on [GitHub Discussions](https://github.com/SaleemLww/Python-PowerScript/discussions)! 💬**
