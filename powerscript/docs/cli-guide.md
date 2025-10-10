# PowerScript CLI Guide

## Overview

PowerScript provides several command-line tools to compile, run, and manage PowerScript projects:

- `powerscriptc` - Compile PowerScript to Python
- `ps-run` - Run PowerScript files directly  
- `ps-create` - Create new PowerScript projects
- `psc` - Type checker and static analyzer

## Installation

```bash
# Install from source
git clone https://github.com/SaleemLww/Python-PowerScript.git
cd Python-PowerScript
pip install -e .

# Verify installation
powerscriptc --version
ps-run --version
ps-create --version
psc --version
```

## powerscriptc - Compiler

Compiles PowerScript files to Python.

### Basic Usage

```bash
# Compile a single file
powerscriptc hello.ps

# Compile with output directory
powerscriptc hello.ps -o build/

# Compile entire directory
powerscriptc src/ -o build/

# Compile multiple files
powerscriptc file1.ps file2.ps -o build/
```

### Options

```bash
powerscriptc [OPTIONS] [FILES...]

Options:
  -o, --output DIR     Output directory (default: current directory)
  -w, --watch         Watch mode - recompile on file changes
  -v, --verbose       Verbose output
  -s, --strict        Strict type checking mode
  -r, --runtime       Include runtime type checks
  --no-stubs          Don't generate .pyi stub files
  --target VERSION    Python target version (3.8, 3.9, 3.10, 3.11, 3.12)
  --optimize          Enable optimizations
  --debug             Include debug information
  -h, --help          Show help message
  --version           Show version
```

### Examples

```bash
# Watch mode for development
powerscriptc -w src/ -o build/

# Strict mode with runtime checks
powerscriptc -s -r src/ -o build/

# Target specific Python version
powerscriptc --target 3.11 src/ -o build/

# Verbose compilation with debug info
powerscriptc -v --debug src/ -o build/

# Production build with optimizations
powerscriptc --optimize --no-stubs src/ -o dist/
```

### Configuration File

Create `powerscript.toml` in your project root:

```toml
[project]
name = "my_project"
version = "1.0.0"
main = "src/main.ps"

[compiler]
output_dir = "build"
strict_typing = true
runtime_checks = false
target_python = "3.11"
generate_stubs = true
optimize = false

[compiler.include]
paths = ["src/**/*.ps"]

[compiler.exclude]
paths = ["src/test_*.ps", "**/*.dev.ps"]
```

## ps-run - Direct Runner

Run PowerScript files without explicit compilation.

### Basic Usage

```bash
# Run a single file
ps-run main.ps

# Run with arguments
ps-run script.ps arg1 arg2

# Run from different directory
ps-run /path/to/script.ps
```

### Options

```bash
ps-run [OPTIONS] FILE [ARGS...]

Options:
  -v, --verbose       Verbose output
  -s, --strict        Strict type checking
  -r, --runtime       Enable runtime checks
  --temp-dir DIR      Temporary directory for compiled files
  --keep-temp         Don't delete temporary files
  --profile           Profile execution time
  -h, --help          Show help message
  --version           Show version
```

### Examples

```bash
# Run with strict checking
ps-run -s main.ps

# Profile execution
ps-run --profile data_processing.ps

# Keep temporary files for debugging
ps-run --keep-temp --temp-dir=/tmp/ps debug.ps

# Pass arguments to script
ps-run script.ps --input data.csv --output results.json
```

## ps-create - Project Generator

Create new PowerScript projects with proper structure.

### Basic Usage

```bash
# Create basic project
ps-create my_project

# Create AI/ML project
ps-create my_ai_project --template ai

# Create web project
ps-create my_web_app --template web

# Create library project
ps-create my_library --template library
```

### Templates

#### Basic Template
```
my_project/
├── src/
│   └── main.ps
├── tests/
│   └── test_main.ps
├── powerscript.toml
├── requirements.txt
├── README.md
└── .gitignore
```

#### AI Template
```
my_ai_project/
├── src/
│   ├── main.ps
│   ├── models/
│   │   └── base_model.ps
│   ├── data/
│   │   ├── loader.ps
│   │   └── processor.ps
│   └── utils/
│       └── helpers.ps
├── tests/
│   ├── test_models.ps
│   └── test_data.ps
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── requirements.txt
├── powerscript.toml
└── README.md
```

### Options

```bash
ps-create [OPTIONS] PROJECT_NAME

Options:
  -t, --template TYPE   Project template (basic, ai, web, library)
  -d, --directory DIR   Parent directory (default: current)
  --no-git             Don't initialize git repository
  --no-venv            Don't create virtual environment
  --python-version VER Python version for venv
  -f, --force          Overwrite existing directory
  -h, --help           Show help message
  --version            Show version
```

### Examples

```bash
# Create AI project with specific Python version
ps-create ml_project -t ai --python-version 3.11

# Create project in specific directory
ps-create web_app -t web -d /projects/

# Force overwrite existing directory
ps-create my_project -f

# Create without git initialization
ps-create simple_project --no-git
```

### Custom Templates

Create custom templates in `~/.powerscript/templates/`:

