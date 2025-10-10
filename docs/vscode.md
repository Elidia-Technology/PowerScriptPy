# PowerScript VS Code Extension

**Complete IDE integration guide for PowerScript development in Visual Studio Code**

> **Version**: 2.0 | **Status**: Production Ready | **Updated**: October 2025

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Features](#features)
4. [Configuration](#configuration)
5. [Language Server](#language-server)
6. [Debugging](#debugging)
7. [Code Completion](#code-completion)
8. [Syntax Highlighting](#syntax-highlighting)
9. [Error Diagnostics](#error-diagnostics)
10. [Code Actions](#code-actions)
11. [Snippets](#snippets)
12. [Tasks and Build](#tasks-and-build)
13. [Troubleshooting](#troubleshooting)

## Overview

The PowerScript VS Code extension provides comprehensive IDE support for PowerScript development, including syntax highlighting, IntelliSense, debugging, error diagnostics, and integrated build tools.

### Key Features

- **🎨 Syntax Highlighting**: Full PowerScript syntax support with modern theme compatibility
- **🧠 IntelliSense**: Auto-completion, parameter hints, and hover information
- **🐛 Debugging**: Full debugging support with breakpoints and variable inspection
- **⚠️ Error Diagnostics**: Real-time error detection and type checking
- **🔧 Code Actions**: Quick fixes, refactoring, and code improvements
- **📝 Snippets**: Code templates for common PowerScript patterns
- **🏗️ Build Integration**: Integrated compilation and task running
- **🔍 Symbol Navigation**: Go to definition, find references, symbol outline

## Installation

### Method 1: VS Code Marketplace (Recommended)

1. Open VS Code
2. Go to Extensions view (`Ctrl+Shift+X` / `Cmd+Shift+X`)
3. Search for "PowerScript"
4. Click "Install" on the PowerScript extension by SaleemLww

### Method 2: Manual Installation

```bash
# Clone the PowerScript repository
git clone https://github.com/SaleemLww/Python-PowerScript.git
cd Python-PowerScript

# Install the extension
code --install-extension powerscript/vscode-extension/powerscript-*.vsix
```

### Method 3: Development Installation

```bash
# For extension development
cd Python-PowerScript/powerscript/vscode-extension
npm install
npm run compile

# Link for development
npm run watch
```

### Verify Installation

1. Open a `.ps` file in VS Code
2. Check that syntax highlighting is active
3. Verify the PowerScript language mode in the status bar
4. Test IntelliSense with `Ctrl+Space`

## Features

### 🎨 Syntax Highlighting

Complete syntax highlighting for all PowerScript language constructs:

#### Basic Language Elements
```powerscript
// Keywords and operators
function calculateArea(radius: number): number {
    const PI = 3.14159
    return PI * radius * radius
}

// Modern features with proper highlighting
const users = data.map(user => ({ 
    name: user.name.toUpperCase(),
    email: user.email 
}))

// F-strings and template literals
const greeting = f"Hello, {name}!"
const template = `Welcome ${user.name}
Your role: ${user.role}`
```

#### Advanced Constructs
```powerscript
// Classes with access modifiers
class DataProcessor {
    private data: Array<number>
    protected config: ProcessorConfig
    public readonly name: string
    
    constructor(name: string, data: Array<number>) {
        this.name = name
        this.data = data
    }
}

// Switch statements with multiple cases
switch (status) {
    case "pending", "processing":
        return "In Progress"
    case "completed", "success":
        return "Done"
    default:
        return "Unknown"
}

// Import/export statements
import { DataProcessor, Config } from "./data-utils"
export const VERSION = "2.0.0"
```

### 🧠 IntelliSense

Intelligent code completion and suggestions:

#### Auto-completion Features

1. **Variable and Function Names**
   - Context-aware suggestions
   - Type-based filtering
   - Import suggestions

2. **Object Properties and Methods**
   ```powerscript
   const user = { name: "John", age: 30 }
   user.  // Shows: name, age + Object methods
   
   const numbers = [1, 2, 3]
   numbers.  // Shows: Array methods (map, filter, etc.)
   ```

3. **Type Annotations**
   ```powerscript
   function process(data:  // Suggests: string, number, boolean, Array, etc.
   ```

4. **Import Completions**
   ```powerscript
   import {  // Suggests available exports from modules
   ```

#### Parameter Hints

```powerscript
// Function signature hints while typing
calculateDistance(
   // Shows: calculateDistance(x1: number, y1: number, x2: number, y2: number): number
```

#### Hover Information

Hover over any symbol to see:
- Type information
- Documentation comments
- Source location
- Usage examples

### 🐛 Debugging

Full debugging support with Python backend integration:

#### Debug Configuration

Create `.vscode/launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "PowerScript: Debug Current File",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/build/${fileBasenameNoExtension}.py",
            "console": "integratedTerminal",
            "preLaunchTask": "powerscript: compile current file",
            "cwd": "${workspaceFolder}"
        },
        {
            "name": "PowerScript: Debug Main",
            "type": "python", 
            "request": "launch",
            "program": "${workspaceFolder}/build/main.py",
            "console": "integratedTerminal",
            "preLaunchTask": "powerscript: build",
            "cwd": "${workspaceFolder}",
            "args": []
        },
        {
            "name": "PowerScript: Debug Tests",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "args": ["build/tests/"],
            "console": "integratedTerminal",
            "preLaunchTask": "powerscript: build tests"
        }
    ]
}
```

#### Debug Features

1. **Breakpoints**
   - Set breakpoints in `.ps` files
   - Conditional breakpoints
   - Logpoints for non-intrusive debugging

2. **Variable Inspection**
   - Local variables view
   - Watch expressions
   - Call stack navigation

3. **Step Controls**
   - Step over, into, out
   - Continue, pause, restart
   - Exception breakpoints

### ⚠️ Error Diagnostics

Real-time error detection and reporting:

#### Syntax Errors
```powerscript
// Missing semicolons, brackets, etc. are highlighted immediately
function test( {  // Error: Missing parameter list
    return 42
// Error: Missing closing brace
```

#### Type Errors
```powerscript
function greet(name: string): string {
    return name.toUpperCase()
}

greet(42)  // Error: Argument of type 'number' is not assignable to parameter of type 'string'
```

#### Import Errors
```powerscript
import { nonExistentFunction } from "./utils"  // Error: 'nonExistentFunction' is not exported
```

#### Configuration

Configure diagnostics in VS Code settings:

```json
{
    "powerscript.diagnostics.enable": true,
    "powerscript.diagnostics.strictMode": true,
    "powerscript.diagnostics.checkOnSave": true,
    "powerscript.diagnostics.checkOnType": true,
    "powerscript.diagnostics.maxProblems": 100
}
```

### 🔧 Code Actions

Quick fixes and refactoring options:

#### Available Actions

1. **Auto-fix imports**
   ```powerscript
   console.log("Hello")  // Quick fix: Add missing import
   // Becomes: import console from "console"
   ```

2. **Add missing type annotations**
   ```powerscript
   function calculate(x, y) {  // Quick fix: Add type annotations
   // Becomes: function calculate(x: number, y: number): number {
   ```

3. **Convert to arrow function**
   ```powerscript
   function double(x) { return x * 2 }
   // Quick fix: Convert to arrow function
   // Becomes: const double = (x) => x * 2
   ```

4. **Extract function**
   ```powerscript
   // Select code block, right-click → Extract Function
   const result = data.filter(x => x > 0).map(x => x * 2)
   // Becomes: const result = processPositiveNumbers(data)
   ```

5. **Organize imports**
   - Remove unused imports
   - Sort imports alphabetically
   - Group imports by type

### 📝 Snippets

Pre-built code templates for common patterns:

#### Function Snippets

| Trigger | Description | Generated Code |
|---------|-------------|---------------|
| `func` | Basic function | `function name(): type {\n\t$0\n}` |
| `afunc` | Arrow function | `const name = () => {\n\t$0\n}` |
| `async` | Async function | `async function name(): Promise<type> {\n\t$0\n}` |

#### Class Snippets

| Trigger | Description | Generated Code |
|---------|-------------|---------------|
| `class` | Basic class | `class Name {\n\tconstructor() {\n\t\t$0\n\t}\n}` |
| `interface` | Interface | `interface Name {\n\t$0\n}` |
| `enum` | Enumeration | `enum Name {\n\t$0\n}` |

#### Control Flow Snippets

| Trigger | Description | Generated Code |
|---------|-------------|---------------|
| `if` | If statement | `if ($1) {\n\t$0\n}` |
| `switch` | Switch statement | `switch ($1) {\n\tcase $2:\n\t\t$0\n\t\tbreak\n}` |
| `for` | For loop | `for (let $1 = 0; $1 < $2; $1++) {\n\t$0\n}` |
| `while` | While loop | `while ($1) {\n\t$0\n}` |

#### Modern Features Snippets

| Trigger | Description | Generated Code |
|---------|-------------|---------------|
| `fstring` | F-string | `f"$1{$2}$3"` |
| `template` | Template literal | `` `$1\${$2}$3` `` |
| `arrow` | Arrow function | `$1 => $2` |
| `import` | Import statement | `import { $1 } from "$2"` |
| `export` | Export statement | `export const $1 = $2` |

#### Custom Snippets

Create custom snippets in User Snippets (`Ctrl+Shift+P` → "Configure User Snippets"):

```json
{
    "PowerScript ML Model": {
        "prefix": "mlmodel",
        "body": [
            "class ${1:ModelName} {",
            "\tprivate model: any",
            "\tprivate trained: boolean = false",
            "",
            "\tconstructor(config: ${2:ModelConfig}) {",
            "\t\tthis.model = this.initializeModel(config)",
            "\t}",
            "",
            "\tpublic async train(data: TrainingData): Promise<void> {",
            "\t\t${3:// Training logic}",
            "\t\tthis.trained = true",
            "\t}",
            "",
            "\tpublic predict(input: ${4:InputType}): ${5:OutputType} {",
            "\t\tif (!this.trained) {",
            "\t\t\tthrow new Error('Model not trained')",
            "\t\t}",
            "\t\t${6:// Prediction logic}",
            "\t}",
            "",
            "\tprivate initializeModel(config: ${2:ModelConfig}): any {",
            "\t\t${7:// Initialization logic}",
            "\t}",
            "}"
        ],
        "description": "Create a machine learning model class"
    }
}
```

## Configuration

### Extension Settings

Configure the extension in VS Code settings (`Ctrl+,`):

```json
{
    // Language Server
    "powerscript.languageServer.enable": true,
    "powerscript.languageServer.maxMemory": 512,
    "powerscript.languageServer.debug": false,
    
    // Diagnostics
    "powerscript.diagnostics.enable": true,
    "powerscript.diagnostics.strictMode": true,
    "powerscript.diagnostics.checkOnSave": true,
    "powerscript.diagnostics.checkOnType": false,
    "powerscript.diagnostics.maxProblems": 100,
    
    // Formatting
    "powerscript.formatting.enable": true,
    "powerscript.formatting.insertSpaces": true,
    "powerscript.formatting.tabSize": 4,
    "powerscript.formatting.trimTrailingWhitespace": true,
    
    // IntelliSense
    "powerscript.intellisense.enable": true,
    "powerscript.intellisense.autoImports": true,
    "powerscript.intellisense.suggestSnippets": true,
    "powerscript.intellisense.maxSuggestions": 50,
    
    // Build Integration
    "powerscript.build.autoCompile": true,
    "powerscript.build.watchMode": true,
    "powerscript.build.outputDirectory": "build",
    "powerscript.build.strictMode": true,
    
    // Debug
    "powerscript.debug.enable": true,
    "powerscript.debug.sourceMaps": true,
    "powerscript.debug.autoLaunch": false
}
```

### Workspace Settings

Project-specific settings in `.vscode/settings.json`:

```json
{
    "files.associations": {
        "*.ps": "powerscript"
    },
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true,
        "source.fixAll.powerscript": true
    },
    "powerscript.build.outputDirectory": "./build",
    "powerscript.diagnostics.strictMode": true,
    "search.exclude": {
        "build/": true,
        "node_modules/": true
    }
}
```

## Language Server

The PowerScript Language Server provides advanced IDE features:

### Features Provided

1. **Hover Information**: Type information and documentation
2. **Go to Definition**: Navigate to symbol definitions
3. **Find References**: Find all usages of a symbol
4. **Rename Symbol**: Rename symbols across files
5. **Document Symbols**: Outline view of file structure
6. **Workspace Symbols**: Search symbols across project
7. **Code Completion**: Intelligent auto-completion
8. **Signature Help**: Parameter information while typing
9. **Diagnostics**: Error and warning reporting

### Language Server Configuration

```json
{
    "powerscript.languageServer.enable": true,
    "powerscript.languageServer.path": "auto",  // or path to custom LSP
    "powerscript.languageServer.arguments": [],
    "powerscript.languageServer.environment": {},
    "powerscript.languageServer.maxMemory": 512,
    "powerscript.languageServer.debug": false,
    "powerscript.languageServer.trace": "off"  // "off", "messages", "verbose"
}
```

### Performance Tuning

For large projects:

```json
{
    "powerscript.languageServer.maxMemory": 1024,
    "powerscript.diagnostics.checkOnType": false,
    "powerscript.intellisense.maxSuggestions": 25,
    "files.watcherExclude": {
        "**/build/**": true,
        "**/node_modules/**": true
    }
}
```

## Tasks and Build

Integrate PowerScript compilation with VS Code tasks:

### Basic Tasks Configuration

Create `.vscode/tasks.json`:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "PowerScript: Build",
            "type": "shell",
            "command": "powerscriptc",
            "args": ["src/", "-o", "build/", "--strict"],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "presentation": {
                "reveal": "always",
                "panel": "new"
            },
            "problemMatcher": "$powerscript"
        },
        {
            "label": "PowerScript: Build and Run",
            "type": "shell",
            "command": "powerscriptc",
            "args": ["src/", "-o", "build/", "--strict"],
            "group": "build",
            "presentation": {
                "reveal": "always"
            },
            "problemMatcher": "$powerscript",
            "dependsOrder": "sequence",
            "dependsOn": "PowerScript: Run"
        },
        {
            "label": "PowerScript: Run",
            "type": "shell",
            "command": "python",
            "args": ["build/main.py"],
            "group": "test",
            "presentation": {
                "reveal": "always"
            }
        },
        {
            "label": "PowerScript: Watch",
            "type": "shell",
            "command": "powerscriptc",
            "args": ["src/", "-o", "build/", "--watch", "--verbose"],
            "group": "build",
            "isBackground": true,
            "presentation": {
                "reveal": "always",
                "panel": "new"
            },
            "problemMatcher": "$powerscript"
        },
        {
            "label": "PowerScript: Type Check",
            "type": "shell",
            "command": "psc",
            "args": ["src/", "--strict"],
            "group": "test",
            "presentation": {
                "reveal": "always"
            },
            "problemMatcher": "$powerscript"
        },
        {
            "label": "PowerScript: Clean",
            "type": "shell",
            "command": "rm",
            "args": ["-rf", "build/"],
            "group": "build"
        }
    ]
}
```

### Problem Matchers

The extension provides problem matchers for error parsing:

```json
{
    "problemMatchers": [
        {
            "name": "powerscript",
            "owner": "powerscript",
            "fileLocation": "relative",
            "pattern": {
                "regexp": "^(.+):(\\d+):(\\d+):\\s+(error|warning|info):\\s+(.+)$",
                "file": 1,
                "line": 2,
                "column": 3,
                "severity": 4,
                "message": 5
            }
        }
    ]
}
```

### Keyboard Shortcuts

Add custom keybindings in `.vscode/keybindings.json`:

```json
[
    {
        "key": "ctrl+shift+b",
        "command": "workbench.action.tasks.runTask",
        "args": "PowerScript: Build"
    },
    {
        "key": "f5",
        "command": "workbench.action.tasks.runTask", 
        "args": "PowerScript: Build and Run"
    },
    {
        "key": "ctrl+shift+t",
        "command": "workbench.action.tasks.runTask",
        "args": "PowerScript: Type Check"
    },
    {
        "key": "ctrl+shift+w",
        "command": "workbench.action.tasks.runTask",
        "args": "PowerScript: Watch"
    }
]
```

## Troubleshooting

### Common Issues

#### Extension Not Activating

**Problem**: PowerScript files not recognized

**Solutions**:
1. Check file association:
   ```json
   {
       "files.associations": {
           "*.ps": "powerscript"
       }
   }
   ```

2. Reload VS Code: `Ctrl+Shift+P` → "Developer: Reload Window"

3. Check extension installation: Extensions view → Search "PowerScript"

#### IntelliSense Not Working

**Problem**: No auto-completion or hover information

**Solutions**:
1. Check language server status:
   ```json
   {
       "powerscript.languageServer.enable": true,
       "powerscript.languageServer.debug": true
   }
   ```

2. Restart language server: `Ctrl+Shift+P` → "PowerScript: Restart Language Server"

3. Check PowerScript installation:
   ```bash
   powerscriptc --version
   psc --version
   ```

#### Syntax Highlighting Issues

**Problem**: Code not properly highlighted

**Solutions**:
1. Set language mode manually: Click language mode in status bar → Select "PowerScript"

2. Check theme compatibility: Some themes may not support all PowerScript tokens

3. Update extension: Extensions view → PowerScript → Update

#### Build Tasks Failing

**Problem**: Tasks not running or failing

**Solutions**:
1. Check task configuration in `.vscode/tasks.json`

2. Verify PowerScript CLI tools are in PATH:
   ```bash
   which powerscriptc
   which psc
   ```

3. Check workspace settings:
   ```json
   {
       "powerscript.build.outputDirectory": "build"
   }
   ```

#### Debug Configuration Issues

**Problem**: Debugging not working

**Solutions**:
1. Check launch configuration in `.vscode/launch.json`

2. Ensure Python extension is installed

3. Verify compiled files exist in build directory

4. Check source maps are enabled:
   ```json
   {
       "powerscript.debug.sourceMaps": true
   }
   ```

### Performance Issues

#### Slow IntelliSense

**Solutions**:
1. Reduce suggestion limits:
   ```json
   {
       "powerscript.intellisense.maxSuggestions": 25
   }
   ```

2. Disable type checking on type:
   ```json
   {
       "powerscript.diagnostics.checkOnType": false
   }
   ```

3. Exclude build directories:
   ```json
   {
       "files.watcherExclude": {
           "**/build/**": true
       }
   }
   ```

#### High Memory Usage

**Solutions**:
1. Limit language server memory:
   ```json
   {
       "powerscript.languageServer.maxMemory": 256
   }
   ```

2. Restart language server periodically:
   `Ctrl+Shift+P` → "PowerScript: Restart Language Server"

### Extension Logs

Access extension logs for debugging:

1. **Output Panel**: View → Output → Select "PowerScript"
2. **Developer Tools**: Help → Toggle Developer Tools → Console
3. **Language Server Logs**: Enable debug mode and check output

```json
{
    "powerscript.languageServer.debug": true,
    "powerscript.languageServer.trace": "verbose"
}
```

## Advanced Features

### Multi-root Workspace Support

PowerScript extension supports multi-root workspaces:

```json
// workspace.code-workspace
{
    "folders": [
        {
            "name": "PowerScript App",
            "path": "./app"
        },
        {
            "name": "PowerScript Shared",
            "path": "./shared"
        }
    ],
    "settings": {
        "powerscript.build.outputDirectory": "build",
        "powerscript.diagnostics.strictMode": true
    }
}
```

### Remote Development

Use PowerScript with VS Code remote development:

1. **Remote - SSH**: Develop on remote servers
2. **Dev Containers**: Containerized development environment
3. **WSL**: Windows Subsystem for Linux support

### Integration with Other Extensions

#### Recommended Extensions

- **Python**: For debugging compiled Python code
- **GitLens**: Enhanced Git integration
- **Bracket Pair Colorizer**: Better bracket visualization
- **Error Lens**: Inline error highlighting
- **TODO Highlight**: TODO comment highlighting

#### Extension API

For extension developers, PowerScript provides APIs:

```typescript
// Extension API
import * as vscode from 'vscode'
import { PowerScriptExtension } from 'powerscript-vscode'

export function activate(context: vscode.ExtensionContext) {
    const powerscript = vscode.extensions.getExtension('powerscript.powerscript')
    if (powerscript) {
        const api = powerscript.exports
        
        // Access PowerScript compiler
        api.compile(source, options)
        
        // Access type checker
        api.typeCheck(source, options)
        
        // Access language server
        api.languageServer.sendRequest(method, params)
    }
}
```

---

This completes the PowerScript VS Code Extension documentation. For more information, see:

- [Language Reference](language-reference.md)
- [API Documentation](api.md)
- [CLI Guide](cli.md)
- [Tutorial](../powerscript/docs/tutorial.md)

**PowerScript: Complete IDE integration for modern development! 🐍✨**