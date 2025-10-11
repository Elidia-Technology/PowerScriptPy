# 🎨 VS Code Extension Guide# 🎨 VS Code Extension Guide# 🎨 VS Code Extension Guide# 🎨 VS Code Extension Guide# VS Code Extension Guide



Complete guide to the PowerScript VS Code extension.



## 📦 InstallationComplete guide to the PowerScript VS Code extension.



### Method 1: Install from VSIX (Recommended)



1. **Locate Extension File**---Complete guide to the PowerScript VS Code extension.

   ```bash

   # In PowerScript repository

   cd vscode-extension

   # File: powerscript-1.0.0.vsix (550.28 KB)## 📦 Installation

   ```



2. **Install in VS Code**

   - Open VS Code### Method 1: Install from VSIX (Recommended)---Complete guide to the PowerScript VS Code extension.The PowerScript VS Code extension provides a complete IDE experience with syntax highlighting, IntelliSense, error diagnostics, and more!

   - Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)

   - Type: `Extensions: Install from VSIX`

   - Navigate to `powerscript-1.0.0.vsix`

   - Click "Install"1. **Locate Extension File**



3. **Verify Installation**

   - Create file: `test.ps`

   - Should see PowerScript syntax highlighting```bash## 📦 Installation

   - Check Extensions panel for "PowerScript"

# In PowerScript repository

### Method 2: Build from Source

cd vscode-extension

```bash

cd vscode-extension# File: powerscript-1.0.0.vsix (550.28 KB)



# Install Node.js dependencies```### Method 1: Install from VSIX (Recommended)## 📦 Installation## Table of Contents

npm install



# Compile

npm run compile2. **Install in VS Code**



# Package extension

npm install -g vsce

vsce package```bash1. **Locate Extension File**- [Features](#features)



# Install the generated .vsix# Using command line

code --install-extension powerscript-1.0.0.vsix

```code --install-extension powerscript-1.0.0.vsix   ```bash



## ✨ Features



### 1. Syntax Highlighting ✅# OR using VS Code UI:   # In PowerScript repository### Method 1: Install from VSIX (Recommended)- [Installation](#installation)



Beautiful, semantic highlighting for PowerScript code:# - Press Cmd+Shift+P (Mac) or Ctrl+Shift+P (Windows/Linux)



**Keywords:**# - Type: "Extensions: Install from VSIX"   cd vscode-extension

- Control flow: `if`, `else`, `for`, `while`, `switch`, `case`

- Types: `string`, `number`, `boolean`, `void`, `any`, `null`# - Navigate to powerscript-1.0.0.vsix

- Modifiers: `public`, `private`, `protected`, `static`, `async`

- Classes: `class`, `interface`, `abstract`, `extends`# - Click "Install"   # File: powerscript-1.0.0.vsix (550.28 KB)- [Getting Started](#getting-started)

- Functions: `function`, `return`, `constructor`

- Modules: `import`, `export`, `from`, `as````



**Operators:**   ```

- Arithmetic: `+`, `-`, `*`, `/`, `%`

- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`3. **Verify Installation**

- Logical: `&&`, `||`, `!`

