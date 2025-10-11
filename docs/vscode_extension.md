# 🎨 VS Code Extension Guide# VS Code Extension Guide



Complete guide to the PowerScript VS Code extension.The PowerScript VS Code extension provides a complete IDE experience with syntax highlighting, IntelliSense, error diagnostics, and more!



## 📦 Installation## Table of Contents

- [Features](#features)

### Method 1: Install from VSIX (Recommended)- [Installation](#installation)

- [Getting Started](#getting-started)

1. **Locate Extension File**- [Code Snippets](#code-snippets)

   ```bash- [Commands](#commands)

   # In PowerScript repository- [Keyboard Shortcuts](#keyboard-shortcuts)

   cd vscode-extension- [Configuration](#configuration)

   # File: powerscript-1.0.0.vsix (550.28 KB)- [Troubleshooting](#troubleshooting)

   ```

## Features

2. **Install in VS Code**

   - Open VS Code### ✨ Syntax Highlighting

   - Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)- Full syntax highlighting for `.ps` files

   - Type: `Extensions: Install from VSIX`- Color-coded keywords, strings, comments, types

   - Navigate to `powerscript-1.0.0.vsix`- Support for modern PowerScript features

   - Click "Install"- Semantic highlighting for better readability



3. **Verify Installation**### 🧠 IntelliSense

   - Create file: `test.ps`- Auto-completion for keywords and types

   - Should see PowerScript syntax highlighting- Function and method suggestions

   - Check Extensions panel for "PowerScript"- Variable name completion

- Import statement assistance

### Method 2: Build from Source- Parameter hints



```bash### 🔍 Error Diagnostics

cd vscode-extension- Real-time syntax error detection

- Type checking warnings

# Install Node.js dependencies- Missing semicolon suggestions

npm install- Unknown type flags

- Inline error messages

# Compile TypeScript

npm run compile### 📝 Code Snippets

13 built-in code snippets for common patterns:

# Package extension- `function` - Function declaration

npm install -g vsce- `class` - Class definition

vsce package- `interface` - Interface declaration

- `arrow` - Arrow function

# Install the generated .vsix- `async` - Async function

code --install-extension powerscript-1.0.0.vsix- `if` - If statement

```- `for` - For loop

- `while` - While loop

## ✨ Features- `try` - Try-catch block

- `switch` - Switch statement

### 1. Syntax Highlighting ✅- `enum` - Enum declaration

- `import` - Import statement

Beautiful, semantic highlighting for PowerScript code:- `export` - Export statement



**Keywords:**### 🎯 Commands

- Control flow: `if`, `else`, `for`, `while`, `switch`, `case`- **Compile File** - Compile current `.ps` file to Python

- Types: `string`, `number`, `boolean`, `void`, `any`, `null`, `undefined`- **Run File** - Compile and run current file

- Modifiers: `public`, `private`, `protected`, `static`, `async`, `const`, `let`- **Create Project** - Scaffold new PowerScript project

- Classes: `class`, `interface`, `abstract`, `extends`, `implements`

- Functions: `function`, `return`, `constructor`### ⌨️ Keyboard Shortcuts

- Modules: `import`, `export`, `from`, `as`- `Ctrl+Shift+B` / `Cmd+Shift+B` - Compile current file

- `Ctrl+Shift+R` / `Cmd+Shift+R` - Run current file

**Operators & Symbols:**

- Arithmetic: `+`, `-`, `*`, `/`, `%`### 📚 Additional Features

- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`- Hover information for types and functions

- Logical: `&&`, `||`, `!`- Definition and reference finding

- Assignment: `=`, `+=`, `-=`, `*=`, `/=`- Document formatting

- Code folding

**Literals:**- Bracket matching

- Strings: `"double quotes"`, `'single quotes'`- Comment toggling

- Numbers: `42`, `3.14`, `0xFF`

- Booleans: `true`, `false`## Installation

- Null: `null`, `undefined`

### Method 1: Install from GitHub Release

### 2. Code Snippets ✅

1. **Visit the GitHub Repository**

13 intelligent snippets for common patterns:   ```

   https://github.com/SaleemLww/Python-PowerScript

#### Basic Snippets   ```



**`func`** - Function Declaration2. **Download the Extension**

```powerscript   - Navigate to the `vscode-extension/` folder

function functionName(param: type): returnType {   - Download the latest `.vsix` file

    // function body   - Or clone the entire repository

}

```3. **Install in VS Code**

   ```bash

**`arrow`** - Arrow Function   code --install-extension powerscript-1.0.0.vsix

```powerscript   ```

const name = (param: type): returnType => {

    // function body### Method 2: Build from Source

};

``````bash

# Clone the repository

**`class`** - Class with Constructorgit clone https://github.com/SaleemLww/Python-PowerScript.git

```powerscriptcd Python-PowerScript/vscode-extension

class ClassName {

    constructor(param: type) {# Install dependencies

        // constructor bodynpm install

    }

    # Compile the extension source

    methodName(): returnType {npm run compile

        // method body

    }# Package the extension

}npx vsce package

```

# Install the generated .vsix file

**`interface`** - Interface Declarationcode --install-extension powerscript-1.0.0.vsix

```powerscript```

interface InterfaceName {

    property: type;### Method 3: Install via VS Code UI

    method(): returnType;

}1. Open VS Code

```2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)

3. Type: "Extensions: Install from VSIX..."

#### Control Flow Snippets4. Select the downloaded `.vsix` file

5. Restart VS Code

**`if`** - If Statement

```powerscript### Verify Installation

if (condition) {

    // true block1. Open VS Code

}2. Go to Extensions (`Ctrl+Shift+X`)

```3. Search for "PowerScript"

4. You should see "PowerScript Language Support" installed

**`ife`** - If-Else Statement

```powerscript## Getting Started

if (condition) {

    // true block### Open a PowerScript File

} else {

    // false block1. Create a new file with `.ps` extension

}2. VS Code automatically activates PowerScript mode

```3. Start coding with full IDE support!



**`for`** - For Loop### First PowerScript File

```powerscript

for (let i = 0; i < length; i++) {Create `hello.ps`:

    // loop body

}```powerscript

```// hello.ps

console.log("Hello, PowerScript!");

**`while`** - While Loop

```powerscriptfunction greet(name: string): string {

while (condition) {    return f"Hello, {name}!";

    // loop body}

}

```let message = greet("World");

console.log(message);

**`switch`** - Switch Statement```

```powerscript

switch (expression) {### Using the Extension

    case value1:

        // case 11. **Syntax Highlighting** - Automatically applied

        break;2. **IntelliSense** - Type and see suggestions

    case value2:3. **Error Detection** - Errors appear as red underlines

        // case 24. **Compile** - Right-click → "Compile PowerScript File"

        break;5. **Run** - Right-click → "Run PowerScript File"

    default:

        // default case## Code Snippets

}

```Type the prefix and press `Tab` to expand:



#### Module Snippets### Function Snippet

```powerscript

**`import`** - Import Statement// Type: function + Tab

```powerscriptfunction functionName(param: type): returnType {

import { symbol } from "module";    // function body

```    return value;

}

**`export`** - Export Statement```

```powerscript

export class ClassName {### Class Snippet

    // class body```powerscript

}// Type: class + Tab

```class ClassName {

    private property: type;

#### Advanced Snippets    

    constructor(param: type) {

**`async`** - Async Function        this.property = param;

```powerscript    }

async function functionName(): Promise<type> {    

    // async body    public method(): returnType {

}        // method body

```    }

}

**`enum`** - Enum Declaration```

```powerscript

enum EnumName {### Arrow Function Snippet

    Value1,```powerscript

    Value2,// Type: arrow + Tab

    Value3const functionName = (param: type): returnType => {

}    return value;

```};



### 3. File Recognition ✅// Or single expression

const square = (x: number): number => x * x;

**Supported Extensions:**```

- `.ps` - PowerScript source files

- `.pscript` - Alternative extension### Async Function Snippet

```powerscript

**Auto-Detection:**// Type: async + Tab

- VS Code automatically applies PowerScript syntax when opening `.ps` filesasync function asyncFunction(): Promise<type> {

- Language mode shows "PowerScript" in status bar    const result = await someAsyncOperation();

    return result;

### 4. Comment Support ✅}

```

**Single-line Comments:**

```powerscript### If Statement Snippet

// This is a single-line comment```powerscript

let x: number = 5; // inline comment// Type: if + Tab

```if (condition) {

    // code

**Multi-line Comments:**} else {

```powerscript    // code

/*}

 * This is a```

 * multi-line comment

 */### For Loop Snippet

function test(): void {```powerscript

    /* inline block comment */// Type: for + Tab

}let i = 0;

```for (i = 0; i < length; i += 1) {

    // loop body

**Block Comments:**}

- Toggle: `Cmd+/` (Mac) or `Ctrl+/` (Windows/Linux)```

- Block comment: `Cmd+Shift+A` (Mac) or `Ctrl+Shift+A` (Windows/Linux)

### Try-Catch Snippet

### 5. Bracket Matching ✅```powerscript

// Type: try + Tab

**Auto-completion:**try {

- Type `{` → Auto-completes `}`    // risky code

- Type `[` → Auto-completes `]`} catch (error) {

- Type `(` → Auto-completes `)`    console.log(error);

- Type `"` → Auto-completes `"`}

- Type `'` → Auto-completes `'````



**Auto-surrounding:**### Interface Snippet

- Select text and type `{` → Wraps in `{}````powerscript

- Select text and type `"` → Wraps in `""`// Type: interface + Tab

interface InterfaceName {

**Bracket colorization:**    property: type;

- Nested brackets shown in different colors    method(param: type): returnType;

- Easy to match opening/closing pairs}

```

## 🎯 Usage Tips

### Enum Snippet

### Snippet Workflow```powerscript

// Type: enum + Tab

1. **Type snippet prefix** (e.g., `func`)enum EnumName {

2. **Press Tab** to expand    VALUE1 = "value1",

3. **Tab through placeholders** to fill in values    VALUE2 = "value2"

4. **Press Enter** when done}

```

### Example: Create a Class

### Switch Statement Snippet

``````powerscript

1. Type: class [Tab]// Type: switch + Tab

2. Fill in: Personswitch (expression) {

3. Tab to param: name    case value1:

4. Tab to type: string        // code

5. Tab to method: greet        break;

6. Tab to return type: string    case value2:

7. Done!        // code

```        break;

    default:

Result:        // code

```powerscript}

class Person {```

    constructor(name: string) {

        // constructor body## Commands

    }

    Access via Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`):

    greet(): string {

        // method body### PowerScript: Compile File

    }- Compiles current `.ps` file to Python

}- Shortcut: `Ctrl+Shift+B` / `Cmd+Shift+B`

```- Output: `.py` file in same directory



### Keyboard Shortcuts### PowerScript: Run File

- Compiles and runs current file

| Action | Mac | Windows/Linux |- Shortcut: `Ctrl+Shift+R` / `Cmd+Shift+R`

|--------|-----|---------------|- Output: Terminal shows execution results

| Toggle comment | `Cmd+/` | `Ctrl+/` |

| Block comment | `Cmd+Shift+A` | `Ctrl+Shift+A` |### PowerScript: Create Project

| Format document | `Cmd+Shift+F` | `Ctrl+Shift+F` |- Scaffolds new PowerScript project

| Go to definition | `F12` | `F12` |- Prompts for project name and template

| Find references | `Shift+F12` | `Shift+F12` |- Creates complete project structure

| Rename symbol | `F2` | `F2` |

| Command palette | `Cmd+Shift+P` | `Ctrl+Shift+P` |### Using Commands



### Recommended Settings**Via Command Palette:**

1. Press `Ctrl+Shift+P` / `Cmd+Shift+P`

Add to your VS Code `settings.json`:2. Type "PowerScript"

3. Select desired command

```json

{**Via Right-Click Menu:**

  // PowerScript specific1. Right-click in `.ps` file

  "[powerscript]": {2. Select "Compile PowerScript File" or "Run PowerScript File"

    "editor.defaultFormatter": "esbenp.prettier-vscode",

    "editor.formatOnSave": true,**Via Keyboard:**

    "editor.tabSize": 4,- `Ctrl+Shift+B` - Compile

    "editor.insertSpaces": true- `Ctrl+Shift+R` - Run

  },

  ## Keyboard Shortcuts

  // Bracket pair colorization

  "editor.bracketPairColorization.enabled": true,| Action | Windows/Linux | macOS |

  |--------|---------------|-------|

  // Auto-closing brackets| Compile File | `Ctrl+Shift+B` | `Cmd+Shift+B` |

  "editor.autoClosingBrackets": "always",| Run File | `Ctrl+Shift+R` | `Cmd+Shift+R` |

  "editor.autoClosingQuotes": "always",| Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` |

  | Quick Open | `Ctrl+P` | `Cmd+P` |

  // Suggestions| Toggle Sidebar | `Ctrl+B` | `Cmd+B` |

  "editor.quickSuggestions": {| Toggle Terminal | `Ctrl+\`` | `Cmd+\`` |

    "other": true,

    "comments": false,### Customize Shortcuts

    "strings": false

  },1. Open Keyboard Shortcuts (`Ctrl+K Ctrl+S`)

  2. Search for "PowerScript"

  // File associations3. Click on command and set new binding

  "files.associations": {

    "*.ps": "powerscript",## Configuration

    "*.pscript": "powerscript"

  }### VS Code Settings

}

```Add to `.vscode/settings.json`:



## 🔧 Configuration```json

{

### Extension Settings    "powerscript.enableLSP": true,

    "powerscript.enableDiagnostics": true,

Currently, no custom settings required. The extension works out of the box!    "powerscript.compilerPath": "tps-compile",

    "powerscript.pythonPath": "python3"

**Future Settings (Coming Soon 🔄):**}

- `powerscript.compiler.path` - Custom compiler path```

- `powerscript.linter.enabled` - Enable/disable linting

- `powerscript.format.tabSize` - Tab size for formatting### File Associations

- `powerscript.typecheck.onSave` - Type check on save

Automatically associates `.ps` files with PowerScript:

### Workspace Configuration

```json

Create `.vscode/settings.json` in your project:{

    "files.associations": {

```json        "*.ps": "powerscript"

{    }

  "files.exclude": {}

    "**/__pycache__": true,```

    "**/*.pyc": true,

    "build/": false### Editor Settings

  },

  Recommended settings for PowerScript:

  "search.exclude": {

    "build/": true,```json

    "**/__pycache__": true{

  }    "editor.tabSize": 4,

}    "editor.insertSpaces": true,

```    "editor.formatOnSave": true,

    "editor.suggestSelection": "first",

## 🚀 Workflow Integration    "editor.quickSuggestions": {

        "other": true,

### Compile on Save        "comments": false,

        "strings": false

Create `.vscode/tasks.json`:    }

}

```json```

{

  "version": "2.0.0",## Troubleshooting

  "tasks": [

    {### Extension Not Showing

      "label": "compile-powerscript",

      "type": "shell",**Problem:** Extension doesn't appear in Extensions list

      "command": "tps-compile ${file}",

      "group": {**Solution:**

        "kind": "build",1. Restart VS Code completely

        "isDefault": true2. Check installation: `code --list-extensions`

      },3. Reinstall: `code --install-extension powerscript-1.0.0.vsix`

      "presentation": {

        "reveal": "always",### Syntax Highlighting Not Working

        "panel": "new"

      }**Problem:** `.ps` files not highlighted

    }

  ]**Solution:**

}1. Click language indicator (bottom right)

```2. Select "PowerScript" from list

3. Or add to settings:

**Usage:**   ```json

- Press `Cmd+Shift+B` (Mac) or `Ctrl+Shift+B` (Windows/Linux)   {

- Compiles current `.ps` file automatically       "files.associations": {

           "*.ps": "powerscript"

### Run PowerScript Files       }

   }

Add to `tasks.json`:   ```



```json### Commands Not Working

{

  "label": "run-powerscript",**Problem:** Compile/Run commands fail

  "type": "shell",

  "command": "tps-run ${file}",**Solution:**

  "group": "test",1. Ensure TPS is installed: `pip install tps`

  "presentation": {2. Verify PATH includes Python scripts

    "reveal": "always",3. Test manually: `tps-compile --version`

    "panel": "new"4. Check settings for correct paths

  }

}### Snippets Not Expanding

```

**Problem:** Typing prefix doesn't show snippet

**Usage:**

- `Cmd+Shift+P` → "Tasks: Run Task" → "run-powerscript"**Solution:**

1. Type prefix exactly (e.g., `function`)

### Debug Configuration2. Press `Tab` (not Enter)

3. Ensure file is recognized as PowerScript

Create `.vscode/launch.json`:4. Check settings: `editor.snippetSuggestions`



```json### IntelliSense Not Working

{

  "version": "0.2.0",**Problem:** No auto-completion suggestions

  "configurations": [

    {**Solution:**

      "name": "PowerScript: Current File",1. Check LSP is enabled in settings

      "type": "python",2. Restart VS Code

      "request": "launch",3. Ensure file is saved with `.ps` extension

      "program": "${workspaceFolder}/build/${fileBasenameNoExtension}.py",4. Check output panel for errors

      "console": "integratedTerminal",

      "preLaunchTask": "compile-powerscript"### Error Diagnostics Not Showing

    }

  ]**Problem:** Syntax errors not highlighted

}

```**Solution:**

1. Enable diagnostics in settings

## 🎨 Theme Compatibility2. Check file is saved

3. Restart Language Server: Reload Window

The extension works with all VS Code themes:4. Check PowerScript installation



**Recommended Themes:**## Advanced Usage

- Dark+ (default dark)

- Light+ (default light)### Multi-Root Workspaces

- Monokai

- DraculaPowerScript extension supports multi-root workspaces:

- One Dark Pro

- Material Theme```json

// workspace.code-workspace

All themes provide excellent PowerScript syntax highlighting!{

    "folders": [

## 🔄 Updates        { "path": "project1" },

        { "path": "project2" }

### Check for Updates    ],

    "settings": {

```bash        "powerscript.enableLSP": true

# Check current version    }

code --list-extensions --show-versions | grep powerscript}

```

# Output: saleemlewis.powerscript@1.0.0

```### Custom Build Tasks



### Update ExtensionCreate `.vscode/tasks.json`:



When new versions are released:```json

{

1. Download new `.vsix` file    "version": "2.0.0",

2. Uninstall old version:    "tasks": [

   ```bash        {

   code --uninstall-extension saleemlewis.powerscript            "label": "Compile PowerScript",

   ```            "type": "shell",

3. Install new version:            "command": "tps-compile",

   ```bash            "args": ["${file}"],

   code --install-extension powerscript-<new-version>.vsix            "group": {

   ```                "kind": "build",

                "isDefault": true

## 🐛 Troubleshooting            }

        },

### Extension Not Loading        {

            "label": "Run PowerScript",

**Symptom:** No PowerScript in Extensions panel            "type": "shell",

            "command": "tps-run",

**Solutions:**            "args": ["${file}"]

1. Reload VS Code: `Cmd/Ctrl+Shift+P` → "Reload Window"        }

2. Check installation: View → Extensions → Search "PowerScript"    ]

3. Reinstall from VSIX}

4. Check VS Code version (1.60+ required)```



### No Syntax Highlighting### Debugging Support



**Symptom:** `.ps` files show as plain textWhile native debugging isn't yet supported, you can debug the transpiled Python:



**Solutions:**1. Compile to Python: `tps-compile file.ps -o file.py`

1. Check language mode (bottom right) - should show "PowerScript"2. Add Python breakpoints

2. Manually set language: `Cmd/Ctrl+K M` → type "powerscript"3. Use VS Code Python debugger on `.py` file

3. Check file association in settings

4. Reload window## Tips & Tricks



### Snippets Not Working### Productivity Tips



**Symptom:** Typing `func` doesn't show snippet1. **Use Snippets** - Type prefix + Tab for quick templates

2. **Keyboard Shortcuts** - Learn Ctrl+Shift+B and Ctrl+Shift+R

**Solutions:**3. **IntelliSense** - Press Ctrl+Space for suggestions

1. Check suggestions enabled: Settings → Editor: Quick Suggestions4. **Hover Info** - Hover over types for documentation

2. Press `Cmd+Space` (Mac) or `Ctrl+Space` (Windows/Linux) to trigger manually5. **Quick Open** - Ctrl+P to quickly open files

3. Type snippet prefix and press `Tab` instead of `Enter`

4. Verify extension installed correctly### Best Practices



### Performance Issues1. **Save Frequently** - Diagnostics run on save

2. **Organize Imports** - Keep imports at top

**Symptom:** VS Code slow with large `.ps` files3. **Use Type Annotations** - Get better IntelliSense

4. **Format Code** - Use consistent spacing

**Solutions:**5. **Check Terminal** - Watch for compilation errors

1. Increase memory limit: Settings → Files: Max Memory For Large File (MB)

2. Disable unused extensions### Extension Updates

3. Close other heavy files

4. Split large files into modulesTo update the extension:



## 📚 Coming Soon 🔄1. Download latest `.vsix` from GitHub

2. Uninstall old version

Future extension features:3. Install new version

4. Restart VS Code

- **LSP Integration** - Real-time error checking

- **IntelliSense** - Smart code completion## Resources

- **Go to Definition** - Jump to symbol definitions

- **Find References** - Find all symbol usages- **Extension Documentation**: See `vscode-extension/README.md` in repo

- **Rename Refactoring** - Rename across files- **Quick Reference**: See `vscode-extension/QUICK_REFERENCE.md`

- **Code Actions** - Quick fixes and refactorings- **GitHub**: [Python-PowerScript](https://github.com/SaleemLww/Python-PowerScript)

- **Debugging Support** - Step-through debugging- **Issues**: [Report problems](https://github.com/SaleemLww/Python-PowerScript/issues)

- **Test Explorer** - Run and view tests

## Next Steps

## 🆘 Getting Help

1. ✅ Install the VS Code extension

**Issues with Extension?**2. ✅ Try the code snippets

- Check [Troubleshooting](troubleshooting.md)3. ✅ Use compile and run commands

- Report issue: [GitHub Issues](https://github.com/SaleemLww/Python-PowerScript/issues)4. ✅ Start building with PowerScript!

- Ask community: [GitHub Discussions](https://github.com/SaleemLww/Python-PowerScript/discussions)

---

---

**Happy coding with PowerScript in VS Code!** 🚀

**Extension installed? Start coding with [Quick Start](quickstart.md)! 🚀**
