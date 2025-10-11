# 📦 Installation Guide# 📦 Installation Guide



Complete guide to installing PowerScript (TPS) on any platform.Complete guide to installing PowerScript on any platform.



---## 🎯 Prerequisites



## 🎯 Prerequisites- **Python 3.8+** (Python 3.9+ recommended)

- **pip** package manager

- **Python 3.8+** (Python 3.9+ recommended)- **VS Code** (optional, for IDE support)

- **pip** package manager

- **VS Code** (optional, for IDE support)## 🚀 Quick Install



---### Option 1: Install from PyPI (Recommended)



## 🚀 Quick Install\```bash

# Install TPS globally

### Option 1: Install from PyPI (Recommended)pip install tps



```bash# Verify installation

# Install TPS globallytps --version

pip install tps\```



# Verify installation### Option 2: Install from Source

tps --version

```\```bash

# Clone repository

### Option 2: Install from Sourcegit clone https://github.com/SaleemLww/Python-PowerScript.git

cd Python-PowerScript

```bash

# Clone repository# Create virtual environment (recommended)

git clone https://github.com/SaleemLww/Python-PowerScript.gitpython -m venv .venv

cd Python-PowerScriptsource .venv/bin/activate  # On Windows: .venv\Scripts\activate



# Create virtual environment (recommended)# Install in development mode

python -m venv .venvpip install -e .

source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Verify installation

# Install in development modetps --version

pip install -e .\```



# Verify installation## 📦 Installation Methods

tps --version

```### 1. Global Installation



---Install TPS system-wide for all projects:



## 📦 Installation Methods\```bash

pip install tps

### 1. Global Installation\```



Install TPS system-wide for all projects:**Pros:**

- Available everywhere

```bash- Simple to use

pip install tps- No project setup needed

```

**Cons:**

**Pros:**- Version conflicts possible

- ✅ Available everywhere- Requires admin rights

- ✅ Simple to use

- ✅ No project setup needed### 2. Virtual Environment (Recommended)



**Cons:**Install TPS in a project-specific environment:

- ⚠️ Version conflicts possible

- ⚠️ May require admin rights\```bash

# Create virtual environment

### 2. Virtual Environment (Recommended)python -m venv myproject_env



Install TPS in a project-specific environment:# Activate it

source myproject_env/bin/activate  # macOS/Linux

```bashmyproject_env\Scripts\activate     # Windows

# Create virtual environment

python -m venv myproject_env# Install TPS

pip install tps

# Activate it\```

source myproject_env/bin/activate  # macOS/Linux

myproject_env\Scripts\activate     # Windows**Pros:**

- Isolated dependencies

# Install TPS- Multiple TPS versions

pip install tps- No admin rights needed

```

**Cons:**

**Pros:**- Must activate before use

- ✅ Isolated dependencies- Per-project setup

- ✅ Multiple TPS versions possible

- ✅ No admin rights needed## 🖥️ Platform-Specific Instructions



**Cons:**### macOS

- ⚠️ Must activate before use

- ⚠️ Per-project setup required\```bash

# Install Python 3.9+ via Homebrew

### 3. Development Installationbrew install python@3.9



For contributing or testing:# Install TPS

pip3 install tps

```bash

# Clone and install editably# Add to PATH if needed

git clone https://github.com/SaleemLww/Python-PowerScript.gitecho 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc

cd Python-PowerScriptsource ~/.zshrc

pip install -e ".[dev]"\```

```

### Linux (Ubuntu/Debian)

---

\```bash

## 🖥️ Platform-Specific Instructions# Install Python 3.9+

sudo apt update

### macOSsudo apt install python3.9 python3.9-pip python3.9-venv



```bash# Install TPS

# Install Python 3.9+ via Homebrewpip3 install tps

brew install python@3.9

# Add to PATH if needed

# Install TPSecho 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

pip3 install tpssource ~/.bashrc

\```

# Add to PATH if needed

echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc### Windows

source ~/.zshrc

```\```powershell

# Install Python from python.org or Microsoft Store

### Linux (Ubuntu/Debian)

# Install TPS

```bashpip install tps

