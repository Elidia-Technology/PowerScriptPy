# 📦 Installation Guide# Installation Guide



Complete guide to installing PowerScript on any platform.This guide covers all the ways to install PowerScript on your system.



## 🎯 Prerequisites## Table of Contents

- [Prerequisites](#prerequisites)

- **Python 3.8+** (Python 3.9+ recommended)- [Installation Methods](#installation-methods)

- **pip** package manager- [PyPI Installation](#pypi-installation-recommended)

- **VS Code** (optional, for IDE support)- [Source Installation](#source-installation)

- [Development Installation](#development-installation)

## 🚀 Quick Install- [VS Code Extension](#vs-code-extension)

- [Verification](#verification)

### Option 1: Install from PyPI (Recommended)- [Troubleshooting](#troubleshooting)



```bash## Prerequisites

# Install TPS globally

pip install tps### System Requirements

- **Python**: 3.8 or higher

# Verify installation- **pip**: Latest version recommended

tps --version- **OS**: Windows, macOS, Linux

```

### Check Your Python Version

### Option 2: Install from Source

```bash

```bashpython --version

# Clone repository# or

git clone https://github.com/SaleemLww/Python-PowerScript.gitpython3 --version

cd Python-PowerScript```



# Create virtual environment (recommended)If you need to install Python, visit [python.org](https://www.python.org/downloads/).

python -m venv .venv

source .venv/bin/activate  # On Windows: .venv\Scripts\activate## Installation Methods



# Install in development modePowerScript can be installed in three ways:

pip install -e .

1. **PyPI Installation** (Recommended) - For end users

# Verify installation2. **Source Installation** - For advanced users

tps --version3. **Development Installation** - For contributors

```

## PyPI Installation (Recommended)

## 📦 Installation Methods

The easiest way to install PowerScript is from PyPI:

### 1. Global Installation

```bash

Install TPS system-wide for all projects:# Install TPS (Typed PowerScript)

pip install tps

```bash

pip install tps# Or with Python 3 explicitly

```pip3 install tps

```

**Pros:**

- Available everywhere### Verify Installation

- Simple to use

- No project setup needed```bash

# Check version

**Cons:**tps --version

- Version conflicts possible

- Requires admin rights# Check installed commands

tps --help

### 2. Virtual Environment (Recommended)tps-compile --help

tps-run --help

Install TPS in a project-specific environment:tps-create --help

```

```bash

# Create virtual environment### What Gets Installed?

python -m venv myproject_env

When you install TPS, you get:

# Activate it- `tps` - Main CLI tool

source myproject_env/bin/activate  # macOS/Linux- `tps-compile` - PowerScript compiler

myproject_env\Scripts\activate     # Windows- `tps-run` - Direct file execution

- `tps-create` - Project scaffolding

# Install TPS- `powerscript` - Python package

pip install tps- All runtime libraries

```

## Source Installation

**Pros:**

- Isolated dependencies### Clone the Repository

- Multiple TPS versions

- No admin rights needed```bash

# Clone from GitHub

**Cons:**git clone https://github.com/SaleemLww/Python-PowerScript.git

- Must activate before usecd Python-PowerScript

- Per-project setup```



### 3. Development Installation### Install Dependencies



For contributing or testing:```bash

# Create virtual environment (optional but recommended)

```bashpython -m venv .venv

# Clone and install editablysource .venv/bin/activate  # On Windows: .venv\Scripts\activate

git clone https://github.com/SaleemLww/Python-PowerScript.git

cd Python-PowerScript# Install requirements

pip install -e ".[dev]"pip install -r requirements.txt

``````



## 🖥️ Platform-Specific Instructions### Install PowerScript



### macOS```bash

# Install in user mode

```bashpip install .

# Install Python 3.9+ via Homebrew

brew install python@3.9# Or install globally (may require sudo/admin)

sudo pip install .

# Install TPS```

pip3 install tps

### Make CLI Tools Executable (Optional)

# Add to PATH if needed

echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc```bash

source ~/.zshrc# On Linux/macOS

```chmod +x bin/*



### Linux (Ubuntu/Debian)# Add to PATH (optional)

export PATH="$PATH:$(pwd)/bin"

```bash```

# Install Python 3.9+

sudo apt update## Development Installation

sudo apt install python3.9 python3.9-pip python3.9-venv

For contributors who want to modify PowerScript:

# Install TPS

pip3 install tps```bash

# Clone the repository

# Add to PATH if neededgit clone https://github.com/SaleemLww/Python-PowerScript.git

echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrccd Python-PowerScript

source ~/.bashrc

```# Create virtual environment

python -m venv .venv

### Windowssource .venv/bin/activate  # On Windows: .venv\Scripts\activate



```powershell# Install in editable mode

# Install Python from python.org or Microsoft Storepip install -e .



# Install TPS# Install development dependencies

pip install tpspip install pytest black flake8 mypy

```

# Add to PATH (usually automatic)

# If needed, add: C:\Users\<YourName>\AppData\Local\Programs\Python\Python39\Scripts### Development Setup

```

```bash

## 🔧 VS Code Extension# Run tests

pytest

### Install from VSIX

# Format code

1. **Download Extension**black powerscript/

   ```bash

   # From PowerScript repo# Lint code

   cd vscode-extensionflake8 powerscript/

   # powerscript-1.0.0.vsix is included

   ```# Type check

mypy powerscript/

2. **Install in VS Code**```

   - Open VS Code

   - Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)## VS Code Extension

   - Type "Extensions: Install from VSIX"

   - Select `powerscript-1.0.0.vsix`PowerScript has a full-featured VS Code extension with LSP support!



3. **Verify Installation**### Installation from GitHub

   - Create a file: `test.ps`

   - Should see syntax highlighting1. **Download the Extension**

   - Visit: [https://github.com/SaleemLww/Python-PowerScript](https://github.com/SaleemLww/Python-PowerScript)

### Build from Source   - Navigate to the `vscode-extension/` folder

   - Download the `.vsix` file (or clone the repo)

```bash

cd vscode-extension2. **Build the Extension** (if cloning)

   ```bash

# Install dependencies   cd Python-PowerScript/vscode-extension

npm install   npm install

   npm run compile

# Compile TypeScript   npx vsce package

npm run compile   ```



# Package extension3. **Install in VS Code**

vsce package   ```bash

   code --install-extension powerscript-1.0.0.vsix

# Install the generated .vsix   ```

code --install-extension powerscript-1.0.0.vsix

```4. **Or Install via VS Code**

   - Open VS Code

## ✅ Verify Installation   - Press `Ctrl+Shift+P` (Cmd+Shift+P on Mac)

   - Type: "Install from VSIX"

### Check TPS Version   - Select the `.vsix` file



```bash5. **Restart VS Code**

tps --version   - Close and reopen VS Code to activate the extension

# Output: TPS 1.0.0b1

```### Extension Features



### Run Test Program- ✅ Syntax highlighting for `.ps` files

- ✅ Code snippets (function, class, async, arrow, etc.)

Create `hello.ps`:- ✅ IntelliSense and auto-completion

- ✅ Error diagnostics

```powerscript- ✅ Hover information

function main(): void {- ✅ Commands (Compile, Run, Create Project)

    console.log("Hello, PowerScript!");- ✅ Keyboard shortcuts (Ctrl+Shift+B, Ctrl+Shift+R)

}

```See [VS Code Extension Guide](vscode_extension.md) for detailed usage.



Compile and run:## Verification



```bash### Test Your Installation

tps-compile hello.ps

python hello.pyCreate a test file `hello.ps`:

```

```powerscript

### Check CLI Tools// hello.ps

console.log("Hello, PowerScript!");

```bash

# All commands should workfunction greet(name: string): string {

tps-compile --help    return f"Hello, {name}!";

tps-run --help}

tps-create --help

tps-check --helplet message = greet("World");

```console.log(message);

```

## 🔍 Troubleshooting

### Compile and Run

### Command Not Found

```bash

**Symptom:** `tps: command not found`# Compile to Python

tps-compile hello.ps

**Solutions:**

1. Ensure pip install completed successfully# Run directly

2. Add pip scripts to PATH:tps-run hello.ps

   ```bash

   # macOS/Linux# Or compile then run

   export PATH="$HOME/.local/bin:$PATH"tps-compile hello.ps -o hello.py

   python hello.py

   # Windows```

   # Add to System PATH: %USERPROFILE%\AppData\Local\Programs\Python\Python39\Scripts

   ```### Expected Output

3. Use full path: `python -m powerscript.cli.cli --version`

```

### Import ErrorsHello, PowerScript!

Hello, World!

**Symptom:** `ModuleNotFoundError: No module named 'powerscript'````



**Solutions:**## Platform-Specific Notes

1. Activate virtual environment if used

2. Reinstall TPS: `pip install --force-reinstall tps`### Windows

3. Check Python version: `python --version` (must be 3.8+)

```bash

### VS Code Extension Not Working# Use Python 3 explicitly

py -3 -m pip install tps

**Symptom:** No syntax highlighting for `.ps` files

# Verify installation

**Solutions:**py -3 -m tps --version

1. Reload VS Code: `Cmd/Ctrl + Shift + P` → "Reload Window"

2. Check extension installed: View → Extensions → Search "PowerScript"# Run PowerScript files

3. Reinstall extension from VSIXpy -3 -m tps run hello.ps

4. Check file association: `.ps` files should use PowerScript language```



### Permission Denied### macOS



**Symptom:** `Permission denied` during installation```bash

# Install with pip3

**Solutions:**pip3 install tps

1. Use `pip install --user tps` instead of global install

2. Use virtual environment (recommended)# If command not found, check PATH

3. On Linux/macOS: Use `sudo pip install tps` (not recommended)export PATH="$HOME/Library/Python/3.x/bin:$PATH"



## 🔄 Updating TPS# Add to ~/.zshrc for persistence

echo 'export PATH="$HOME/Library/Python/3.x/bin:$PATH"' >> ~/.zshrc

### Update from PyPI```



```bash### Linux

pip install --upgrade tps

``````bash

# Install with pip3

### Update from Sourcepip3 install tps



```bash# If permission denied

cd Python-PowerScriptpip3 install --user tps

git pull

pip install --upgrade -e .# Add to PATH if needed

```export PATH="$HOME/.local/bin:$PATH"



## 🗑️ Uninstalling# Add to ~/.bashrc for persistence

echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

### Remove TPS```



```bash## Troubleshooting

pip uninstall tps

```### Command Not Found



### Remove VS Code ExtensionIf `tps` command is not found after installation:



```bash```bash

code --uninstall-extension saleemlewis.powerscript# Find where pip installed the package

```pip show tps



## 📋 System Requirements# Check if scripts directory is in PATH

echo $PATH  # Linux/macOS

### Minimumecho %PATH%  # Windows

- **OS:** Windows 7+, macOS 10.12+, Linux (any modern distro)

- **Python:** 3.8+# Add to PATH (example for Linux/macOS)

- **RAM:** 512 MBexport PATH="$HOME/.local/bin:$PATH"

- **Disk:** 50 MB```



### Recommended### Permission Denied

- **OS:** Windows 10+, macOS 11+, Ubuntu 20.04+

- **Python:** 3.9+```bash

- **RAM:** 2 GB# Install for current user only

- **Disk:** 200 MBpip install --user tps

- **IDE:** VS Code with PowerScript extension

# Or use virtual environment

## 🎓 Next Stepspython -m venv myenv

source myenv/bin/activate

After installation:pip install tps

```

1. **[Quick Start Guide](quickstart.md)** - Your first program in 5 minutes

2. **[VS Code Extension Guide](vscode_extension.md)** - Setup your IDE### Module Not Found

3. **[Tutorial](tutorial.md)** - Learn PowerScript step by step

```bash

## 🆘 Getting Help# Reinstall dependencies

pip install --upgrade tps

- **Issues:** [GitHub Issues](https://github.com/SaleemLww/Python-PowerScript/issues)

- **Discussions:** [GitHub Discussions](https://github.com/SaleemLww/Python-PowerScript/discussions)# Or install from source

- **Docs:** [Documentation](README.md)pip uninstall tps

pip install git+https://github.com/SaleemLww/Python-PowerScript.git

---```



**Installation successful? Start coding with [Quick Start](quickstart.md)! 🚀**### Python Version Issues


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
