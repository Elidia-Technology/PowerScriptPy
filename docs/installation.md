# 📦 Installation Guide

Complete guide to installing PowerScript on any platform.

## 🎯 Prerequisites

- **Python 3.8+** (Python 3.9+ recommended)
- **pip** package manager
- **VS Code** (optional, for IDE support)

## 🚀 Quick Install

### Option 1: Install from PyPI (Recommended)

\```bash
# Install TPS globally
pip install tps

# Verify installation
tps --version
\```

### Option 2: Install from Source

\```bash
# Clone repository
git clone https://github.com/SaleemLww/Python-PowerScript.git
cd Python-PowerScript

# Create virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode
pip install -e .

# Verify installation
tps --version
\```

## 📦 Installation Methods

### 1. Global Installation

Install TPS system-wide for all projects:

\```bash
pip install tps
\```

**Pros:**
- Available everywhere
- Simple to use
- No project setup needed

**Cons:**
- Version conflicts possible
- Requires admin rights

### 2. Virtual Environment (Recommended)

Install TPS in a project-specific environment:

\```bash
# Create virtual environment
python -m venv myproject_env

# Activate it
source myproject_env/bin/activate  # macOS/Linux
myproject_env\Scripts\activate     # Windows

# Install TPS
pip install tps
\```

**Pros:**
- Isolated dependencies
- Multiple TPS versions
- No admin rights needed

**Cons:**
- Must activate before use
- Per-project setup

## 🖥️ Platform-Specific Instructions

### macOS

\```bash
# Install Python 3.9+ via Homebrew
brew install python@3.9

# Install TPS
pip3 install tps

# Add to PATH if needed
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
\```

### Linux (Ubuntu/Debian)

\```bash
# Install Python 3.9+
sudo apt update
sudo apt install python3.9 python3.9-pip python3.9-venv

# Install TPS
pip3 install tps

# Add to PATH if needed
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
\```

### Windows

\```powershell
# Install Python from python.org or Microsoft Store

# Install TPS
pip install tps
\```

## 🔧 VS Code Extension

### Install from VSIX

1. **Download Extension**
   \```bash
   # From PowerScript repo
   cd vscode-extension
   # powerscript-1.0.0.vsix is included
   \```

2. **Install in VS Code**
   - Open VS Code
   - Press Cmd+Shift+P (Mac) or Ctrl+Shift+P (Windows/Linux)
   - Type "Extensions: Install from VSIX"
   - Select powerscript-1.0.0.vsix

3. **Verify Installation**
   - Create a file: test.ps
   - Should see syntax highlighting

## ✅ Verify Installation

### Check TPS Version

\```bash
tps --version
# Output: TPS 1.0.0b1
\```

### Run Test Program

Create hello.ps:

\```powerscript
function main(): void {
    console.log("Hello, PowerScript!");
}
\```

Compile and run:

\```bash
tps-compile hello.ps
python hello.py
\```

### Check CLI Tools

\```bash
# All commands should work
tps-compile --help
tps-run --help
tps-create --help
tps-check --help
\```

## 🔍 Troubleshooting

### Command Not Found

**Symptom:** tps: command not found

**Solutions:**
1. Ensure pip install completed successfully
2. Add pip scripts to PATH
3. Use full path: python -m powerscript.cli.cli --version

### Import Errors

**Symptom:** ModuleNotFoundError: No module named 'powerscript'

**Solutions:**
1. Activate virtual environment if used
2. Reinstall TPS: pip install --force-reinstall tps
3. Check Python version: python --version (must be 3.8+)

### VS Code Extension Not Working

**Symptom:** No syntax highlighting for .ps files

**Solutions:**
1. Reload VS Code: Cmd/Ctrl + Shift + P → "Reload Window"
2. Check extension installed: View → Extensions → Search "PowerScript"
3. Reinstall extension from VSIX

## 🔄 Updating TPS

### Update from PyPI

\```bash
pip install --upgrade tps
\```

### Update from Source

\```bash
cd Python-PowerScript
git pull
pip install --upgrade -e .
\```

## 🗑️ Uninstalling

### Remove TPS

\```bash
pip uninstall tps
\```

### Remove VS Code Extension

\```bash
code --uninstall-extension saleemlewis.powerscript
\```

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

## 🎓 Next Steps

After installation:

1. **[Quick Start Guide](quickstart.md)** - Your first program in 5 minutes
2. **[VS Code Extension Guide](vscode_extension.md)** - Setup your IDE
3. **[CLI Reference](cli_reference.md)** - Learn command-line tools

## 🆘 Getting Help

- **Issues:** [GitHub Issues](https://github.com/SaleemLww/Python-PowerScript/issues)
- **Discussions:** [GitHub Discussions](https://github.com/SaleemLww/Python-PowerScript/discussions)
- **Docs:** [Documentation](README.md)

---

**Installation successful? Start coding with [Quick Start](quickstart.md)! 🚀**