# Install Python 3.9+\```

sudo apt update

sudo apt install python3.9 python3.9-pip python3.9-venv## 🔧 VS Code Extension



# Install TPS### Install from VSIX

pip3 install tps

1. **Download Extension**

# Add to PATH if needed   \```bash

echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc   # From PowerScript repo

source ~/.bashrc   cd vscode-extension

```   # powerscript-1.0.0.vsix is included

   \```

### Windows

2. **Install in VS Code**

```powershell   - Open VS Code

# Install Python from python.org or Microsoft Store   - Press Cmd+Shift+P (Mac) or Ctrl+Shift+P (Windows/Linux)

   - Type "Extensions: Install from VSIX"

# Install TPS   - Select powerscript-1.0.0.vsix

pip install tps

3. **Verify Installation**

# Add to PATH (usually automatic)   - Create a file: test.ps

# If needed, add: C:\Users\<YourName>\AppData\Local\Programs\Python\Python39\Scripts   - Should see syntax highlighting

```

## ✅ Verify Installation

---

### Check TPS Version

## 🔧 VS Code Extension

\```bash

### Install from VSIXtps --version

# Output: TPS 1.0.0b1

1. **Locate Extension File**\```

   ```bash

   cd Python-PowerScript/vscode-extension### Run Test Program

   # File: powerscript-1.0.0.vsix

   ```Create hello.ps:



2. **Install in VS Code**\```powerscript

   - Open VS Codefunction main(): void {

   - Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)    console.log("Hello, PowerScript!");

   - Type: "Extensions: Install from VSIX"}

   - Select `powerscript-1.0.0.vsix`\```



3. **Verify Installation**Compile and run:

   - Create file: `test.ps`

   - Should see syntax highlighting\```bash

   - Check Extensions panel for "PowerScript"tps-compile hello.ps

python hello.py

### Build from Source\```



```bash### Check CLI Tools

cd vscode-extension

\```bash

# Install dependencies# All commands should work

npm installtps-compile --help

tps-run --help

# Compile TypeScripttps-create --help

npm run compiletps-check --help

\```

# Package extension

npm install -g vsce## 🔍 Troubleshooting

vsce package

### Command Not Found

# Install the generated .vsix

code --install-extension powerscript-1.0.0.vsix**Symptom:** tps: command not found

```

**Solutions:**

---1. Ensure pip install completed successfully

2. Add pip scripts to PATH

## ✅ Verify Installation3. Use full path: python -m powerscript.cli.cli --version



### Check TPS Version### Import Errors



```bash**Symptom:** ModuleNotFoundError: No module named 'powerscript'

tps --version

# Output: TPS 1.0.0b1**Solutions:**

```1. Activate virtual environment if used

2. Reinstall TPS: pip install --force-reinstall tps

### Run Test Program3. Check Python version: python --version (must be 3.8+)



Create `hello.ps`:### VS Code Extension Not Working



```powerscript**Symptom:** No syntax highlighting for .ps files

function main(): void {

    console.log("Hello, PowerScript!");**Solutions:**

}1. Reload VS Code: Cmd/Ctrl + Shift + P → "Reload Window"

```2. Check extension installed: View → Extensions → Search "PowerScript"

3. Reinstall extension from VSIX

Compile and run:

## 🔄 Updating TPS

```bash

tps-compile hello.ps### Update from PyPI

python hello.py

# Output: Hello, PowerScript!\```bash

```pip install --upgrade tps

\```

### Check CLI Tools

### Update from Source

```bash

# All commands should work\```bash

tps-compile --helpcd Python-PowerScript

tps-run --helpgit pull

tps-create --helppip install --upgrade -e .

tps-check --help\```

```

## 🗑️ Uninstalling

---

### Remove TPS

## 🔍 Troubleshooting

