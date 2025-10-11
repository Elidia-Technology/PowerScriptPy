# PowerScript VS Code Extension

A comprehensive VS Code extension that provides full IDE support for the PowerScript programming language.

## Features

### 🎨 Syntax Highlighting
- Complete TextMate grammar support for PowerScript syntax
- Highlighting for keywords, types, strings, comments, and operators
- Support for modern language features like F-strings and template literals

### 📝 Code Snippets
Ready-to-use code templates for faster development:
- `class` - Class definition
- `constructor` - Constructor method
- `function` - Function definition
- `arrow` - Arrow function
- `async` - Async function
- `if` - If statement
- `for` - For loop
- `while` - While loop
- `try` - Try-catch block
- `switch` - Switch statement
- `import` - Import statement
- `fstring` - F-string template
- `template` - Template literal

### 🔧 Language Server Protocol (LSP)
- **Auto-completion**: IntelliSense for keywords, types, and user-defined symbols
- **Hover information**: Documentation and type information on hover
- **Diagnostics**: Real-time syntax and type error detection
- **Go-to-definition**: Navigate to symbol definitions (planned)

### ⚡ Commands
- `PowerScript: Compile File` - Compile current PowerScript file
- `PowerScript: Run File` - Run current PowerScript file  
- `PowerScript: Create Project` - Create new PowerScript project

### 🐛 Debugging (Planned)
- Integration with Python debugger for compiled PowerScript code
- Breakpoint support
- Variable inspection
- Step-through debugging

## Installation

### From VSIX Package
1. Download the `powerscript-1.0.0.vsix` file
2. Open VS Code
3. Go to Extensions view (`Ctrl+Shift+X`)
4. Click the "..." menu and select "Install from VSIX..."
5. Select the downloaded `.vsix` file

### From Command Line
```bash
code --install-extension powerscript-1.0.0.vsix
```

## Usage

### Basic Usage
1. Create or open a `.ps` file
2. The extension will automatically activate and provide syntax highlighting
3. Use snippets by typing trigger words (e.g., `class`, `function`) and pressing Tab
4. Right-click in editor for compile/run options

### Keyboard Shortcuts
- `Ctrl+Shift+B` / `Cmd+Shift+B` - Compile current file
- `Ctrl+Shift+R` / `Cmd+Shift+R` - Run current file

### Configuration
The extension supports the following settings:

```json
{
    "powerscript.enableLSP": true,
    "powerscript.enableDiagnostics": true,
    "powerscript.compilerPath": "powerscriptc",
    "powerscript.pythonPath": "python3"
}
```

## PowerScript Language Features

### Class Definitions
```powerscript
class Person {
    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
    
    greet(): string {
        return f"Hello, I'm {this.name}";
    }
}
```

### Functions and Arrow Functions
```powerscript
function add(a: number, b: number): number {
    return a + b;
}

const multiply = (a: number, b: number): number => a * b;
```

### Async/Await
```powerscript
async function fetchData(url: string): Hello {
    const response = await fetch(url);
    return await response.json();
}
```

### Modern String Features
```powerscript
let name = "PowerScript";
let version = "1.0";

// F-strings
let message = f"Welcome to {name} v{version}!";

// Template literals
let template = `
    Language: ${name}
    Version: ${version}
    Status: Ready
`;
```

## Requirements

- VS Code 1.60.0 or higher
- PowerScript compiler (`powerscriptc`) installed and in PATH
- Python 3.x for running compiled code

## Development

### Building from Source
1. Clone the repository
2. Install dependencies: `npm install`
3. Compile TypeScript: `npm run compile`
4. Package extension: `vsce package`
5. Install: `code --install-extension powerscript-1.0.0.vsix`

### Project Structure
```
vscode-extension/
├── src/
│   ├── extension.ts          # Main extension entry point
│   ├── lsp-server.py        # Language Server Protocol implementation
│   └── extension-simple.ts  # Simplified extension version
├── syntaxes/
│   └── powerscript.tmLanguage.json  # TextMate grammar
├── snippets/
│   └── powerscript.json     # Code snippets
├── language-configuration.json     # Language configuration
├── package.json             # Extension manifest
└── tsconfig.json           # TypeScript configuration
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License

Copyright (c) 2025 Saleem Ahmad (Elite India Org Team)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

**Author**: Saleem Ahmad (Elite India Org Team)  
**Email**: team@eliteindia.org

## Support

For issues, feature requests, or questions:
- Create an issue on GitHub
- Check the PowerScript documentation
- Join the community discussions

## Changelog

### 1.0.0
- Initial release
- Complete syntax highlighting
- Code snippets
- Basic LSP support
- Compile and run commands
- Diagnostics and error detection

## Roadmap

- [ ] Enhanced LSP features (go-to-definition, find references)
- [ ] Integrated debugging support
- [ ] Code formatting and linting
- [ ] Project templates and scaffolding
- [ ] IntelliSense improvements
- [ ] Symbol outline and navigation
- [ ] Refactoring tools