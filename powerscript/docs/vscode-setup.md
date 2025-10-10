# PowerScript VS Code Extension Setup Guide

## Overview

The PowerScript VS Code extension provides complete IDE support for PowerScript development including:

- **Syntax Highlighting** - Beautiful, accurate syntax coloring
- **IntelliSense** - Auto-completion, parameter hints, quick info
- **Error Diagnostics** - Real-time error checking and warnings  
- **Go to Definition** - Navigate to symbols and declarations
- **Hover Information** - Type information and documentation
- **Code Snippets** - Quick templates for common patterns
- **Debugging Support** - Breakpoints and step-through debugging
- **Project Management** - Integrated compilation and running

## Installation

### Method 1: From VS Code Marketplace (Coming Soon)

1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X / Cmd+Shift+X)
3. Search for "PowerScript"
4. Click "Install" on the PowerScript extension

### Method 2: Manual Installation (Current)

1. **Build the Extension**
   ```bash
   cd powerscript/vscode-extension/
   npm install
   npm run compile
   vsce package
   ```

2. **Install the .vsix File**
   ```bash
   code --install-extension powerscript-0.1.0.vsix
   ```

3. **Or Install via VS Code UI**
   - Open VS Code
   - Press Ctrl+Shift+P (Cmd+Shift+P on Mac)
   - Type "Extensions: Install from VSIX"
   - Select the generated .vsix file

### Method 3: Development Mode

For development and testing:

```bash
# Clone the repository
git clone https://github.com/SaleemLww/Python-PowerScript.git
cd Python-PowerScript/powerscript/vscode-extension/

# Install dependencies
npm install

# Open in VS Code
code .

# Press F5 to launch Extension Development Host
```

## Features Overview

### 1. Syntax Highlighting

PowerScript files (`.ps`) are automatically recognized and highlighted with:

- **Keywords**: `class`, `function`, `let`, `const`, `async`, `await`
- **Types**: `string`, `number`, `boolean`, `Array`, `Promise`
- **Access Modifiers**: `public`, `private`, `protected`
- **Comments**: Single-line `//` and multi-line `/* */`
- **Strings**: Template literals with `${}` interpolation
- **Numbers**: Integers, floats, scientific notation
- **Operators**: Arithmetic, logical, comparison operators

### 2. IntelliSense

The extension provides intelligent code completion:

**Class Members**
```powerscript
class MyClass {
    private value: number;
    
    constructor(value: number) {
        this.| // Shows: value, constructor methods
    }
}
```

**Function Parameters**
```powerscript
function process(data: string, options: any): void {
    // Parameter hints when calling process(|)
}
```

**Built-in Types and Keywords**
- Type suggestions: `string`, `number`, `boolean`, `Array<T>`
- Keyword completion: `class`, `function`, `async`, `await`
- Access modifiers: `public`, `private`, `protected`

### 3. Error Diagnostics

Real-time error checking with:

- **Syntax Errors**: Immediately highlighted in red
- **Type Errors**: Type mismatches and violations
- **Access Violations**: Private/protected member access
- **Undefined Variables**: Usage of undeclared variables

### 4. Code Snippets

Quick templates for common PowerScript patterns:

**Class Snippet** (`ps-class`)
```powerscript
class ${1:ClassName} {
    ${2:// properties}
    
    constructor(${3:parameters}) {
        ${4:// initialization}
    }
    
    ${5:// methods}
}
```

**Function Snippet** (`ps-function`)
```powerscript
function ${1:functionName}(${2:parameters}): ${3:returnType} {
    ${4:// implementation}
}
```

**Async Function Snippet** (`ps-async`)
```powerscript
async function ${1:functionName}(${2:parameters}): Promise<${3:returnType}> {
    ${4:// implementation}
}
```

**For Loop Snippet** (`ps-for`)
```powerscript
for (let ${1:i} = 0; ${1:i} < ${2:length}; ${1:i}++) {
    ${3:// loop body}
}
```

## Configuration

### Extension Settings

Configure PowerScript extension in VS Code settings (`settings.json`):