\```bash

### Command Not Foundpip uninstall tps

\```

**Symptom:** `tps: command not found`

### Remove VS Code Extension

**Solutions:**

\```bash

1. Ensure pip install completed successfullycode --uninstall-extension saleemlewis.powerscript

2. Add pip scripts to PATH:\```

   ```bash

   # macOS/Linux## 📋 System Requirements

   export PATH="$HOME/.local/bin:$PATH"

   ### Minimum

   # Windows - Add to System PATH:- **OS:** Windows 7+, macOS 10.12+, Linux (any modern distro)

   # %USERPROFILE%\AppData\Local\Programs\Python\Python39\Scripts- **Python:** 3.8+

   ```- **RAM:** 512 MB

3. Use full path: `python -m powerscript.cli.cli --version`- **Disk:** 50 MB



### Import Errors### Recommended

- **OS:** Windows 10+, macOS 11+, Ubuntu 20.04+

**Symptom:** `ModuleNotFoundError: No module named 'powerscript'`- **Python:** 3.9+

- **RAM:** 2 GB

**Solutions:**- **Disk:** 200 MB

- **IDE:** VS Code with PowerScript extension

1. Activate virtual environment if used

2. Reinstall TPS: `pip install --force-reinstall tps`## 🎓 Next Steps

3. Check Python version: `python --version` (must be 3.8+)

After installation:

### VS Code Extension Not Working

1. **[Quick Start Guide](quickstart.md)** - Your first program in 5 minutes

**Symptom:** No syntax highlighting for `.ps` files2. **[VS Code Extension Guide](vscode_extension.md)** - Setup your IDE

3. **[CLI Reference](cli_reference.md)** - Learn command-line tools

**Solutions:**

## 🆘 Getting Help

1. Reload VS Code: `Cmd/Ctrl + Shift + P` → "Reload Window"

2. Check extension installed: View → Extensions → Search "PowerScript"- **Issues:** [GitHub Issues](https://github.com/SaleemLww/Python-PowerScript/issues)

3. Reinstall extension from VSIX- **Discussions:** [GitHub Discussions](https://github.com/SaleemLww/Python-PowerScript/discussions)

4. Check file association: `.ps` files should use PowerScript language- **Docs:** [Documentation](README.md)



### Permission Denied---



**Symptom:** `Permission denied` during installation**Installation successful? Start coding with [Quick Start](quickstart.md)! 🚀**


**Solutions:**

1. Use `pip install --user tps` instead of global install
2. Use virtual environment (recommended)
3. On Linux/macOS: Use `sudo pip install tps` (not recommended)

---

## 🔄 Updating TPS

### Update from PyPI

```bash
pip install --upgrade tps
```

### Update from Source

```bash
cd Python-PowerScript
git pull
pip install --upgrade -e .
```

---

## 🗑️ Uninstalling

### Remove TPS

```bash
pip uninstall tps
```

### Remove VS Code Extension

```bash
code --uninstall-extension saleemlewis.powerscript
```

---

## 📋 System Requirements

### Minimum

- **OS:** Windows 7+, macOS 10.12+, Linux (any modern distro)
- **Python:** 3.8+
- **RAM:** 512 MB
- **Disk:** 50 MB

### Recommended

- **OS:** Windows 10+, macOS 11+, Ubuntu 20.04+
- **Python:** 3.9+
- **RAM:** 2 GB
- **Disk:** 200 MB
- **IDE:** VS Code with PowerScript extension

---

## 🎓 Next Steps

After installation:

1. **[Quick Start Guide](quickstart.md)** - Your first program in 5 minutes
2. **[CLI Reference](cli_reference.md)** - Learn the command-line tools
3. **[VS Code Extension Guide](vscode_extension.md)** - Setup your IDE

---

## 🆘 Getting Help

- **Issues:** [GitHub Issues](https://github.com/SaleemLww/Python-PowerScript/issues)
- **Discussions:** [GitHub Discussions](https://github.com/SaleemLww/Python-PowerScript/discussions)
- **Documentation:** [Main Docs](README.md)

---

**Installation successful? Start coding with [Quick Start](quickstart.md)! 🚀**
