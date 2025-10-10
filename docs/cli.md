# PowerScript CLI Guide

**Complete command-line interface documentation for PowerScript development tools**

> **Version**: 2.0 | **Status**: Production Ready | **Updated**: October 2025

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [powerscriptc - The Compiler](#powerscriptc---the-compiler)
4. [ps-run - Direct Execution](#ps-run---direct-execution)
5. [ps-create - Project Creator](#ps-create---project-creator)
6. [psc - Type Checker](#psc---type-checker)
7. [Configuration Files](#configuration-files)
8. [Common Workflows](#common-workflows)
9. [Troubleshooting](#troubleshooting)
10. [Advanced Usage](#advanced-usage)

## Overview

PowerScript provides a comprehensive set of command-line tools for developing, compiling, and managing PowerScript projects. All tools are designed to work together seamlessly and provide a professional development experience.

### Available Tools

| Tool | Purpose | Key Features |
|------|---------|--------------|
| `powerscriptc` | Compile PowerScript to Python | Watch mode, strict checking, optimization |
| `ps-run` | Execute PowerScript files directly | Auto-compilation, runtime environment |
| `ps-create` | Create new projects | Templates, scaffolding, dependencies |
| `psc` | Static type checking | JSON output, integration support |

### System Requirements

- **Python**: 3.8 or higher
- **Operating System**: macOS, Linux, Windows
- **Dependencies**: See `requirements.txt`

## Installation

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/SaleemLww/Python-PowerScript.git
cd Python-PowerScript

# Install dependencies
pip install -r requirements.txt

# Make CLI tools executable (macOS/Linux)
chmod +x bin/*

# Add to PATH (optional)
export PATH="$PWD/bin:$PATH"
```

### Verify Installation

```bash
# Check all tools are available
powerscriptc --version
ps-run --version
ps-create --version
psc --version
```

## powerscriptc - The Compiler

The main compiler tool that transpiles PowerScript source code to Python.

### Basic Usage

```bash
# Compile a single file
powerscriptc src/main.ps

# Compile with output directory
powerscriptc src/main.ps -o build/

# Compile entire directory
powerscriptc src/ -o build/

# Compile multiple files
powerscriptc src/main.ps src/utils.ps -o build/
```

### Command Options

#### Input/Output Options

```bash
-o, --output DIRECTORY     # Output directory for compiled files
-s, --source DIRECTORY     # Source directory (alternative to file list)
--ext EXTENSION           # Output file extension (default: .py)
```

Example:
```bash
powerscriptc src/ -o dist/ --ext .python
```

#### Compilation Options

```bash
--strict                  # Enable strict type checking
--no-runtime             # Exclude PowerScript runtime
--optimize               # Enable code optimization
--target python38        # Target Python version (3.8, 3.9, 3.10, 3.11)
```

Example:
```bash
powerscriptc src/ -o build/ --strict --optimize --target python39
```

#### Development Options  

```bash
-w, --watch              # Watch mode - recompile on changes
-v, --verbose            # Verbose output
--debug                  # Debug mode with detailed logging
--dry-run               # Show what would be compiled without doing it
```

Example:
```bash
powerscriptc src/ -o build/ --watch --verbose
```

#### Type Checking Options

```bash
--no-type-check          # Skip type checking
--type-check-only        # Only perform type checking, don't compile
--beartype               # Enable runtime type validation
--ignore-errors          # Continue compilation despite errors
```

Example:
```bash
powerscriptc src/ --type-check-only --strict
```

### Configuration File

Create a `powerscript.toml` file in your project root:

```toml
[compiler]
strict = true
optimize = true
target = "python39"
output_extension = ".py"
exclude_runtime = false

[watch]
ignore_patterns = ["*.tmp", "*.log", "__pycache__"]
debounce_delay = 500

[type_checking]
enable_beartype = true
ignore_missing_imports = false
```

### Watch Mode

Watch mode automatically recompiles files when they change:

```bash
# Basic watch mode
powerscriptc src/ -o build/ --watch

# Watch with specific patterns
powerscriptc src/ -o build/ --watch --ignore "*.test.ps"

# Watch with custom debounce delay
powerscriptc src/ -o build/ --watch --debounce 1000
```

Watch mode features:
- **Incremental compilation**: Only recompiles changed files
- **Dependency tracking**: Recompiles dependent files automatically
- **Error recovery**: Continues watching after compilation errors
- **Smart ignoring**: Ignores temporary and build files

### Examples

#### Development Workflow

```bash
# Start development with watch mode
powerscriptc src/ -o build/ --watch --verbose

# In another terminal, run the compiled code
python build/main.py
```

#### Production Build

```bash
# Optimized production build
powerscriptc src/ -o dist/ --strict --optimize --target python39

# Verify the build
ls -la dist/
python dist/main.py
```

#### Type Checking Only

```bash
# Check types without compiling
powerscriptc src/ --type-check-only --strict

# Generate type checking report
powerscriptc src/ --type-check-only --json > type-report.json
```

## ps-run - Direct Execution

Execute PowerScript files directly without manual compilation.

### Basic Usage

```bash
# Run a PowerScript file
ps-run src/main.ps

# Run with arguments
ps-run src/cli-tool.ps --verbose --output results.txt

# Run with environment variables
DEBUG=1 ps-run src/debug-script.ps
```

### Command Options

```bash
-c, --compile-only       # Compile but don't execute
-k, --keep-output        # Keep compiled Python files
-o, --output DIRECTORY   # Custom output directory for compiled files
--python EXECUTABLE      # Python executable to use for execution
--strict                 # Enable strict type checking
--verbose               # Verbose output
```

### Examples

#### Quick Script Execution

```bash
# Run a simple script
ps-run scripts/data-processing.ps

# Run with verbose output
ps-run scripts/analysis.ps --verbose
```

#### Development Testing

```bash
# Test script with arguments
ps-run tests/unit-test.ps --test-suite api

# Keep compiled files for debugging
ps-run src/main.ps --keep-output -o debug/
```

#### Custom Python Environment

```bash
# Use specific Python version
ps-run src/ml-script.ps --python python3.9

# Use virtual environment Python
ps-run src/app.ps --python venv/bin/python
```

## ps-create - Project Creator

Create new PowerScript projects with templates and scaffolding.

### Basic Usage

```bash
# Create a basic project
ps-create my-project

# Create with specific template
ps-create my-ai-project --template ai

# Create in specific directory
ps-create my-project --directory /path/to/projects/
```

### Available Templates

#### Built-in Templates

```bash
--template basic         # Basic PowerScript project
--template web           # Web application with HTTP server
--template ai            # AI/ML project with data science libraries
--template cli           # Command-line interface application
--template library       # Reusable library/package
--template api           # REST API service
--template desktop       # Desktop GUI application
```

#### Template Features

**Basic Template**:
- Simple project structure
- Example PowerScript files
- Basic configuration
- README and documentation

**AI Template**:
- NumPy, Pandas, scikit-learn integration
- Jupyter notebook examples
- Data processing utilities
- ML model templates

**Web Template**:
- HTTP server setup
- Route handling
- Template rendering
- Static file serving

**CLI Template**:
- Argument parsing
- Command structure
- Help system
- Configuration management

### Command Options

```bash
-t, --template NAME      # Project template to use
-d, --directory PATH     # Target directory
--no-git                # Don't initialize Git repository
--no-deps               # Don't install dependencies
--python VERSION        # Target Python version (3.8, 3.9, 3.10, 3.11)
```

### Project Structure

A typical PowerScript project created by `ps-create`:

```
my-project/
├── src/                 # Source code
│   ├── main.ps         # Main application file
│   ├── utils/          # Utility modules
│   └── types/          # Type definitions
├── tests/              # Test files
│   ├── unit/           # Unit tests
│   └── integration/    # Integration tests
├── docs/               # Documentation
├── examples/           # Usage examples
├── build/              # Compiled output (created by compiler)
├── powerscript.toml    # Project configuration
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── .gitignore         # Git ignore patterns
└── .vscode/           # VS Code configuration
    ├── settings.json
    ├── tasks.json
    └── launch.json
```

### Examples

#### Create AI/ML Project

```bash
ps-create my-ml-project --template ai
cd my-ml-project

# Project includes:
# - Data processing utilities
# - ML model templates
# - Jupyter notebooks
# - NumPy/Pandas integration
```

#### Create Web API Project

```bash
ps-create my-api --template api
cd my-api

# Project includes:
# - HTTP server setup
# - Route handling
# - Request/response utilities
# - Authentication examples
```

#### Create CLI Tool

```bash
ps-create my-cli-tool --template cli
cd my-cli-tool

# Project includes:
# - Argument parsing
# - Command structure
# - Help system
# - Configuration management
```

### Custom Templates

You can create custom templates by:

1. **Creating template directory**:
```bash
mkdir ~/.powerscript/templates/my-template
```

2. **Adding template files**:
```
~/.powerscript/templates/my-template/
├── template.toml       # Template configuration
├── src/
│   └── main.ps.template
├── tests/
│   └── test_main.ps.template
└── README.md.template
```

3. **Template configuration** (`template.toml`):
```toml
[template]
name = "my-template"
description = "My custom project template"
author = "Your Name"
version = "1.0.0"

[variables]
project_name = "Project name"
author_name = "Author name"
license = "License type"

[dependencies]
python = ["requests", "click"]
powerscript = []
```

4. **Using custom template**:
```bash
ps-create my-project --template my-template
```

## psc - Type Checker

Static type checker for PowerScript code.

### Basic Usage

```bash
# Check a single file
psc src/main.ps

# Check entire directory
psc src/

# Check multiple files
psc src/main.ps src/utils.ps src/types.ps
```

### Command Options

```bash
--strict                # Enable strict type checking
--json                  # Output results in JSON format
--ignore-missing        # Ignore missing type annotations
--follow-imports        # Check imported modules
--cache                 # Use type checking cache
--no-cache             # Disable type checking cache
```

### Output Formats

#### Standard Output

```bash
psc src/main.ps
```
```
src/main.ps:15:12: error: Argument 1 to "process_data" has incompatible type "str"; expected "int"
src/main.ps:23:8: warning: Variable "result" is not used
src/utils.ps:45:20: error: Cannot assign to read-only property "name"
```

#### JSON Output

```bash
psc src/ --json
```
```json
{
  "files_checked": 5,
  "errors": [
    {
      "file": "src/main.ps",
      "line": 15,
      "column": 12,
      "severity": "error",
      "message": "Argument 1 to \"process_data\" has incompatible type \"str\"; expected \"int\"",
      "code": "type-mismatch"
    }
  ],
  "warnings": [
    {
      "file": "src/main.ps", 
      "line": 23,
      "column": 8,
      "severity": "warning",
      "message": "Variable \"result\" is not used",
      "code": "unused-variable"
    }
  ],
  "summary": {
    "total_errors": 1,
    "total_warnings": 1,
    "files_with_errors": 1
  }
}
```

### Integration Examples

#### CI/CD Integration

```bash
# GitHub Actions
- name: Type Check
  run: |
    psc src/ --json > type-check-results.json
    if [ $(jq '.summary.total_errors' type-check-results.json) -gt 0 ]; then
      echo "Type checking failed"
      exit 1
    fi
```

#### Pre-commit Hook

```bash
#!/bin/bash
# .git/hooks/pre-commit

echo "Running type checks..."
psc src/ --strict

if [ $? -ne 0 ]; then
    echo "Type checking failed. Please fix errors before committing."
    exit 1
fi
```

#### VS Code Integration

```json
// .vscode/tasks.json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Type Check",
            "type": "shell", 
            "command": "psc",
            "args": ["src/", "--json"],
            "group": "build",
            "presentation": {
                "reveal": "always",
                "panel": "new"
            },
            "problemMatcher": {
                "owner": "powerscript",
                "fileLocation": "absolute",
                "pattern": {
                    "regexp": "^(.+):(\\d+):(\\d+):\\s+(error|warning):\\s+(.+)$",
                    "file": 1,
                    "line": 2,
                    "column": 3,
                    "severity": 4,
                    "message": 5
                }
            }
        }
    ]
}
```

## Configuration Files

### powerscript.toml

Main configuration file for PowerScript projects:

```toml
[project]
name = "my-project"
version = "1.0.0"
description = "My PowerScript project"
author = "Your Name <you@example.com>"
license = "MIT"

[compiler]
# Compilation settings
strict = true                    # Enable strict mode
optimize = true                  # Enable optimizations
target = "python39"             # Target Python version
output_extension = ".py"         # Output file extension
exclude_runtime = false          # Include PowerScript runtime
source_maps = true              # Generate source maps for debugging

[type_checking]
# Type checking settings
strict_mode = true              # Strict type checking
ignore_missing_imports = false  # Fail on missing imports
follow_imports = true           # Check imported files
enable_beartype = true          # Runtime type validation
cache_type_info = true          # Cache type information

[build]
# Build settings
source_dir = "src"              # Source directory
output_dir = "build"            # Output directory
include_patterns = ["*.ps"]     # Files to include
exclude_patterns = ["*.test.ps", "*.example.ps"]  # Files to exclude

[watch]
# Watch mode settings
enable = true                   # Enable watch mode
debounce_delay = 500           # Delay before recompilation (ms)
ignore_patterns = [            # Patterns to ignore
    "*.tmp",
    "*.log", 
    "__pycache__",
    ".git"
]

[dependencies]
# Python dependencies
python = [
    "requests>=2.25.0",
    "click>=8.0.0",
    "pydantic>=1.8.0"
]

# PowerScript dependencies  
powerscript = []

[dev_dependencies]
# Development dependencies
python = [
    "pytest>=6.0.0",
    "black>=21.0.0", 
    "mypy>=0.910"
]

[scripts]
# Custom scripts
build = "powerscriptc src/ -o build/ --strict"
test = "pytest tests/"
format = "black build/"
type-check = "psc src/ --strict"
dev = "powerscriptc src/ -o build/ --watch"

[vscode]
# VS Code integration
enable_extension = true
syntax_highlighting = true
intellisense = true
debugging = true
```

### .powerscriptignore

Ignore files and directories during compilation:

```gitignore
# Temporary files
*.tmp
*.log
*.cache

# Test files
*.test.ps
*_test.ps
test_*.ps

# Example files
*.example.ps
examples/

# Build artifacts
build/
dist/
*.pyc
__pycache__/

# Development files
.vscode/
.idea/
*.swp
*.swo

# Documentation
docs/
*.md
```

## Common Workflows

### Development Workflow

```bash
# 1. Create new project
ps-create my-app --template web

# 2. Navigate to project
cd my-app

# 3. Start development server with watch mode
powerscriptc src/ -o build/ --watch --verbose &

# 4. Run the application
python build/main.py

# 5. In another terminal, run type checking
psc src/ --strict --json
```

### Production Deployment

```bash
# 1. Type check
psc src/ --strict
if [ $? -ne 0 ]; then exit 1; fi

# 2. Optimized build
powerscriptc src/ -o dist/ --strict --optimize --target python39

# 3. Run tests on compiled code
python -m pytest tests/

# 4. Deploy
rsync -av dist/ production-server:/app/
```

### Testing Workflow

```bash
# 1. Compile test files
powerscriptc tests/ -o build/tests/

# 2. Run unit tests
python -m pytest build/tests/unit/

# 3. Run integration tests
python -m pytest build/tests/integration/

# 4. Generate coverage report
python -m pytest build/tests/ --cov=build/src --cov-report=html
```

### Library Development

```bash
# 1. Create library project
ps-create my-library --template library

# 2. Develop with type checking
powerscriptc src/ -o build/ --strict --watch &
psc src/ --strict --follow-imports

# 3. Build for distribution
powerscriptc src/ -o dist/ --strict --optimize

# 4. Package
python setup.py sdist bdist_wheel
```

## Troubleshooting

### Common Issues

#### Compilation Errors

**Problem**: `SyntaxError: invalid syntax`
```bash
powerscriptc src/main.ps
# Error: SyntaxError at line 15: unexpected token 'function'
```

**Solution**: Check PowerScript syntax:
```powerscript
// Correct syntax
function greet(name: string): string {
    return f"Hello, {name}!"
}

// Incorrect syntax (missing type annotation)
function greet(name) {
    return f"Hello, {name}!"
}
```

#### Type Checking Errors

**Problem**: Type mismatch errors
```bash
psc src/main.ps
# Error: Argument 1 has incompatible type "str"; expected "int"
```

**Solution**: Fix type annotations:
```powerscript
// Problem
function processAge(age: number): void {
    console.log(f"Age: {age}")
}

processAge("25")  // Error: string instead of number

// Solution
processAge(25)    // Correct: number
// or
processAge(parseInt("25"))  // Convert string to number
```

#### Import Errors

**Problem**: Module not found
```bash
powerscriptc src/main.ps
# Error: Cannot resolve import './utils'
```

**Solution**: Check file paths and extensions:
```powerscript
// Make sure file exists: src/utils.ps
import { helper } from "./utils"    // Correct

// Or use full path
import { helper } from "./utils.ps" // Also works
```

#### Watch Mode Issues

**Problem**: Watch mode not detecting changes
```bash
powerscriptc src/ -o build/ --watch
# Changes not detected
```

**Solutions**:
1. Check ignore patterns in `powerscript.toml`
2. Increase debounce delay
3. Use polling mode:
```bash
powerscriptc src/ -o build/ --watch --poll
```

### Performance Issues

#### Slow Compilation

**Problem**: Compilation takes too long

**Solutions**:
1. **Exclude unnecessary files**:
```toml
[build]
exclude_patterns = ["*.test.ps", "examples/", "docs/"]
```

2. **Use incremental compilation**:
```bash
powerscriptc src/ -o build/ --incremental
```

3. **Disable type checking for faster builds**:
```bash
powerscriptc src/ -o build/ --no-type-check
```

#### Memory Issues

**Problem**: High memory usage during compilation

**Solutions**:
```bash
# Reduce memory usage
powerscriptc src/ -o build/ --memory-limit 512MB

# Process files in batches
powerscriptc src/ -o build/ --batch-size 10
```

### Debug Mode

Enable debug mode for detailed information:

```bash
# Debug compilation
powerscriptc src/main.ps --debug

# Debug with verbose output
powerscriptc src/ -o build/ --debug --verbose 2> debug.log

# Debug type checking
psc src/ --debug --verbose
```

Debug output includes:
- Token analysis
- AST construction
- Type inference steps
- Code generation process
- Error stack traces

## Advanced Usage

### Custom Python AST Generation

You can customize the Python AST generation process:

```bash
# Custom AST transformations
powerscriptc src/ -o build/ --ast-transform custom_transform.py

# Custom runtime injections
powerscriptc src/ -o build/ --runtime-inject custom_runtime.py
```

### Integration with Build Systems

#### Makefile Integration

```makefile
# Makefile
.PHONY: build test clean type-check

build:
	powerscriptc src/ -o build/ --strict --optimize

test: build
	python -m pytest build/tests/

type-check:
	psc src/ --strict --json > type-report.json

clean:
	rm -rf build/ dist/

dev:
	powerscriptc src/ -o build/ --watch &
	python build/main.py

install:
	pip install -r requirements.txt
	chmod +x bin/*
```

#### npm Scripts Integration

```json
{
  "scripts": {
    "build": "powerscriptc src/ -o build/ --strict",
    "dev": "powerscriptc src/ -o build/ --watch",
    "test": "python -m pytest build/tests/",
    "type-check": "psc src/ --strict",
    "clean": "rm -rf build/ dist/"
  }
}
```

### Continuous Integration

#### GitHub Actions

```yaml
# .github/workflows/powerscript.yml
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
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        chmod +x bin/*
    
    - name: Type check
      run: psc src/ --strict --json > type-report.json
    
    - name: Build
      run: powerscriptc src/ -o build/ --strict --optimize
    
    - name: Test
      run: python -m pytest build/tests/
    
    - name: Upload artifacts
      uses: actions/upload-artifact@v2
      with:
        name: build-artifacts
        path: build/
```

### Performance Optimization

#### Compilation Performance

```bash
# Parallel compilation
powerscriptc src/ -o build/ --parallel --jobs 4

# Cache compilation results
powerscriptc src/ -o build/ --cache --cache-dir .ps-cache

# Profile compilation
powerscriptc src/ -o build/ --profile > compile-profile.txt
```

#### Runtime Performance

```bash
# Generate optimized Python code
powerscriptc src/ -o build/ --optimize --target python39

# Enable JIT compilation markers
powerscriptc src/ -o build/ --jit-hints

# Inline small functions
powerscriptc src/ -o build/ --inline-functions
```

---

This completes the PowerScript CLI Guide. For more information, see:

- [Language Reference](language-reference.md)
- [API Documentation](api.md)
- [VS Code Extension](vscode.md)
- [Tutorial](../powerscript/docs/tutorial.md)

**PowerScript: Professional command-line tools for modern development! 🐍✨**