```
~/.powerscript/templates/
├── my_template/
│   ├── template.json
│   ├── src/
│   │   └── {{project_name}}.ps
│   └── powerscript.toml.template
```

**template.json:**
```json
{
  "name": "my_template",
  "description": "My custom PowerScript template",
  "variables": {
    "project_name": "Project name",
    "author": "Author name",
    "version": "Initial version"
  },
  "dependencies": [
    "numpy>=1.21.0",
    "pandas>=1.3.0"
  ]
}
```

Use custom template:
```bash
ps-create my_project -t my_template
```

## psc - Type Checker

Static type checker and code analyzer.

### Basic Usage

```bash
# Check single file
psc main.ps

# Check directory
psc src/

# Check with specific config
psc --config myconfig.toml src/
```

### Options

```bash
psc [OPTIONS] [FILES...]

Options:
  -c, --config FILE    Configuration file
  -s, --strict         Strict mode
  --no-cache          Disable type checking cache
  --show-traceback    Show full error tracebacks
  --json              Output results as JSON
  --watch             Watch mode - recheck on changes
  --fix               Attempt to fix issues automatically
  -h, --help          Show help message
  --version           Show version
```

### Examples

```bash
# Strict type checking
psc -s src/

# Watch mode for continuous checking
psc --watch src/

# Output as JSON for integration
psc --json src/ > type_check_results.json

# Auto-fix issues where possible
psc --fix src/
```

### Type Check Configuration

**psc.toml:**
```toml
[type_check]
strict_mode = true
cache_enabled = true
max_errors = 50
ignore_patterns = ["**/*test*.ps"]

[type_check.rules]
require_return_type = true
require_parameter_types = true
disallow_any = false
warn_unused_variables = true
warn_unused_imports = true

[type_check.python_integration]
use_pyright = true
pyright_config = "pyrightconfig.json"
```

## Workflow Integration

### Development Workflow

```bash
# 1. Create new project
ps-create ml_project -t ai

# 2. Navigate to project
cd ml_project

# 3. Start development with watch mode
powerscriptc -w src/ -o build/ &

# 4. Run type checker in watch mode
psc --watch src/ &

# 5. Edit files in your IDE
code src/main.ps

# 6. Test your changes
ps-run src/main.ps

# 7. Run compiled Python
python build/main.py
```

### CI/CD Integration

**GitHub Actions workflow:**
```yaml
name: PowerScript CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.11'
    
    - name: Install PowerScript
      run: |
        pip install -r requirements.txt
        pip install -e .
    
    - name: Type check
      run: psc src/
    
    - name: Compile
      run: powerscriptc src/ -o build/
    
    - name: Run tests
      run: python -m pytest build/tests/
```

### Makefile Integration

```makefile
# Makefile for PowerScript project

.PHONY: compile run test check clean install

compile:
	powerscriptc src/ -o build/

run: compile
	python build/main.py

test: compile
	python -m pytest build/tests/

check:
	psc src/

clean:
	rm -rf build/ __pycache__/ .pytest_cache/

install:
	pip install -r requirements.txt

dev: install
	powerscriptc -w src/ -o build/ &
	psc --watch src/

# Usage: make dev
```

## Troubleshooting

### Common Issues

**1. Import Errors**
```bash
# Problem: Module not found
# Solution: Check Python path and ensure modules are compiled
powerscriptc -v src/ -o build/
export PYTHONPATH="${PYTHONPATH}:./build"
```

**2. Type Checking Errors**
```bash
# Problem: Type errors in strict mode
# Solution: Run with detailed error messages
psc --show-traceback src/
```

**3. Compilation Failures**
```bash
# Problem: Syntax errors
# Solution: Check with verbose output
powerscriptc -v --debug src/
```

### Debug Options

```bash
# Enable all debug options
powerscriptc --debug -v --keep-temp src/

# Check intermediate files
ls -la /tmp/powerscript_*

# Examine generated Python code
cat build/main.py
```

### Performance Tips

1. **Use watch mode during development**
   ```bash
   powerscriptc -w src/ -o build/
   ```

2. **Enable caching for type checking**
   ```bash
   psc --cache src/
   ```

3. **Compile only changed files**
   ```bash
   powerscriptc --incremental src/
   ```

4. **Use specific file patterns**
   ```bash
   powerscriptc src/**/*.ps -o build/
   ```

## Advanced Usage

### Custom Transpilation Rules

Create `transpile_rules.py`:
```python
from powerscript.compiler.transpiler import Transpiler

class CustomTranspiler(Transpiler):
    def visit_custom_node(self, node):
        # Custom transpilation logic
        return self.create_python_node(node)
```

Use with:
```bash
powerscriptc --transpiler custom_transpiler.py src/
```

### Integration with Build Tools

**setup.py integration:**
```python
from setuptools import setup
from powerscript.build import compile_powerscript

class PowerScriptBuild:
    def run(self):
        compile_powerscript('src/', 'build/')

setup(
    name="my_project",
    cmdclass={'build_ps': PowerScriptBuild},
    # ... other setup options
)
```

Run with:
```bash
python setup.py build_ps
```

This comprehensive CLI guide covers all the tools and workflows for effective PowerScript development!