1. **Locate Extension File**- [Code Snippets](#code-snippets)

**Literals:**

- Strings: `"double quotes"`, `'single quotes'`- Create file: `test.ps`

- Numbers: `42`, `3.14`

- Booleans: `true`, `false`- Should see PowerScript syntax highlighting2. **Install in VS Code**



### 2. Code Snippets ✅- Check Extensions panel for "PowerScript"



13 intelligent snippets for common patterns:   - Open VS Code   ```bash- [Commands](#commands)



#### Basic Snippets### Method 2: Build from Source



**`func`** - Function Declaration   - Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)

```powerscript

function functionName(param: type): returnType {```bash

    // function body

}cd vscode-extension   - Type: `Extensions: Install from VSIX`   # In PowerScript repository- [Keyboard Shortcuts](#keyboard-shortcuts)

```



**`class`** - Class with Constructor

```powerscript# Install Node.js dependencies   - Navigate to `powerscript-1.0.0.vsix`

class ClassName {

    constructor(param: type) {npm install

        // constructor body

    }   - Click "Install"   cd vscode-extension- [Configuration](#configuration)

    

    methodName(): returnType {# Compile TypeScript

        // method body

    }npm run compile

}

```



**`interface`** - Interface Declaration# Package extension3. **Verify Installation**   # File: powerscript-1.0.0.vsix (550.28 KB)- [Troubleshooting](#troubleshooting)

```powerscript

interface InterfaceName {npm install -g vsce

    property: type;

    method(): returnType;vsce package   - Create file: `test.ps`

}

```



#### Control Flow Snippets# Install the generated .vsix   - Should see PowerScript syntax highlighting   ```



**`if`** - If Statementcode --install-extension powerscript-1.0.0.vsix

```powerscript

if (condition) {```   - Check Extensions panel for "PowerScript"

    // true block

}

```

---## Features

**`ife`** - If-Else Statement

```powerscript

if (condition) {

    // true block## ✨ Features### Method 2: Build from Source

} else {

    // false block

}

```### 1. Syntax Highlighting ✅2. **Install in VS Code**



**`for`** - For Loop

```powerscript

for (let i = 0; i < length; i++) {Beautiful, semantic highlighting for PowerScript code:```bash

    // loop body

}

```

**Keywords:**cd vscode-extension   - Open VS Code### ✨ Syntax Highlighting

**`while`** - While Loop

```powerscript- Control flow: `if`, `else`, `for`, `while`, `switch`, `case`

while (condition) {

    // loop body- Types: `string`, `number`, `boolean`, `void`, `any`, `null`, `undefined`

}

```- Modifiers: `public`, `private`, `protected`, `static`, `async`, `const`, `let`



#### Module Snippets- Classes: `class`, `interface`, `abstract`, `extends`, `implements`# Install Node.js dependencies   - Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)- Full syntax highlighting for `.ps` files



**`import`** - Import Statement- Functions: `function`, `return`, `constructor`

```powerscript

import { symbol } from "module";- Modules: `import`, `export`, `from`, `as`npm install

```



**`export`** - Export Statement

```powerscript**Operators & Symbols:**   - Type: `Extensions: Install from VSIX`- Color-coded keywords, strings, comments, types

export class ClassName {

    // class body- Arithmetic: `+`, `-`, `*`, `/`, `%`

}

```- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`# Compile TypeScript



### 3. File Recognition ✅- Logical: `&&`, `||`, `!`



**Supported Extensions:**- Assignment: `=`, `+=`, `-=`, `*=`, `/=`npm run compile   - Navigate to `powerscript-1.0.0.vsix`- Support for modern PowerScript features

- `.ps` - PowerScript source files

- `.pscript` - Alternative extension



**Auto-Detection:****Literals:**

- VS Code automatically applies PowerScript syntax

- Language mode shows "PowerScript" in status bar- Strings: `"double quotes"`, `'single quotes'`



### 4. Comment Support ✅- Numbers: `42`, `3.14`, `0xFF`# Package extension   - Click "Install"- Semantic highlighting for better readability



**Single-line Comments:**- Booleans: `true`, `false`

```powerscript

// This is a single-line comment- Null: `null`, `undefined`npm install -g vsce

let x: number = 5; // inline comment

```



**Multi-line Comments:**### 2. Code Snippets ✅vsce package

```powerscript

/*

 * This is a

 * multi-line comment13 intelligent snippets for common patterns:

 */

```



**Toggle Comments:**#### Basic Snippets# Install the generated .vsix3. **Verify Installation**### 🧠 IntelliSense

- Single-line: `Cmd+/` (Mac) or `Ctrl+/` (Windows/Linux)

- Block comment: `Cmd+Shift+A` (Mac) or `Ctrl+Shift+A` (Windows/Linux)



### 5. Bracket Matching ✅**`func`** - Function Declarationcode --install-extension powerscript-1.0.0.vsix



**Auto-completion:**```powerscript

- Type `{` → Auto-completes `}`

- Type `[` → Auto-completes `]`function functionName(param: type): returnType {```   - Create file: `test.ps`- Auto-completion for keywords and types

- Type `(` → Auto-completes `)`

- Type `"` → Auto-completes `"`    // function body



**Auto-surrounding:**}

- Select text and type `{` → Wraps in `{}`

- Select text and type `"` → Wraps in `""````



## 🎯 Usage Tips---   - Should see PowerScript syntax highlighting- Function and method suggestions



### Snippet Workflow**`arrow`** - Arrow Function



1. **Type snippet prefix** (e.g., `func`)```powerscript

2. **Press Tab** to expand

3. **Tab through placeholders** to fill in valuesconst name = (param: type): returnType => {

4. **Press Enter** when done

    // function body## ✨ Features   - Check Extensions panel for "PowerScript"- Variable name completion

### Keyboard Shortcuts

};

| Action | Mac | Windows/Linux |

|--------|-----|---------------|```

| Toggle comment | `Cmd+/` | `Ctrl+/` |

| Block comment | `Cmd+Shift+A` | `Ctrl+Shift+A` |

| Format document | `Cmd+Shift+F` | `Ctrl+Shift+F` |

| Command palette | `Cmd+Shift+P` | `Ctrl+Shift+P` |**`class`** - Class with Constructor### 1. Syntax Highlighting ✅- Import statement assistance



### Recommended Settings```powerscript



Add to your VS Code `settings.json`:class ClassName {



```json    constructor(param: type) {

{

  "[powerscript]": {        // constructor bodyBeautiful, semantic highlighting for PowerScript code:### Method 2: Build from Source- Parameter hints

    "editor.tabSize": 4,

    "editor.insertSpaces": true,    }

    "editor.formatOnSave": true

  },    

  

  "editor.bracketPairColorization.enabled": true,    methodName(): returnType {

  "editor.autoClosingBrackets": "always",

  "editor.autoClosingQuotes": "always",        // method body**Keywords:**

  

  "files.associations": {    }

    "*.ps": "powerscript",

    "*.pscript": "powerscript"}- Control flow: `if`, `else`, `for`, `while`, `switch`, `case`

  }

}```

```

- Types: `string`, `number`, `boolean`, `void`, `any`, `null`, `undefined````bash### 🔍 Error Diagnostics

## 🚀 Workflow Integration

**`interface`** - Interface Declaration

### Compile on Save

```powerscript- Modifiers: `public`, `private`, `protected`, `static`, `async`, `const`, `let`

Create `.vscode/tasks.json`:

interface InterfaceName {

```json

{    property: type;- Classes: `class`, `interface`, `abstract`, `extends`, `implements`cd vscode-extension- Real-time syntax error detection

  "version": "2.0.0",

  "tasks": [    method(): returnType;

    {

      "label": "compile-powerscript",}- Functions: `function`, `return`, `constructor`

      "type": "shell",

      "command": "tps-compile ${file}",```

      "group": {

        "kind": "build",- Modules: `import`, `export`, `from`, `as`- Type checking warnings

        "isDefault": true

      }#### Control Flow Snippets

    }

  ]

}

```**`if`** - If Statement



**Usage:**```powerscript**Operators & Symbols:**# Install Node.js dependencies- Missing semicolon suggestions

- Press `Cmd+Shift+B` (Mac) or `Ctrl+Shift+B` (Windows/Linux)

- Compiles current `.ps` file automaticallyif (condition) {



### Run PowerScript Files    // true block- Arithmetic: `+`, `-`, `*`, `/`, `%`



Add to `tasks.json`:}



```json```- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`npm install- Unknown type flags

{

  "label": "run-powerscript",

  "type": "shell",

  "command": "tps-run ${file}",**`ife`** - If-Else Statement- Logical: `&&`, `||`, `!`

  "group": "test"

}```powerscript

```

if (condition) {- Assignment: `=`, `+=`, `-=`, `*=`, `/=`- Inline error messages

## 🎨 Theme Compatibility

    // true block

The extension works with all VS Code themes:

} else {

**Recommended Themes:**

- Dark+ (default dark)    // false block

- Light+ (default light)

- Monokai}**Literals:**# Compile TypeScript

- Dracula

- One Dark Pro```



## 🐛 Troubleshooting- Strings: `"double quotes"`, `'single quotes'`



### Extension Not Loading**`for`** - For Loop



**Symptom:** No PowerScript in Extensions panel```powerscript- Numbers: `42`, `3.14`, `0xFF`npm run compile### 📝 Code Snippets



**Solutions:**for (let i = 0; i < length; i++) {

1. Reload VS Code: `Cmd/Ctrl+Shift+P` → "Reload Window"

2. Check installation: View → Extensions → Search "PowerScript"    // loop body- Booleans: `true`, `false`

3. Reinstall from VSIX

}

### No Syntax Highlighting

```- Null: `null`, `undefined`13 built-in code snippets for common patterns:

**Symptom:** `.ps` files show as plain text



**Solutions:**

1. Check language mode (bottom right) - should show "PowerScript"**`while`** - While Loop

2. Manually set language: `Cmd/Ctrl+K M` → type "powerscript"

3. Reload window```powerscript



### Snippets Not Workingwhile (condition) {### 2. Code Snippets ✅# Package extension- `function` - Function declaration



**Symptom:** Typing `func` doesn't show snippet    // loop body



**Solutions:**}

1. Press `Cmd+Space` (Mac) or `Ctrl+Space` (Windows/Linux)

2. Type snippet prefix and press `Tab````

3. Verify extension installed correctly

13 intelligent snippets for common patterns:npm install -g vsce- `class` - Class definition

## 📚 Coming Soon 🔄

**`switch`** - Switch Statement

Future extension features:

```powerscript

- **LSP Integration** - Real-time error checking

- **IntelliSense** - Smart code completionswitch (expression) {

- **Go to Definition** - Jump to symbol definitions

- **Find References** - Find all symbol usages    case value1:#### Basic Snippetsvsce package- `interface` - Interface declaration

- **Debugging Support** - Step-through debugging

        // case 1

## 🆘 Getting Help

        break;

**Issues with Extension?**

- Check [FAQ](faq.md)    case value2:

- Report issue: [GitHub Issues](https://github.com/SaleemLww/Python-PowerScript/issues)

- Ask community: [GitHub Discussions](https://github.com/SaleemLww/Python-PowerScript/discussions)        // case 2**`func`** - Function Declaration- `arrow` - Arrow function



---        break;



**Extension installed? Start coding with [Quick Start](quickstart.md)! 🚀**    default:```powerscript


        // default case

}function functionName(param: type): returnType {# Install the generated .vsix- `async` - Async function

```

    // function body

#### Module Snippets

}code --install-extension powerscript-1.0.0.vsix- `if` - If statement

**`import`** - Import Statement

```powerscript```

import { symbol } from "module";

``````- `for` - For loop



**`export`** - Export Statement**`arrow`** - Arrow Function

```powerscript

export class ClassName {```powerscript- `while` - While loop

    // class body

}const name = (param: type): returnType => {

```

    // function body## ✨ Features- `try` - Try-catch block

#### Advanced Snippets

};

**`async`** - Async Function

```powerscript```- `switch` - Switch statement

async function functionName(): Promise<type> {

    // async body

}

```**`class`** - Class with Constructor### 1. Syntax Highlighting ✅- `enum` - Enum declaration



**`enum`** - Enum Declaration```powerscript

```powerscript

enum EnumName {class ClassName {- `import` - Import statement

    Value1,

    Value2,    constructor(param: type) {

    Value3

}        // constructor bodyBeautiful, semantic highlighting for PowerScript code:- `export` - Export statement

```

    }

### 3. File Recognition ✅

    

**Supported Extensions:**

- `.ps` - PowerScript source files    methodName(): returnType {

- `.pscript` - Alternative extension

        // method body**Keywords:**### 🎯 Commands

**Auto-Detection:**

- VS Code automatically applies PowerScript syntax when opening `.ps` files    }

- Language mode shows "PowerScript" in status bar

}- Control flow: `if`, `else`, `for`, `while`, `switch`, `case`- **Compile File** - Compile current `.ps` file to Python

### 4. Comment Support ✅

```

**Single-line Comments:**

```powerscript- Types: `string`, `number`, `boolean`, `void`, `any`, `null`, `undefined`- **Run File** - Compile and run current file

// This is a single-line comment

let x: number = 5; // inline comment**`interface`** - Interface Declaration

```

```powerscript- Modifiers: `public`, `private`, `protected`, `static`, `async`, `const`, `let`- **Create Project** - Scaffold new PowerScript project

**Multi-line Comments:**

```powerscriptinterface InterfaceName {

/*

 * This is a    property: type;- Classes: `class`, `interface`, `abstract`, `extends`, `implements`

 * multi-line comment

 */    method(): returnType;

function test(): void {

    /* inline block comment */}- Functions: `function`, `return`, `constructor`### ⌨️ Keyboard Shortcuts

}

``````



**Block Comments:**- Modules: `import`, `export`, `from`, `as`- `Ctrl+Shift+B` / `Cmd+Shift+B` - Compile current file

- Toggle: `Cmd+/` (Mac) or `Ctrl+/` (Windows/Linux)

- Block comment: `Cmd+Shift+A` (Mac) or `Ctrl+Shift+A` (Windows/Linux)#### Control Flow Snippets



### 5. Bracket Matching ✅- `Ctrl+Shift+R` / `Cmd+Shift+R` - Run current file



**Auto-completion:****`if`** - If Statement

- Type `{` → Auto-completes `}`

- Type `[` → Auto-completes `]````powerscript**Operators & Symbols:**

- Type `(` → Auto-completes `)`

- Type `"` → Auto-completes `"`if (condition) {

- Type `'` → Auto-completes `'`

    // true block- Arithmetic: `+`, `-`, `*`, `/`, `%`### 📚 Additional Features

**Auto-surrounding:**

- Select text and type `{` → Wraps in `{}`}

- Select text and type `"` → Wraps in `""`

```- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`- Hover information for types and functions

**Bracket colorization:**

- Nested brackets shown in different colors

- Easy to match opening/closing pairs

**`ife`** - If-Else Statement- Logical: `&&`, `||`, `!`- Definition and reference finding

---

```powerscript

## 🎯 Usage Tips

if (condition) {- Assignment: `=`, `+=`, `-=`, `*=`, `/=`- Document formatting

### Snippet Workflow

    // true block

1. **Type snippet prefix** (e.g., `func`)

2. **Press Tab** to expand} else {- Code folding

3. **Tab through placeholders** to fill in values

4. **Press Enter** when done    // false block



### Example: Create a Class}**Literals:**- Bracket matching



``````

1. Type: class [Tab]

2. Fill in: Person- Strings: `"double quotes"`, `'single quotes'`- Comment toggling

3. Tab to param: name

4. Tab to type: string**`for`** - For Loop

5. Tab to method: greet

6. Tab to return type: string```powerscript- Numbers: `42`, `3.14`, `0xFF`

7. Done!

```for (let i = 0; i < length; i++) {



Result:    // loop body- Booleans: `true`, `false`## Installation

```powerscript

class Person {}

    constructor(name: string) {

        // constructor body```- Null: `null`, `undefined`

    }

    

    greet(): string {

        // method body**`while`** - While Loop### Method 1: Install from GitHub Release

    }

}```powerscript

```

while (condition) {### 2. Code Snippets ✅

### Keyboard Shortcuts

    // loop body

| Action | Mac | Windows/Linux |

|--------|-----|---------------|}1. **Visit the GitHub Repository**

| Toggle comment | `Cmd+/` | `Ctrl+/` |

| Block comment | `Cmd+Shift+A` | `Ctrl+Shift+A` |```

| Format document | `Cmd+Shift+F` | `Ctrl+Shift+F` |

| Go to definition | `F12` | `F12` |13 intelligent snippets for common patterns:   ```

| Find references | `Shift+F12` | `Shift+F12` |

| Rename symbol | `F2` | `F2` |**`switch`** - Switch Statement

| Command palette | `Cmd+Shift+P` | `Ctrl+Shift+P` |

```powerscript   https://github.com/SaleemLww/Python-PowerScript

### Recommended Settings

switch (expression) {

Add to your VS Code `settings.json`:

    case value1:#### Basic Snippets   ```

```json

{        // case 1

  // PowerScript specific

  "[powerscript]": {        break;

    "editor.defaultFormatter": "esbenp.prettier-vscode",

    "editor.formatOnSave": true,    case value2:

    "editor.tabSize": 4,

    "editor.insertSpaces": true        // case 2**`func`** - Function Declaration2. **Download the Extension**

  },

          break;

  // Bracket pair colorization

  "editor.bracketPairColorization.enabled": true,    default:```powerscript   - Navigate to the `vscode-extension/` folder

  

  // Auto-closing brackets        // default case

  "editor.autoClosingBrackets": "always",

  "editor.autoClosingQuotes": "always",}function functionName(param: type): returnType {   - Download the latest `.vsix` file

  

  // Suggestions```

  "editor.quickSuggestions": {

    "other": true,    // function body   - Or clone the entire repository

    "comments": false,

    "strings": false#### Module Snippets

  },

  }

  // File associations

  "files.associations": {**`import`** - Import Statement

    "*.ps": "powerscript",

    "*.pscript": "powerscript"```powerscript```3. **Install in VS Code**

  }

}import { symbol } from "module";

```

```   ```bash

---



## 🔧 Configuration

**`export`** - Export Statement**`arrow`** - Arrow Function   code --install-extension powerscript-1.0.0.vsix

### Extension Settings

```powerscript

Currently, no custom settings required. The extension works out of the box!

export class ClassName {```powerscript   ```

**Future Settings (Coming Soon 🔄):**

- `powerscript.compiler.path` - Custom compiler path    // class body

- `powerscript.linter.enabled` - Enable/disable linting

- `powerscript.format.tabSize` - Tab size for formatting}const name = (param: type): returnType => {

- `powerscript.typecheck.onSave` - Type check on save

```

### Workspace Configuration

    // function body### Method 2: Build from Source

Create `.vscode/settings.json` in your project:

#### Advanced Snippets

```json

{};

  "files.exclude": {

    "**/__pycache__": true,**`async`** - Async Function

    "**/*.pyc": true,

    "build/": false```powerscript``````bash

  },

  async function functionName(): Promise<type> {

  "search.exclude": {

    "build/": true,    // async body# Clone the repository

    "**/__pycache__": true

  }}

}

``````**`class`** - Class with Constructorgit clone https://github.com/SaleemLww/Python-PowerScript.git



---



## 🚀 Workflow Integration**`enum`** - Enum Declaration```powerscriptcd Python-PowerScript/vscode-extension



### Compile on Save```powerscript



Create `.vscode/tasks.json`:enum EnumName {class ClassName {



```json    Value1,

{

  "version": "2.0.0",    Value2,    constructor(param: type) {# Install dependencies

  "tasks": [

    {    Value3

      "label": "compile-powerscript",

      "type": "shell",}        // constructor bodynpm install

      "command": "tps-compile ${file}",

      "group": {```

        "kind": "build",

        "isDefault": true    }

      },

      "presentation": {### 3. File Recognition ✅

        "reveal": "always",

        "panel": "new"    # Compile the extension source

      }

    }**Supported Extensions:**

  ]

}- `.ps` - PowerScript source files    methodName(): returnType {npm run compile

```

- `.pscript` - Alternative extension

**Usage:**

- Press `Cmd+Shift+B` (Mac) or `Ctrl+Shift+B` (Windows/Linux)        // method body

- Compiles current `.ps` file automatically

**Auto-Detection:**

### Run PowerScript Files

- VS Code automatically applies PowerScript syntax when opening `.ps` files    }# Package the extension

Add to `tasks.json`:

- Language mode shows "PowerScript" in status bar

```json

{}npx vsce package

  "label": "run-powerscript",

  "type": "shell",### 4. Comment Support ✅

  "command": "tps-run ${file}",

  "group": "test",```

  "presentation": {

    "reveal": "always",**Single-line Comments:**

    "panel": "new"

  }```powerscript# Install the generated .vsix file

}

```// This is a single-line comment



**Usage:**let x: number = 5; // inline comment**`interface`** - Interface Declarationcode --install-extension powerscript-1.0.0.vsix

- `Cmd+Shift+P` → "Tasks: Run Task" → "run-powerscript"

```

### Debug Configuration

```powerscript```

Create `.vscode/launch.json`:

**Multi-line Comments:**

```json

{```powerscriptinterface InterfaceName {

  "version": "0.2.0",

  "configurations": [/*

    {

      "name": "PowerScript: Current File", * This is a    property: type;### Method 3: Install via VS Code UI

      "type": "python",

      "request": "launch", * multi-line comment

      "program": "${workspaceFolder}/build/${fileBasenameNoExtension}.py",

      "console": "integratedTerminal", */    method(): returnType;

      "preLaunchTask": "compile-powerscript"

    }function test(): void {

  ]

}    /* inline block comment */}1. Open VS Code

```

}

---

``````2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)

## 🎨 Theme Compatibility



The extension works with all VS Code themes:

**Block Comments:**3. Type: "Extensions: Install from VSIX..."

**Recommended Themes:**

- Dark+ (default dark)- Toggle: `Cmd+/` (Mac) or `Ctrl+/` (Windows/Linux)

- Light+ (default light)

- Monokai- Block comment: `Cmd+Shift+A` (Mac) or `Ctrl+Shift+A` (Windows/Linux)#### Control Flow Snippets4. Select the downloaded `.vsix` file

- Dracula

- One Dark Pro

- Material Theme

### 5. Bracket Matching ✅5. Restart VS Code

All themes provide excellent PowerScript syntax highlighting!



---

**Auto-completion:****`if`** - If Statement

## 🔄 Updates

- Type `{` → Auto-completes `}`

### Check for Updates

- Type `[` → Auto-completes `]````powerscript### Verify Installation

```bash

# Check current version- Type `(` → Auto-completes `)`

code --list-extensions --show-versions | grep powerscript

- Type `"` → Auto-completes `"`if (condition) {

# Output: saleemlewis.powerscript@1.0.0

```- Type `'` → Auto-completes `'`



### Update Extension    // true block1. Open VS Code



When new versions are released:**Auto-surrounding:**



1. Download new `.vsix` file- Select text and type `{` → Wraps in `{}`}2. Go to Extensions (`Ctrl+Shift+X`)

2. Uninstall old version:

```bash- Select text and type `"` → Wraps in `""`

code --uninstall-extension saleemlewis.powerscript

``````3. Search for "PowerScript"

3. Install new version:

```bash**Bracket colorization:**

code --install-extension powerscript-<new-version>.vsix

```- Nested brackets shown in different colors4. You should see "PowerScript Language Support" installed



---- Easy to match opening/closing pairs



## 🐛 Troubleshooting**`ife`** - If-Else Statement



### Extension Not Loading---



**Symptom:** No PowerScript in Extensions panel```powerscript## Getting Started



**Solutions:**## 🎯 Usage Tips

1. Reload VS Code: `Cmd/Ctrl+Shift+P` → "Reload Window"

2. Check installation: View → Extensions → Search "PowerScript"if (condition) {

3. Reinstall from VSIX

4. Check VS Code version (1.60+ required)### Snippet Workflow



### No Syntax Highlighting    // true block### Open a PowerScript File



**Symptom:** `.ps` files show as plain text1. **Type snippet prefix** (e.g., `func`)



**Solutions:**2. **Press Tab** to expand} else {

1. Check language mode (bottom right) - should show "PowerScript"

2. Manually set language: `Cmd/Ctrl+K M` → type "powerscript"3. **Tab through placeholders** to fill in values

3. Check file association in settings

4. Reload window4. **Press Enter** when done    // false block1. Create a new file with `.ps` extension



### Snippets Not Working



**Symptom:** Typing `func` doesn't show snippet### Example: Create a Class}2. VS Code automatically activates PowerScript mode



**Solutions:**

1. Check suggestions enabled: Settings → Editor: Quick Suggestions

2. Press `Cmd+Space` (Mac) or `Ctrl+Space` (Windows/Linux) to trigger manually``````3. Start coding with full IDE support!

3. Type snippet prefix and press `Tab` instead of `Enter`

4. Verify extension installed correctly1. Type: class [Tab]



### Performance Issues2. Fill in: Person



**Symptom:** VS Code slow with large `.ps` files3. Tab to param: name



**Solutions:**4. Tab to type: string**`for`** - For Loop### First PowerScript File

1. Increase memory limit: Settings → Files: Max Memory For Large File (MB)

2. Disable unused extensions5. Tab to method: greet

3. Close other heavy files

4. Split large files into modules6. Tab to return type: string```powerscript



---7. Done!



## 📚 Coming Soon 🔄```for (let i = 0; i < length; i++) {Create `hello.ps`:



Future extension features:



- **LSP Integration** - Real-time error checkingResult:    // loop body

- **IntelliSense** - Smart code completion

- **Go to Definition** - Jump to symbol definitions```powerscript

- **Find References** - Find all symbol usages

- **Rename Refactoring** - Rename across filesclass Person {}```powerscript

- **Code Actions** - Quick fixes and refactorings

- **Debugging Support** - Step-through debugging    constructor(name: string) {

- **Test Explorer** - Run and view tests

        // constructor body```// hello.ps

---

    }

## 🆘 Getting Help

    console.log("Hello, PowerScript!");

**Issues with Extension?**

- Check [FAQ](faq.md)    greet(): string {

- Report issue: [GitHub Issues](https://github.com/SaleemLww/Python-PowerScript/issues)

- Ask community: [GitHub Discussions](https://github.com/SaleemLww/Python-PowerScript/discussions)        // method body**`while`** - While Loop



---    }



<div align="center">}```powerscriptfunction greet(name: string): string {



**Extension installed? Start coding with [Quick Start](quickstart.md)! 🚀**```



</div>while (condition) {    return f"Hello, {name}!";


### Keyboard Shortcuts

    // loop body}

| Action | Mac | Windows/Linux |

|--------|-----|---------------|}

| Toggle comment | `Cmd+/` | `Ctrl+/` |

| Block comment | `Cmd+Shift+A` | `Ctrl+Shift+A` |```let message = greet("World");

| Format document | `Cmd+Shift+F` | `Ctrl+Shift+F` |

| Go to definition | `F12` | `F12` |console.log(message);

| Find references | `Shift+F12` | `Shift+F12` |

| Rename symbol | `F2` | `F2` |**`switch`** - Switch Statement```

| Command palette | `Cmd+Shift+P` | `Ctrl+Shift+P` |

```powerscript

### Recommended Settings

switch (expression) {### Using the Extension

Add to your VS Code `settings.json`:

    case value1:

```json

{        // case 11. **Syntax Highlighting** - Automatically applied

  // PowerScript specific

  "[powerscript]": {        break;2. **IntelliSense** - Type and see suggestions

    "editor.defaultFormatter": "esbenp.prettier-vscode",

    "editor.formatOnSave": true,    case value2:3. **Error Detection** - Errors appear as red underlines

    "editor.tabSize": 4,

    "editor.insertSpaces": true        // case 24. **Compile** - Right-click → "Compile PowerScript File"

  },

          break;5. **Run** - Right-click → "Run PowerScript File"

  // Bracket pair colorization

  "editor.bracketPairColorization.enabled": true,    default:

  

  // Auto-closing brackets        // default case## Code Snippets

  "editor.autoClosingBrackets": "always",

  "editor.autoClosingQuotes": "always",}

  

  // Suggestions```Type the prefix and press `Tab` to expand:

  "editor.quickSuggestions": {

    "other": true,

    "comments": false,

    "strings": false#### Module Snippets### Function Snippet

  },

  ```powerscript

  // File associations

  "files.associations": {**`import`** - Import Statement// Type: function + Tab

    "*.ps": "powerscript",

    "*.pscript": "powerscript"```powerscriptfunction functionName(param: type): returnType {

  }

}import { symbol } from "module";    // function body

```

```    return value;

---

}

## 🔧 Configuration

**`export`** - Export Statement```

### Extension Settings

```powerscript

Currently, no custom settings required. The extension works out of the box!

export class ClassName {### Class Snippet

**Future Settings (Coming Soon 🔄):**

- `powerscript.compiler.path` - Custom compiler path    // class body```powerscript

- `powerscript.linter.enabled` - Enable/disable linting

- `powerscript.format.tabSize` - Tab size for formatting}// Type: class + Tab

- `powerscript.typecheck.onSave` - Type check on save

```class ClassName {

### Workspace Configuration

    private property: type;

Create `.vscode/settings.json` in your project:

#### Advanced Snippets    

```json

{    constructor(param: type) {

  "files.exclude": {

    "**/__pycache__": true,**`async`** - Async Function        this.property = param;

    "**/*.pyc": true,

    "build/": false```powerscript    }

  },

  async function functionName(): Promise<type> {    

  "search.exclude": {

    "build/": true,    // async body    public method(): returnType {

    "**/__pycache__": true

  }}        // method body

}

``````    }



---}



## 🚀 Workflow Integration**`enum`** - Enum Declaration```



### Compile on Save```powerscript



Create `.vscode/tasks.json`:enum EnumName {### Arrow Function Snippet



```json    Value1,```powerscript

{

  "version": "2.0.0",    Value2,// Type: arrow + Tab

  "tasks": [

    {    Value3const functionName = (param: type): returnType => {

      "label": "compile-powerscript",

      "type": "shell",}    return value;

      "command": "tps-compile ${file}",

      "group": {```};

        "kind": "build",

        "isDefault": true

      },

      "presentation": {### 3. File Recognition ✅// Or single expression

        "reveal": "always",

        "panel": "new"const square = (x: number): number => x * x;

      }

    }**Supported Extensions:**```

  ]

}- `.ps` - PowerScript source files

```

- `.pscript` - Alternative extension### Async Function Snippet

**Usage:**

- Press `Cmd+Shift+B` (Mac) or `Ctrl+Shift+B` (Windows/Linux)```powerscript

- Compiles current `.ps` file automatically

**Auto-Detection:**// Type: async + Tab

### Run PowerScript Files

- VS Code automatically applies PowerScript syntax when opening `.ps` filesasync function asyncFunction(): Promise<type> {

Add to `tasks.json`:

- Language mode shows "PowerScript" in status bar    const result = await someAsyncOperation();

```json

{    return result;

  "label": "run-powerscript",

  "type": "shell",### 4. Comment Support ✅}

  "command": "tps-run ${file}",

  "group": "test",```

  "presentation": {

    "reveal": "always",**Single-line Comments:**

    "panel": "new"

  }```powerscript### If Statement Snippet

}

```// This is a single-line comment```powerscript



**Usage:**let x: number = 5; // inline comment// Type: if + Tab

- `Cmd+Shift+P` → "Tasks: Run Task" → "run-powerscript"

```if (condition) {

### Debug Configuration

    // code

Create `.vscode/launch.json`:

**Multi-line Comments:**} else {

```json

{```powerscript    // code

  "version": "0.2.0",

  "configurations": [/*}

    {

      "name": "PowerScript: Current File", * This is a```

      "type": "python",

      "request": "launch", * multi-line comment

      "program": "${workspaceFolder}/build/${fileBasenameNoExtension}.py",

      "console": "integratedTerminal", */### For Loop Snippet

      "preLaunchTask": "compile-powerscript"

    }function test(): void {```powerscript

  ]

}    /* inline block comment */// Type: for + Tab

```

}let i = 0;

---

```for (i = 0; i < length; i += 1) {

## 🎨 Theme Compatibility

    // loop body

The extension works with all VS Code themes:

**Block Comments:**}

**Recommended Themes:**

- Dark+ (default dark)- Toggle: `Cmd+/` (Mac) or `Ctrl+/` (Windows/Linux)```

- Light+ (default light)

- Monokai- Block comment: `Cmd+Shift+A` (Mac) or `Ctrl+Shift+A` (Windows/Linux)

- Dracula

- One Dark Pro### Try-Catch Snippet

- Material Theme

### 5. Bracket Matching ✅```powerscript

All themes provide excellent PowerScript syntax highlighting!

// Type: try + Tab

---

**Auto-completion:**try {

## 🔄 Updates

- Type `{` → Auto-completes `}`    // risky code

### Check for Updates

- Type `[` → Auto-completes `]`} catch (error) {

```bash

# Check current version- Type `(` → Auto-completes `)`    console.log(error);

code --list-extensions --show-versions | grep powerscript

- Type `"` → Auto-completes `"`}

# Output: saleemlewis.powerscript@1.0.0

```- Type `'` → Auto-completes `'````



### Update Extension



When new versions are released:**Auto-surrounding:**### Interface Snippet



1. Download new `.vsix` file- Select text and type `{` → Wraps in `{}````powerscript

2. Uninstall old version:

   ```bash- Select text and type `"` → Wraps in `""`// Type: interface + Tab

   code --uninstall-extension saleemlewis.powerscript

   ```interface InterfaceName {

3. Install new version:

   ```bash**Bracket colorization:**    property: type;

   code --install-extension powerscript-<new-version>.vsix

   ```- Nested brackets shown in different colors    method(param: type): returnType;



---- Easy to match opening/closing pairs}



## 🐛 Troubleshooting```



### Extension Not Loading## 🎯 Usage Tips



**Symptom:** No PowerScript in Extensions panel### Enum Snippet



**Solutions:**### Snippet Workflow```powerscript



1. Reload VS Code: `Cmd/Ctrl+Shift+P` → "Reload Window"// Type: enum + Tab

2. Check installation: View → Extensions → Search "PowerScript"

3. Reinstall from VSIX1. **Type snippet prefix** (e.g., `func`)enum EnumName {

4. Check VS Code version (1.60+ required)

2. **Press Tab** to expand    VALUE1 = "value1",

### No Syntax Highlighting

3. **Tab through placeholders** to fill in values    VALUE2 = "value2"

**Symptom:** `.ps` files show as plain text

4. **Press Enter** when done}

**Solutions:**

```

1. Check language mode (bottom right) - should show "PowerScript"

2. Manually set language: `Cmd/Ctrl+K M` → type "powerscript"### Example: Create a Class

3. Check file association in settings

4. Reload window### Switch Statement Snippet



### Snippets Not Working``````powerscript



**Symptom:** Typing `func` doesn't show snippet1. Type: class [Tab]// Type: switch + Tab



**Solutions:**2. Fill in: Personswitch (expression) {



1. Check suggestions enabled: Settings → Editor: Quick Suggestions3. Tab to param: name    case value1:

2. Press `Cmd+Space` (Mac) or `Ctrl+Space` (Windows/Linux) to trigger manually

3. Type snippet prefix and press `Tab` instead of `Enter`4. Tab to type: string        // code

4. Verify extension installed correctly

5. Tab to method: greet        break;

### Performance Issues

6. Tab to return type: string    case value2:

**Symptom:** VS Code slow with large `.ps` files

7. Done!        // code

**Solutions:**

```        break;

1. Increase memory limit: Settings → Files: Max Memory For Large File (MB)

2. Disable unused extensions    default:

3. Close other heavy files

4. Split large files into modulesResult:        // code



---```powerscript}



## 📚 Coming Soon 🔄class Person {```



Future extension features:    constructor(name: string) {



- 🔄 **LSP Integration** - Real-time error checking        // constructor body## Commands

- 🔄 **IntelliSense** - Smart code completion

- 🔄 **Go to Definition** - Jump to symbol definitions    }

- 🔄 **Find References** - Find all symbol usages

- 🔄 **Rename Refactoring** - Rename across files    Access via Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`):

- 🔄 **Code Actions** - Quick fixes and refactorings

- 🔄 **Debugging Support** - Step-through debugging    greet(): string {

- 🔄 **Test Explorer** - Run and view tests

        // method body### PowerScript: Compile File

---

    }- Compiles current `.ps` file to Python

## 🆘 Getting Help

}- Shortcut: `Ctrl+Shift+B` / `Cmd+Shift+B`

**Issues with Extension?**

```- Output: `.py` file in same directory

- Check **[FAQ](faq.md)** for common questions

- Report issue: [GitHub Issues](https://github.com/SaleemLww/Python-PowerScript/issues)

- Ask community: [GitHub Discussions](https://github.com/SaleemLww/Python-PowerScript/discussions)

### Keyboard Shortcuts### PowerScript: Run File

---

- Compiles and runs current file

**Extension installed? Start coding with [Quick Start](quickstart.md)! 🚀**

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