```json
{
    "powerscript.enable": true,
    "powerscript.trace.server": "verbose",
    "powerscript.compiler.outputDirectory": "build",
    "powerscript.compiler.strictMode": true,
    "powerscript.compiler.runtimeChecks": false,
    "powerscript.typeChecker.enabled": true,
    "powerscript.typeChecker.strictMode": true,
    "powerscript.lsp.maxNumberOfProblems": 100,
    "powerscript.formatting.enabled": true,
    "powerscript.snippets.enabled": true
}
```

### Workspace Settings

For project-specific settings, create `.vscode/settings.json`:

```json
{
    "powerscript.compiler.outputDirectory": "./build",
    "powerscript.compiler.watchMode": true,
    "powerscript.typeChecker.strictMode": true,
    "files.associations": {
        "*.ps": "powerscript"
    }
}
```

### PowerScript Project Configuration

Ensure your project has a `powerscript.toml`:

```toml
[project]
name = "my_project"
version = "1.0.0"
main = "src/main.ps"

[compiler]
output_dir = "build"
strict_typing = true
runtime_checks = true

[lsp]
port = 2087
diagnostics = true
completion = true
hover = true
```

## Usage Guide

### 1. Creating a New PowerScript File

1. **Create File**: Right-click in Explorer → "New File" → `example.ps`
2. **Auto Language Detection**: VS Code automatically detects PowerScript syntax
3. **Start Coding**: Begin with syntax highlighting and IntelliSense active

### 2. IntelliSense in Action

**Type Completion**
```powerscript
let name: str| // Type 'str' → suggests 'string'
```

**Method Completion**
```powerscript
class Calculator {
    add(a: number, b: number): number { return a + b; }
}

let calc = new Calculator();
calc.| // Shows: add method with signature
```

**Import Suggestions**
```powerscript
import { | } from "./utils"; // Shows exported symbols
```

### 3. Error Detection

The extension shows errors in real-time:

**Syntax Error**
```powerscript
class MyClass {
    method() {
        // Missing closing brace - highlighted in red
}
```

**Type Error**
```powerscript
let count: number = "hello"; // Type error underlined
```

**Access Error**
```powerscript
class Test {
    private secret: string = "hidden";
}

let t = new Test();
console.log(t.secret); // Access violation warning
```

### 4. Navigation Features

**Go to Definition** (F12 or Ctrl+Click)
```powerscript
class UserService {
    getUser(id: number): User { /* ... */ }
}

let service = new UserService();
service.getUser(1); // F12 on getUser goes to definition
```

**Find All References** (Shift+F12)
- Shows all usages of a symbol across files
- Useful for refactoring and understanding code flow

### 5. Hover Information

Hover over any symbol to see:
- Type information
- Documentation comments
- Parameter details
- Return type information

```powerscript
/**
 * Calculates the factorial of a number
 * @param n The number to calculate factorial for
 * @returns The factorial result
 */
function factorial(n: number): number {
    return n <= 1 ? 1 : n * factorial(n - 1);
}

// Hover over 'factorial' shows full documentation
let result = factorial(5);
```

## Debugging

### Setup Debugging

