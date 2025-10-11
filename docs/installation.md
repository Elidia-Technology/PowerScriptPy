# Installation Guide

This guide covers all the ways to install PowerScript on your system.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation Methods](#installation-methods)
- [PyPI Installation](#pypi-installation-recommended)
- [Source Installation](#source-installation)
- [Development Installation](#development-installation)
- [VS Code Extension](#vs-code-extension)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

## Prerequisites

### System Requirements
- **Python**: 3.8 or higher
- **pip**: Latest version recommended
- **OS**: Windows, macOS, Linux

### Check Your Python Version

```bash
python --version
# or
python3 --version
```

If you need to install Python, visit [python.org](https://www.python.org/downloads/).

## Installation Methods

PowerScript can be installed in three ways:

1. **PyPI Installation** (Recommended) - For end users
2. **Source Installation** - For advanced users
3. **Development Installation** - For contributors

## PyPI Installation (Recommended)

The easiest way to install PowerScript is from PyPI:

```bash
# Install TPS (Typed PowerScript)
pip install tps

# Or with Python 3 explicitly
pip3 install tps
```

### Verify Installation

```bash
# Check version
tps --version

# Check installed commands
tps --help
tps-compile --help
tps-run --help
tps-create --help
```

### What Gets Installed?

When you install TPS, you get:
- `tps` - Main CLI tool
- `tps-compile` - PowerScript compiler
- `tps-run` - Direct file execution
- `tps-create` - Project scaffolding
- `powerscript` - Python package
- All runtime libraries

## Source Installation

### Clone the Repository

```bash
# Clone from GitHub
git clone https://github.com/SaleemLww/Python-PowerScript.git
cd Python-PowerScript
```

### Install Dependencies

```bash
# Create virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### Install PowerScript

```bash
# Install in user mode
pip install .

# Or install globally (may require sudo/admin)
sudo pip install .
```

### Make CLI Tools Executable (Optional)

```bash
# On Linux/macOS
chmod +x bin/*

# Add to PATH (optional)
export PATH="$PATH:$(pwd)/bin"
```

## Development Installation

For contributors who want to modify PowerScript:

```bash
# Clone the repository
git clone https://github.com/SaleemLww/Python-PowerScript.git
cd Python-PowerScript

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in editable mode
pip install -e .

# Install development dependencies
pip install pytest black flake8 mypy
```

### Development Setup

```bash
# Run tests
pytest

# Format code
black powerscript/

# Lint code
flake8 powerscript/

# Type check
mypy powerscript/
```

## VS Code Extension

PowerScript has a full-featured VS Code extension with LSP support!

### Installation from GitHub

1. **Download the Extension**
   - Visit: [https://github.com/SaleemLww/Python-PowerScript](https://github.com/SaleemLww/Python-PowerScript)
   - Navigate to the `vscode-extension/` folder
   - Download the `.vsix` file (or clone the repo)

2. **Build the Extension** (if cloning)
   ```bash
   cd Python-PowerScript/vscode-extension
   npm install
   npm run compile
   npx vsce package
   ```

3. **Install in VS Code**
   ```bash
   code --install-extension powerscript-1.0.0.vsix
   ```

4. **Or Install via VS Code**
   - Open VS Code
   - Press `Ctrl+Shift+P` (Cmd+Shift+P on Mac)
   - Type: "Install from VSIX"
   - Select the `.vsix` file

5. **Restart VS Code**
   - Close and reopen VS Code to activate the extension

### Extension Features

- ✅ Syntax highlighting for `.ps` files
- ✅ Code snippets (function, class, async, arrow, etc.)
- ✅ IntelliSense and auto-completion
- ✅ Error diagnostics
- ✅ Hover information
- ✅ Commands (Compile, Run, Create Project)
- ✅ Keyboard shortcuts (Ctrl+Shift+B, Ctrl+Shift+R)

See [VS Code Extension Guide](vscode_extension.md) for detailed usage.

## Verification

### Test Your Installation

Create a test file `hello.ps`:

```powerscript
// hello.ps
console.log("Hello, PowerScript!");

function greet(name: string): string {
    return f"Hello, {name}!";
}

let message = greet("World");
console.log(message);
```

### Compile and Run

```bash
# Compile to Python
tps-compile hello.ps

# Run directly
tps-run hello.ps

# Or compile then run
tps-compile hello.ps -o hello.py
python hello.py
```

### Expected Output

```
Hello, PowerScript!
Hello, World!
```

## Platform-Specific Notes

### Windows

```bash
# Use Python 3 explicitly
py -3 -m pip install tps

# Verify installation
py -3 -m tps --version

# Run PowerScript files
py -3 -m tps run hello.ps
```

### macOS

```bash
# Install with pip3
pip3 install tps

# If command not found, check PATH
export PATH="$HOME/Library/Python/3.x/bin:$PATH"

# Add to ~/.zshrc for persistence
echo 'export PATH="$HOME/Library/Python/3.x/bin:$PATH"' >> ~/.zshrc
```

### Linux

```bash
# Install with pip3
pip3 install tps

# If permission denied
pip3 install --user tps

# Add to PATH if needed
export PATH="$HOME/.local/bin:$PATH"

# Add to ~/.bashrc for persistence
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

## Troubleshooting

### Command Not Found

If `tps` command is not found after installation:

```bash
# Find where pip installed the package
pip show tps

# Check if scripts directory is in PATH
echo $PATH  # Linux/macOS
echo %PATH%  # Windows

# Add to PATH (example for Linux/macOS)
export PATH="$HOME/.local/bin:$PATH"
```

### Permission Denied

```bash
# Install for current user only
pip install --user tps

# Or use virtual environment
python -m venv myenv
source myenv/bin/activate
pip install tps
```

### Module Not Found

```bash
# Reinstall dependencies
pip install --upgrade tps

# Or install from source
pip uninstall tps
pip install git+https://github.com/SaleemLww/Python-PowerScript.git
```

### Python Version Issues

```bash
# Use specific Python version
python3.9 -m pip install tps
python3.10 -m pip install tps

# Create virtual environment with specific version
python3.9 -m venv .venv
source .venv/bin/activate
pip install tps
```

## Upgrading PowerScript

### Upgrade from PyPI

```bash
# Upgrade to latest version
pip install --upgrade tps

# Check new version
tps --version
```

### Upgrade from Source

```bash
# Pull latest changes
cd Python-PowerScript
git pull origin master

# Reinstall
pip install --upgrade .
```

## Uninstalling

```bash
# Uninstall PowerScript
pip uninstall tps

# Remove virtual environment (if used)
rm -rf .venv
```

## Next Steps

Now that PowerScript is installed:

1. ✅ Follow the [Quick Start Guide](quickstart.md)
2. ✅ Read the [Language Reference](language_reference.md)
3. ✅ Install the [VS Code Extension](vscode_extension.md)
4. ✅ Build your first project!

---

**Need help?** Check the [Troubleshooting Guide](troubleshooting.md) or open an issue on [GitHub](https://github.com/SaleemLww/Python-PowerScript/issues).
