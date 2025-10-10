# PowerScript

**A fully structured development language that transpiles to Python**

PowerScript is a modern, strongly-typed programming language designed for AI and data science workflows. It combines the expressiveness of Python with robust type safety, access modifiers, and advanced language features, all while maintaining full compatibility with the Python ecosystem.

## 🌟 Features

### Core Language Features
- **Strong Type System**: Static type checking with optional runtime validation
- **Access Modifiers**: `public`, `private`, and `protected` visibility controls
- **Async/Await**: First-class async programming support
- **Generic Types**: Full generic programming support with constraints
- **Class-based OOP**: Modern object-oriented programming with constructors
- **Optional Chaining**: Safe navigation with `?.` operator
- **Null Coalescing**: Default values with `??` operator

### Development Tools
- **Transpiler**: Converts PowerScript to clean, readable Python code
- **Type Checker**: Static analysis with error reporting and suggestions
- **CLI Tools**: Complete command-line interface for development workflow
- **VS Code Extension**: Full IDE support with syntax highlighting, IntelliSense, and debugging
- **LSP Server**: Language Server Protocol for editor integration
- **Watch Mode**: Automatic recompilation on file changes

### AI/ML Ready
- **NumPy/Pandas Integration**: Seamless data science library support
- **PyTorch/TensorFlow Support**: ML framework compatibility
- **Async Training Pipelines**: Built for scalable AI workflows
- **Type-Safe Data Structures**: Strongly typed arrays, matrices, and tensors

## 🚀 Quick Start

### Installation

```bash
pip install powerscript
```

### Create Your First Project

```bash
# Create a new PowerScript project
ps-create my_project

# Navigate to project
cd my_project

# Compile and run
powerscript compile src/ -o build/
powerscript run src/main.ps
```

### Example PowerScript Code

```powerscript
// classes.ps - Object-oriented programming
class DataProcessor<T> {
    private data: Array<T>;
    
    constructor(initialData: Array<T>) {
        this.data = initialData;
    }
    
    public async function process(): Array<T> {
        // Type-safe data processing
        return this.data.filter(item => item !== null);
    }
    
    protected function validate(item: T): boolean {
        return item !== undefined && item !== null;
    }
}

// main.ps - Async main function
async function main(): void {
    let processor: DataProcessor<number> = new DataProcessor([1, 2, null, 4, 5]);
    let cleaned: Array<number> = await processor.process();
    
    print("Processed data:", cleaned);
}

main();
```

## 📚 Language Guide

### Type System

PowerScript features a comprehensive type system with both static checking and optional runtime enforcement:

```powerscript
// Basic types
let name: string = "PowerScript";
let count: number = 42;
let isActive: boolean = true;
let data: Array<number> = [1, 2, 3];

// Optional types
let optional: string? = null;
let result: string = optional ?? "default";

// Generic functions
function identity<T>(value: T): T {
    return value;
}

// Type inference
let inferred = identity("hello"); // Type: string
```

### Classes and Access Modifiers

```powerscript
class BankAccount {
    private balance: number;
    protected accountId: string;
    public readonly owner: string;
    
    constructor(owner: string, initialBalance: number = 0) {
        this.owner = owner;
        this.balance = initialBalance;
        this.accountId = this.generateId();
    }
    
    public function getBalance(): number {
        return this.balance;
    }
    
    private function generateId(): string {
        return "ACC_" + Math.random().toString();
    }
}
```

### Async Programming

```powerscript
class APIClient {
    private baseUrl: string;
    
    constructor(baseUrl: string) {
        this.baseUrl = baseUrl;
    }
    
    public async function fetchData<T>(endpoint: string): Promise<T> {
        let response = await fetch(this.baseUrl + endpoint);
        return await response.json();
    }
    
    public async function batchRequest<T>(endpoints: Array<string>): Promise<Array<T>> {
        let promises = endpoints.map(endpoint => this.fetchData<T>(endpoint));
        return await Promise.all(promises);
    }
}
```

## 🛠️ CLI Commands

### Compilation

```bash
# Compile single file
powerscriptc main.ps -o build/

# Compile directory with watch mode
powerscriptc src/ -o build/ --watch

# Strict type checking
powerscriptc src/ -o build/ --strict

# Generate Python stub files
powerscriptc src/ -o build/ --generate-stubs
```

### Running Code

```bash
# Run PowerScript file directly
ps-run main.ps

# Run with arguments
ps-run main.ps --arg1 value1 --arg2 value2

# Run without cache
ps-run main.ps --no-cache
```

### Type Checking

```bash
# Check types
psc src/

# Strict mode
psc src/ --strict

# JSON output
psc src/ --json
```