1. **Create Launch Configuration** (`.vscode/launch.json`):
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "PowerScript Debug",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/build/main.py",
            "console": "integratedTerminal",
            "preLaunchTask": "powerscript-compile"
        }
    ]
}
```

2. **Create Build Task** (`.vscode/tasks.json`):
```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "powerscript-compile",
            "type": "shell",
            "command": "powerscriptc",
            "args": ["src/", "-o", "build/"],
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "silent",
                "focus": false,
                "panel": "shared"
            },
            "problemMatcher": {
                "owner": "powerscript",
                "fileLocation": ["relative", "${workspaceFolder}"],
                "pattern": {
                    "regexp": "^(.*):(\\d+):(\\d+):\\s+(warning|error):\\s+(.*)$",
                    "file": 1,
                    "line": 2,
                    "column": 3,
                    "severity": 4,
                    "message": 5
                }
            }
        }
    ]
}
```

### Debugging Features

- **Breakpoints**: Set breakpoints in PowerScript files
- **Source Maps**: Debug compiled Python with PowerScript line numbers
- **Variable Inspection**: Inspect variables and call stack
- **Step Through**: Step over, into, and out of functions
- **Watch Expressions**: Monitor expressions during debugging

### Debug Session

1. **Set Breakpoints**: Click in the gutter next to line numbers
2. **Start Debugging**: Press F5 or use "Run → Start Debugging"
3. **Step Through Code**: Use F10 (step over), F11 (step into), Shift+F11 (step out)
4. **Inspect Variables**: Hover over variables or use Debug Console

## Advanced Features

### 1. Custom Snippets

Add custom snippets in VS Code settings:

```json
{
    "powerscript-custom-snippets": {
        "AI Model Class": {
            "prefix": "ps-ai-model",
            "body": [
                "class ${1:ModelName} {",
                "    private model: any;",
                "    ",
                "    constructor() {",
                "        this.model = null;",
                "    }",
                "    ",
                "    public async train(data: any): Promise<void> {",
                "        ${2:// Training implementation}",
                "    }",
                "    ",
                "    public predict(input: any): any {",
                "        ${3:// Prediction implementation}",
                "    }",
                "}"
            ],
            "description": "AI model class template"
        }
    }
}
```

### 2. Workspace Integration

**Multi-root Workspaces**
```json
{
    "folders": [
        {"path": "./frontend"},
        {"path": "./backend"},
        {"path": "./shared"}
    ],
    "settings": {
        "powerscript.compiler.outputDirectory": "dist"
    }
}
```

**File Associations**
```json
{
    "files.associations": {
        "*.ps": "powerscript",
        "*.powerscript": "powerscript"
    }
}
```

### 3. Integration with Other Extensions

**Python Extension Integration**
- Seamless debugging of compiled Python code
- IntelliSense for Python libraries used in PowerScript
- Integrated terminal with Python environment

**Git Integration**
- Source control for `.ps` files
- Diff view for PowerScript code
- Git blame and history for PowerScript files

## Troubleshooting

### Common Issues

**1. Extension Not Activating**
```json
// Check file associations in settings.json
{
    "files.associations": {
        "*.ps": "powerscript"
    }
}
```

**2. IntelliSense Not Working**
- Ensure PowerScript LSP server is running
- Check `powerscript.toml` configuration
- Restart VS Code or reload window (Ctrl+Shift+P → "Developer: Reload Window")

**3. Compilation Errors in Problems Panel**
- Verify PowerScript CLI is installed (`powerscriptc --version`)
- Check output directory permissions
- Review `powerscript.toml` compiler settings

**4. Debugging Not Working**
- Ensure Python extension is installed
- Verify launch configuration paths
- Check that build task compiles successfully

### Diagnostic Information

**View LSP Server Logs**
1. Open Output panel (Ctrl+Shift+U)
2. Select "PowerScript Language Server" from dropdown
3. Review connection and error messages

**Extension Debug Mode**
```json
{
    "powerscript.trace.server": "verbose",
    "powerscript.debug.enabled": true
}
```

### Performance Tips

1. **Exclude Large Directories**
   ```json
   {
       "files.exclude": {
           "**/node_modules": true,
           "**/build": true,
           "**/.git": true
       }
   }
   ```

2. **Limit File Watching**
   ```json
   {
       "files.watcherExclude": {
           "**/build/**": true,
           "**/dist/**": true
       }
   }
   ```

3. **Configure LSP Resource Limits**
   ```json
   {
       "powerscript.lsp.maxNumberOfProblems": 50,
       "powerscript.lsp.maxFileSizeInMB": 10
   }
   ```

## Getting Help

- **Documentation**: Check the language specification and tutorials
- **Issues**: Report bugs on GitHub repository
- **Community**: Join discussions on project forums
- **Examples**: Explore example projects in the repository

## Contributing to the Extension

Want to improve the VS Code extension?

1. **Fork the Repository**
2. **Setup Development Environment**
   ```bash
   cd powerscript/vscode-extension/
   npm install
   code .
   ```
3. **Make Changes**
4. **Test in Extension Development Host** (F5)
5. **Submit Pull Request**

The PowerScript VS Code extension makes developing PowerScript applications a smooth, productive experience with full IDE support!