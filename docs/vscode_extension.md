# VS Code Extension Guide

The PowerScript VS Code extension provides a complete IDE experience with syntax highlighting, IntelliSense, error diagnostics, and more!

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Code Snippets](#code-snippets)
- [Commands](#commands)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)

## Features

### ✨ Syntax Highlighting
- Full syntax highlighting for `.ps` files
- Color-coded keywords, strings, comments, types
- Support for modern PowerScript features
- Semantic highlighting for better readability

### 🧠 IntelliSense
- Auto-completion for keywords and types
- Function and method suggestions
- Variable name completion
- Import statement assistance
- Parameter hints

### 🔍 Error Diagnostics
- Real-time syntax error detection
- Type checking warnings
- Missing semicolon suggestions
- Unknown type flags
- Inline error messages

### 📝 Code Snippets
13 built-in code snippets for common patterns:
- `function` - Function declaration
- `class` - Class definition
- `interface` - Interface declaration
- `arrow` - Arrow function
- `async` - Async function
- `if` - If statement
- `for` - For loop
- `while` - While loop
- `try` - Try-catch block
- `switch` - Switch statement
- `enum` - Enum declaration
- `import` - Import statement
- `export` - Export statement

### 🎯 Commands
- **Compile File** - Compile current `.ps` file to Python
- **Run File** - Compile and run current file
- **Create Project** - Scaffold new PowerScript project

### ⌨️ Keyboard Shortcuts
- `Ctrl+Shift+B` / `Cmd+Shift+B` - Compile current file
- `Ctrl+Shift+R` / `Cmd+Shift+R` - Run current file

### 📚 Additional Features
- Hover information for types and functions
- Definition and reference finding
- Document formatting
- Code folding
- Bracket matching
- Comment toggling

## Installation

### Method 1: Install from GitHub Release

1. **Visit the GitHub Repository**
   ```
   https://github.com/SaleemLww/Python-PowerScript
   ```

2. **Download the Extension**
   - Navigate to the `vscode-extension/` folder
   - Download the latest `.vsix` file
   - Or clone the entire repository

3. **Install in VS Code**
   ```bash
   code --install-extension powerscript-1.0.0.vsix
   ```

### Method 2: Build from Source

```bash
# Clone the repository
git clone https://github.com/SaleemLww/Python-PowerScript.git
cd Python-PowerScript/vscode-extension

# Install dependencies
npm install

# Compile TypeScript
npm run compile

# Package the extension
npx vsce package

# Install the generated .vsix file
code --install-extension powerscript-1.0.0.vsix
```

### Method 3: Install via VS Code UI

1. Open VS Code
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)
3. Type: "Extensions: Install from VSIX..."
4. Select the downloaded `.vsix` file
5. Restart VS Code

### Verify Installation

1. Open VS Code
2. Go to Extensions (`Ctrl+Shift+X`)
3. Search for "PowerScript"
4. You should see "PowerScript Language Support" installed

## Getting Started

### Open a PowerScript File

1. Create a new file with `.ps` extension
2. VS Code automatically activates PowerScript mode
3. Start coding with full IDE support!

### First PowerScript File

Create `hello.ps`:

```powerscript
// hello.ps
console.log("Hello, PowerScript!");

function greet(name: string): string {
    return f"Hello, {name}!";
}

let message = greet("World");
console.log(message);
```

### Using the Extension

1. **Syntax Highlighting** - Automatically applied
2. **IntelliSense** - Type and see suggestions
3. **Error Detection** - Errors appear as red underlines
4. **Compile** - Right-click → "Compile PowerScript File"
5. **Run** - Right-click → "Run PowerScript File"

## Code Snippets

Type the prefix and press `Tab` to expand:

### Function Snippet
```powerscript
// Type: function + Tab
function functionName(param: type): returnType {
    // function body
    return value;
}
```

### Class Snippet
```powerscript
// Type: class + Tab
class ClassName {
    private property: type;
    
    constructor(param: type) {
        this.property = param;
    }
    
    public method(): returnType {
        // method body
    }
}
```

### Arrow Function Snippet
```powerscript
// Type: arrow + Tab
const functionName = (param: type): returnType => {
    return value;
};

// Or single expression
const square = (x: number): number => x * x;
```

### Async Function Snippet
```powerscript
// Type: async + Tab
async function asyncFunction(): Promise<type> {
    const result = await someAsyncOperation();
    return result;
}
```

### If Statement Snippet
```powerscript
// Type: if + Tab
if (condition) {
    // code
} else {
    // code
}
```

### For Loop Snippet
```powerscript
// Type: for + Tab
let i = 0;
for (i = 0; i < length; i += 1) {
    // loop body
}
```

### Try-Catch Snippet
```powerscript
// Type: try + Tab
try {
    // risky code
} catch (error) {
    console.log(error);
}
```

### Interface Snippet
```powerscript
// Type: interface + Tab
interface InterfaceName {
    property: type;
    method(param: type): returnType;
}
```

### Enum Snippet
```powerscript
// Type: enum + Tab
enum EnumName {
    VALUE1 = "value1",
    VALUE2 = "value2"
}
```

### Switch Statement Snippet
```powerscript
// Type: switch + Tab
switch (expression) {
    case value1:
        // code
        break;
    case value2:
        // code
        break;
    default:
        // code
}
```

## Commands

Access via Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`):

### PowerScript: Compile File
- Compiles current `.ps` file to Python
- Shortcut: `Ctrl+Shift+B` / `Cmd+Shift+B`
- Output: `.py` file in same directory

### PowerScript: Run File
- Compiles and runs current file
- Shortcut: `Ctrl+Shift+R` / `Cmd+Shift+R`
- Output: Terminal shows execution results

### PowerScript: Create Project
- Scaffolds new PowerScript project
- Prompts for project name and template
- Creates complete project structure

### Using Commands

**Via Command Palette:**
1. Press `Ctrl+Shift+P` / `Cmd+Shift+P`
2. Type "PowerScript"
3. Select desired command

**Via Right-Click Menu:**
1. Right-click in `.ps` file
2. Select "Compile PowerScript File" or "Run PowerScript File"

**Via Keyboard:**
- `Ctrl+Shift+B` - Compile
- `Ctrl+Shift+R` - Run

## Keyboard Shortcuts

| Action | Windows/Linux | macOS |
|--------|---------------|-------|
| Compile File | `Ctrl+Shift+B` | `Cmd+Shift+B` |
| Run File | `Ctrl+Shift+R` | `Cmd+Shift+R` |
| Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` |
| Quick Open | `Ctrl+P` | `Cmd+P` |
| Toggle Sidebar | `Ctrl+B` | `Cmd+B` |
| Toggle Terminal | `Ctrl+\`` | `Cmd+\`` |

### Customize Shortcuts

1. Open Keyboard Shortcuts (`Ctrl+K Ctrl+S`)
2. Search for "PowerScript"
3. Click on command and set new binding

## Configuration

### VS Code Settings

Add to `.vscode/settings.json`:

```json
{
    "powerscript.enableLSP": true,
    "powerscript.enableDiagnostics": true,
    "powerscript.compilerPath": "tps-compile",
    "powerscript.pythonPath": "python3"
}
```

### File Associations

Automatically associates `.ps` files with PowerScript:

```json
{
    "files.associations": {
        "*.ps": "powerscript"
    }
}
```

### Editor Settings

Recommended settings for PowerScript:

```json
{
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "editor.formatOnSave": true,
    "editor.suggestSelection": "first",
    "editor.quickSuggestions": {
        "other": true,
        "comments": false,
        "strings": false
    }
}
```

## Troubleshooting

### Extension Not Showing

**Problem:** Extension doesn't appear in Extensions list

**Solution:**
1. Restart VS Code completely
2. Check installation: `code --list-extensions`
3. Reinstall: `code --install-extension powerscript-1.0.0.vsix`

### Syntax Highlighting Not Working

**Problem:** `.ps` files not highlighted

**Solution:**
1. Click language indicator (bottom right)
2. Select "PowerScript" from list
3. Or add to settings:
   ```json
   {
       "files.associations": {
           "*.ps": "powerscript"
       }
   }
   ```

### Commands Not Working

**Problem:** Compile/Run commands fail

**Solution:**
1. Ensure TPS is installed: `pip install tps`
2. Verify PATH includes Python scripts
3. Test manually: `tps-compile --version`
4. Check settings for correct paths

### Snippets Not Expanding

**Problem:** Typing prefix doesn't show snippet

**Solution:**
1. Type prefix exactly (e.g., `function`)
2. Press `Tab` (not Enter)
3. Ensure file is recognized as PowerScript
4. Check settings: `editor.snippetSuggestions`

### IntelliSense Not Working

**Problem:** No auto-completion suggestions

**Solution:**
1. Check LSP is enabled in settings
2. Restart VS Code
3. Ensure file is saved with `.ps` extension
4. Check output panel for errors

### Error Diagnostics Not Showing

**Problem:** Syntax errors not highlighted

**Solution:**
1. Enable diagnostics in settings
2. Check file is saved
3. Restart Language Server: Reload Window
4. Check PowerScript installation

## Advanced Usage

### Multi-Root Workspaces

PowerScript extension supports multi-root workspaces:

```json
// workspace.code-workspace
{
    "folders": [
        { "path": "project1" },
        { "path": "project2" }
    ],
    "settings": {
        "powerscript.enableLSP": true
    }
}
```

### Custom Build Tasks

Create `.vscode/tasks.json`:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Compile PowerScript",
            "type": "shell",
            "command": "tps-compile",
            "args": ["${file}"],
            "group": {
                "kind": "build",
                "isDefault": true
            }
        },
        {
            "label": "Run PowerScript",
            "type": "shell",
            "command": "tps-run",
            "args": ["${file}"]
        }
    ]
}
```

### Debugging Support

While native debugging isn't yet supported, you can debug the transpiled Python:

1. Compile to Python: `tps-compile file.ps -o file.py`
2. Add Python breakpoints
3. Use VS Code Python debugger on `.py` file

## Tips & Tricks

### Productivity Tips

1. **Use Snippets** - Type prefix + Tab for quick templates
2. **Keyboard Shortcuts** - Learn Ctrl+Shift+B and Ctrl+Shift+R
3. **IntelliSense** - Press Ctrl+Space for suggestions
4. **Hover Info** - Hover over types for documentation
5. **Quick Open** - Ctrl+P to quickly open files

### Best Practices

1. **Save Frequently** - Diagnostics run on save
2. **Organize Imports** - Keep imports at top
3. **Use Type Annotations** - Get better IntelliSense
4. **Format Code** - Use consistent spacing
5. **Check Terminal** - Watch for compilation errors

### Extension Updates

To update the extension:

1. Download latest `.vsix` from GitHub
2. Uninstall old version
3. Install new version
4. Restart VS Code

## Resources

- **Extension Documentation**: See `vscode-extension/README.md` in repo
- **Quick Reference**: See `vscode-extension/QUICK_REFERENCE.md`
- **GitHub**: [Python-PowerScript](https://github.com/SaleemLww/Python-PowerScript)
- **Issues**: [Report problems](https://github.com/SaleemLww/Python-PowerScript/issues)

## Next Steps

1. ✅ Install the VS Code extension
2. ✅ Try the code snippets
3. ✅ Use compile and run commands
4. ✅ Start building with PowerScript!

---

**Happy coding with PowerScript in VS Code!** 🚀