### Project Creation

```bash
# Basic project
ps-create my_project

# AI/ML project
ps-create my_ai_project --template ai

# Web project
ps-create my_web_app --template web

# CLI project
ps-create my_cli_tool --template cli
```

## 🔧 Configuration

Configure your project with `powerscript.toml`:

```toml
[project]
name = "my_project"
version = "0.1.0"
main = "src/main.ps"
description = "My PowerScript project"

[compiler]
output_dir = "build"
strict_typing = true
runtime_checks = true
target_python_version = "3.8"
generate_stubs = true

[runtime]
async_enabled = true
access_modifiers = true
type_validation = "strict"

[lsp]
enabled = true
diagnostics = true
auto_complete = true
```

## 🎯 Use Cases

### Data Science & AI

```powerscript
class NeuralNetwork {
    private layers: Array<Layer>;
    private optimizer: Optimizer;
    
    constructor(architecture: Array<number>) {
        this.layers = this.buildLayers(architecture);
        this.optimizer = new AdamOptimizer();
    }
    
    public async function train(data: TrainingData, epochs: number): Promise<TrainingResult> {
        for (let epoch = 0; epoch < epochs; epoch++) {
            let loss = await this.forwardPass(data);
            await this.backwardPass(loss);
            
            if (epoch % 100 === 0) {
                print(`Epoch ${epoch}, Loss: ${loss}`);
            }
        }
        
        return new TrainingResult(this.getLoss(), this.getAccuracy());
    }
}
```

### Web APIs

```powerscript
class UserController {
    private userService: UserService;
    
    constructor(userService: UserService) {
        this.userService = userService;
    }
    
    public async function createUser(request: CreateUserRequest): Promise<UserResponse> {
        let user = await this.userService.create(request);
        return new UserResponse(user);
    }
    
    public async function getUser(id: string): Promise<UserResponse> {
        let user = await this.userService.findById(id);
        if (!user) {
            throw new NotFoundError("User not found");
        }
        return new UserResponse(user);
    }
}
```

## 🏗️ Architecture

PowerScript is built with a modular architecture:

```
powerscript/
├── compiler/          # Lexer, Parser, AST, Transpiler
├── runtime/           # Access modifiers, type validation, async helpers
├── typechecker/       # Static type analysis
├── cli/               # Command-line tools
├── lsp/               # Language Server Protocol
├── vscode-extension/  # VS Code integration
├── tests/             # Test suite
├── examples/          # Example projects
└── docs/              # Documentation
```

## 🔌 VS Code Extension

Install the PowerScript VS Code extension for the best development experience:

- **Syntax Highlighting**: Full PowerScript syntax support
- **IntelliSense**: Auto-completion, hover docs, signature help
- **Error Diagnostics**: Real-time type checking and error reporting
- **Go to Definition**: Navigate to symbol definitions
- **Debugging**: Integrated debugging with source maps
- **Snippets**: Code templates for common patterns

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

```bash
# Clone the repository
git clone https://github.com/powerscript/powerscript.git
cd powerscript

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .

# Run tests
pytest tests/

# Format code
black powerscript/
```

## 📖 Documentation

- [Language Reference](docs/language-reference.md)
- [API Documentation](docs/api.md)
- [CLI Guide](docs/cli.md)
- [VS Code Extension](docs/vscode.md)
- [Examples](examples/)

## 🎯 Roadmap

### Phase 1: Core Language ✅
- [x] Lexer and Parser
- [x] AST Definition
- [x] Basic Transpiler
- [x] Type System Foundation

### Phase 2: Advanced Features 🚧
- [x] Access Modifiers
- [x] Runtime Validation
- [x] CLI Tools
- [ ] Generic Constraints
- [ ] Pattern Matching

### Phase 3: Developer Experience 📋
- [ ] LSP Server
- [ ] VS Code Extension
- [ ] Debugging Support
- [ ] Source Maps

### Phase 4: AI Integration 📋
- [ ] NumPy/Pandas Integration
- [ ] ML Framework Support
- [ ] Tensor Types
- [ ] GPU Acceleration

## 📄 License

PowerScript is released under the MIT License. See [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

PowerScript builds upon the excellent work of:
- Python language and ecosystem
- Lark parsing toolkit
- Beartype runtime validation
- VS Code Language Server Protocol
- The open-source community

---

**Ready to supercharge your Python development with PowerScript?**

```bash
pip install powerscript
ps-create my_first_project
cd my_first_project
powerscript run src/main.ps
```

Join our community: [Discord](https://discord.gg/powerscript) | [Twitter](https://twitter.com/powerscriptlang) | [GitHub](https://github.com/powerscript/powerscript)