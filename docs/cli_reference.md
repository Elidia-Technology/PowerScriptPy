# ⚙️ CLI Reference# ⚙️ CLI Reference# ⚙️ CLI Reference



Complete reference for PowerScript command-line tools.



## 📦 Available CommandsComplete reference for PowerScript command-line tools.Complete reference for PowerScript command-line tools.



TPS provides 4 main CLI commands:



| Command | Purpose | Status |------

|---------|---------|--------|

| `tps-compile` | Compile `.ps` to `.py` | ✅ Stable |

| `tps-run` | Compile and execute | ✅ Stable |

| `tps-create` | Create new projects | ✅ Stable |## 📦 Available Commands## 📦 Available Commands

| `tps-check` | Type check without compiling | ✅ Stable |



## 🔧 tps-compile

TPS provides 4 main CLI commands:TPS provides 4 main CLI commands:

Compile PowerScript files to Python.



### Basic Usage

| Command | Purpose | Status || Command | Purpose | Status |

```bash

# Compile single file|---------|---------|--------||---------|---------|--------|

tps-compile myfile.ps

| `tps-compile` | Compile `.ps` to `.py` | ✅ Stable || `tps-compile` | Compile `.ps` to `.py` | ✅ Stable |

# Output: myfile.py

```| `tps-run` | Compile and execute | ✅ Stable || `tps-run` | Compile and execute | ✅ Stable |



### Options| `tps-create` | Create new projects | ✅ Stable || `tps-create` | Create new projects | ✅ Stable |



```bash| `tps-check` | Type check without compiling | ✅ Stable || `tps-check` | Type check without compiling | ✅ Stable |

tps-compile [OPTIONS] <input_file>

```



| Option | Description | Default |------

|--------|-------------|---------|

| `-o, --output <file>` | Output file path | `<input>.py` |

| `-d, --output-dir <dir>` | Output directory | Current dir |

| `--strict` | Enable strict type checking | `false` |## 🔧 tps-compile## 🔧 tps-compile

| `--verbose` | Verbose output | `false` |

| `--help` | Show help message | - |



### ExamplesCompile PowerScript files to Python.Compile PowerScript files to Python.



**Custom Output:**

```bash

tps-compile main.ps -o build/main.py### Basic Usage### Basic Usage

```



**Output Directory:**

```bash```bash```bash

tps-compile src/app.ps -d build/

# Creates: build/app.py# Compile single file# Compile single file

```

tps-compile myfile.pstps-compile myfile.ps

**Strict Mode:**

```bash

tps-compile app.ps --strict

# Enables strict type checking# Output: myfile.py# Output: myfile.py

```

``````

**Verbose Compilation:**

```bash

tps-compile app.ps --verbose

# Shows detailed compilation steps### Options### Options

```



### Exit Codes

```bash```bash

| Code | Meaning |

|------|---------|tps-compile [OPTIONS] <input_file>tps-compile [OPTIONS] <input_file>

| `0` | Success |

| `1` | Compilation error |``````

| `2` | File not found |

| `3` | Invalid options |



## 🚀 tps-run| Option | Description | Default || Option | Description | Default |



Compile and execute PowerScript files immediately.|--------|-------------|---------||--------|-------------|---------|



### Basic Usage| `-o, --output <file>` | Output file path | `<input>.py` || `-o, --output <file>` | Output file path | `<input>.py` |



```bash| `-d, --output-dir <dir>` | Output directory | Current dir || `-d, --output-dir <dir>` | Output directory | Current dir |

tps-run myfile.ps

# Compiles and runs in one step| `--strict` | Enable strict type checking | `false` || `--strict` | Enable strict type checking | `false` |

```

| `--no-runtime` | Exclude runtime imports | `false` || `--no-runtime` | Exclude runtime imports | `false` |

### Options

| `-v, --verbose` | Verbose output | `false` || `-v, --verbose` | Verbose output | `false` |

```bash

tps-run [OPTIONS] <input_file> [-- <args>]| `-q, --quiet` | Suppress output | `false` || `-q, --quiet` | Suppress output | `false` |

```

| `--help` | Show help message | - || `--help` | Show help message | - |

| Option | Description | Default |

|--------|-------------|---------|| `--version` | Show version | - || `--version` | Show version | - |

| `--keep` | Keep compiled `.py` file | `false` |

| `--strict` | Enable strict type checking | `false` |

| `--verbose` | Verbose output | `false` |

| `--help` | Show help message | - |### Examples### Examples



### Examples



**Run with Arguments:****Custom Output:****Custom Output:**

```bash

tps-run script.ps -- arg1 arg2 arg3```bash```bash

```

tps-compile main.ps -o build/main.pytps-compile main.ps -o build/main.py

**Keep Compiled File:**

```bash``````

tps-run app.ps --keep

# Keeps app.py after execution

```

**Output Directory:****Output Directory:**

**Verbose Run:**

```bash```bash```bash

tps-run app.ps --verbose

# Shows compilation + execution outputtps-compile src/app.ps -d build/tps-compile src/app.ps -d build/

```

# Creates: build/app.py# Creates: build/app.py

### How It Works

``````

1. Compiles `.ps` to `.py` (in memory or temp file)

2. Executes Python code

3. Cleans up temp files (unless `--keep`)

**Strict Mode:****Strict Mode:**

## 🏗️ tps-create

```bash```bash

Create new PowerScript projects with boilerplate.

tps-compile app.ps --stricttps-compile app.ps --strict

### Basic Usage

# Enables strict type checking# Enables strict type checking

```bash

tps-create my-project``````

cd my-project

```



### Options**Verbose Compilation:****Verbose Compilation:**



```bash```bash```bash

tps-create [OPTIONS] <project_name>

```tps-compile app.ps -vtps-compile app.ps -v



| Option | Description | Default |# Shows detailed compilation steps# Shows detailed compilation steps

|--------|-------------|---------|

| `-t, --template <name>` | Project template | `basic` |``````

| `--no-git` | Don't initialize git | `false` |

| `-f, --force` | Overwrite existing | `false` |

| `--help` | Show help message | - |

**Quiet Mode:****Quiet Mode:**

### Templates

```bash```bash

#### `basic` (Default)

Simple project with one file:tps-compile app.ps -qtps-compile app.ps -q



```# No output unless errors# No output unless errors

my-project/

├── src/``````

│   └── main.ps

├── build/

├── powerscript.toml

└── README.md### Exit Codes### Exit Codes

```



### Examples

| Code | Meaning || Code | Meaning |

**Basic Project:**

```bash|------|---------||------|---------|

tps-create my-app

```| `0` | Success || `0` | Success |



**No Git Init:**| `1` | Compilation error || `1` | Compilation error |

```bash

tps-create my-app --no-git| `2` | File not found || `2` | File not found |

```

| `3` | Invalid options || `3` | Invalid options |

**Force Overwrite:**

```bash

tps-create my-app -f

```### Output Format### Output Format



## ✅ tps-check



Type check PowerScript files without compiling.Compiled Python includes:Compiled Python includes:



### Basic Usage



```bash```python```python

tps-check myfile.ps

# Validates types only#!/usr/bin/env python3#!/usr/bin/env python3

```

# Generated by PowerScript Compiler v1.0.0# Generated by PowerScript Compiler v1.0.0

### Options

# Source: app.ps# Source: app.ps

```bash

tps-check [OPTIONS] <input_file>

```

from powerscript.runtime import Consolefrom powerscript.runtime import Console

| Option | Description | Default |

|--------|-------------|---------|# ... imports# ... imports

| `--strict` | Strict type checking | `false` |

| `--verbose` | Verbose output | `false` |

| `--help` | Show help message | - |

# Your compiled code here# Your compiled code here

### Examples

``````

**Basic Check:**

```bash

tps-check app.ps

# Type checks app.ps------

```



**Strict Mode:**

```bash## 🚀 tps-run## 🚀 tps-run

tps-check app.ps --strict

# Strict type validation

```

Compile and execute PowerScript files immediately.Compile and execute PowerScript files immediately.

### Output Format



**Success:**

```### Basic Usage### Basic Usage

✓ Type check passed: app.ps

  No issues found.

```

```bash```bash

**With Errors:**

```tps-run myfile.pstps-run myfile.ps

✗ Type check failed: app.ps

# Compiles and runs in one step# Compiles and runs in one step

Line 5: Type mismatch

  Expected: number``````

  Got: string

  

2 errors found.

```### Options### Options



## 🔧 Global Options



Available for all commands:```bash```bash



```bashtps-run [OPTIONS] <input_file> [-- <args>]tps-run [OPTIONS] <input_file> [-- <args>]

--version    # Show TPS version

--help       # Show command help``````

--verbose    # Verbose output

```



### Version Check| Option | Description | Default || Option | Description | Default |



```bash|--------|-------------|---------||--------|-------------|---------|

tps-compile --version

# Output: TPS 1.0.0b1| `--no-cache` | Don't cache compiled output | `false` || `--no-cache` | Don't cache compiled output | `false` |

```

| `--keep` | Keep compiled `.py` file | `false` || `--keep` | Keep compiled `.py` file | `false` |

## 📁 Configuration Files

| `--strict` | Enable strict type checking | `false` || `--strict` | Enable strict type checking | `false` |

### powerscript.toml

| `-v, --verbose` | Verbose output | `false` || `-v, --verbose` | Verbose output | `false` |

Project-level configuration:

| `-q, --quiet` | Suppress compilation output | `false` || `-q, --quiet` | Suppress compilation output | `false` |

```toml

[project]| `--help` | Show help message | - || `--help` | Show help message | - |

name = "my-project"

version = "1.0.0"| `--version` | Show version | - || `--version` | Show version | - |

entry = "src/main.ps"



[compiler]

output_dir = "build"### Examples### Examples

strict_types = true

target_version = "3.9"

```

**Run with Arguments:****Run with Arguments:**

## 🎯 Best Practices

```bash```bash

### Development Workflow

tps-run script.ps -- arg1 arg2 arg3tps-run script.ps -- arg1 arg2 arg3

```bash

# 1. Type check first``````

tps-check src/main.ps



# 2. Compile if no errors

tps-compile src/main.ps -d build/**Keep Compiled File:****Keep Compiled File:**



# 3. Run compiled code```bash```bash

python build/main.py

```tps-run app.ps --keeptps-run app.ps --keep



### Production Build# Keeps app.py after execution# Keeps app.py after execution



```bash``````

# Strict type checking

tps-compile src/main.ps --strict --output-dir dist/

```

**No Cache:****No Cache:**

## 📚 See Also

```bash```bash

- **[Quick Start](quickstart.md)** - Basic usage examples

- **[VS Code Extension](vscode_extension.md)** - IDE integrationtps-run app.ps --no-cachetps-run app.ps --no-cache

- **[FAQ](faq.md)** - Common questions

# Force recompilation# Force recompilation

---

``````

**Master the CLI? Continue to [VS Code Extension](vscode_extension.md)! 🚀**



**Verbose Run:****Verbose Run:**

```bash```bash

tps-run app.ps -vtps-run app.ps -v

# Shows compilation + execution output# Shows compilation + execution output

``````



### How It Works### How It Works



1. Compiles `.ps` to `.py` (in memory or temp file)1. Compiles `.ps` to `.py` (in memory or temp file)

2. Executes Python code2. Executes Python code

3. Cleans up temp files (unless `--keep`)3. Cleans up temp files (unless `--keep`)



### Exit Codes### Exit Codes



| Code | Meaning || Code | Meaning |

|------|---------||------|---------|

| `0` | Success || `0` | Success |

| `1` | Compilation error || `1` | Compilation error |

| `2` | Runtime error || `2` | Runtime error |

| `3` | File not found || `3` | File not found |



------



## 🏗️ tps-create## 🏗️ tps-create



Create new PowerScript projects with boilerplate.Create new PowerScript projects with boilerplate.



### Basic Usage### Basic Usage



```bash```bash

tps-create my-projecttps-create my-project

cd my-projectcd my-project

``````



### Options### Options



```bash```bash

tps-create [OPTIONS] <project_name>tps-create [OPTIONS] <project_name>

``````



| Option | Description | Default || Option | Description | Default |

|--------|-------------|---------||--------|-------------|---------|

| `-t, --template <name>` | Project template | `basic` || `-t, --template <name>` | Project template | `basic` |

| `--no-git` | Don't initialize git | `false` || `--no-git` | Don't initialize git | `false` |

| `--no-venv` | Don't create virtual env | `false` || `--no-venv` | Don't create virtual env | `false` |

| `-f, --force` | Overwrite existing | `false` || `-f, --force` | Overwrite existing | `false` |

| `--help` | Show help message | - || `--help` | Show help message | - |



### Templates### Templates



#### `basic` (Default)#### `basic` (Default)



Simple project with one file:Simple project with one file:



``````

my-project/my-project/

├── src/├── src/

│   └── main.ps│   └── main.ps

├── build/├── build/

├── powerscript.toml├── powerscript.toml

└── README.md└── README.md

``````



**main.ps:****main.ps:**

```powerscript```powerscript

function main(): void {function main(): void {

    console.log("Hello from PowerScript!");    console.log("Hello from PowerScript!");

}}

``````



#### `class` Template#### `class` Template



Object-oriented project:Object-oriented project:



``````

my-project/my-project/

├── src/├── src/

│   ├── main.ps│   ├── main.ps

│   └── models/│   └── models/

│       └── example.ps│       └── example.ps

├── build/├── build/

├── powerscript.toml├── powerscript.toml

└── README.md└── README.md

``````



#### `web` Template#### `web` Template



Web application structure:Web application structure:



``````

my-project/my-project/

├── src/├── src/

│   ├── app.ps│   ├── app.ps

│   ├── routes/│   ├── routes/

│   └── models/│   └── models/

├── static/├── static/

├── templates/├── templates/

├── build/├── build/

├── powerscript.toml├── powerscript.toml

└── README.md└── README.md

``````



### Examples### Examples



**Basic Project:****Basic Project:**

```bash```bash

tps-create my-apptps-create my-app

``````



**Class-based Project:****Class-based Project:**

```bash```bash

tps-create my-app -t classtps-create my-app -t class

``````



**Web Application:****Web Application:**

```bash```bash

tps-create my-web-app -t webtps-create my-web-app -t web

``````



**No Git Init:****No Git Init:**

```bash```bash

tps-create my-app --no-gittps-create my-app --no-git

``````



**Force Overwrite:****Force Overwrite:**

```bash```bash

tps-create my-app -ftps-create my-app -f

``````



### Generated Files### Generated Files



**powerscript.toml:****powerscript.toml:**

```toml```toml

[project][project]

name = "my-project"name = "my-project"

version = "0.1.0"version = "0.1.0"

entry = "src/main.ps"entry = "src/main.ps"

author = ""author = ""



[compiler][compiler]

output_dir = "build"output_dir = "build"

strict_types = truestrict_types = true

target_version = "3.9"target_version = "3.9"



[runtime][runtime]

include_builtins = trueinclude_builtins = true

``````



**README.md:**---

```markdown

# My Project## ✅ tps-check



PowerScript project created with tps-create.Type check PowerScript files without compiling.



## Setup### Basic Usage



\```bash```bash

pip install tpstps-check myfile.ps

\```# Validates types only

```

## Build

### Options

\```bash

tps-compile src/main.ps -d build/```bash

\```tps-check [OPTIONS] <input_file>

```

## Run

| Option | Description | Default |

\```bash|--------|-------------|---------|

tps-run src/main.ps| `--strict` | Strict type checking | `false` |

\```| `--warnings` | Show warnings | `true` |

```| `--json` | JSON output | `false` |

| `-v, --verbose` | Verbose output | `false` |

---| `--help` | Show help message | - |



## ✅ tps-check### Examples



Type check PowerScript files without compiling.**Basic Check:**

```bash

### Basic Usagetps-check app.ps

# Type checks app.ps

```bash```

tps-check myfile.ps

# Validates types only**Strict Mode:**

``````bash

tps-check app.ps --strict

### Options# Strict type validation

```

```bash

tps-check [OPTIONS] <input_file>**JSON Output:**

``````bash

tps-check app.ps --json

| Option | Description | Default |# Outputs results as JSON

|--------|-------------|---------|```

| `--strict` | Strict type checking | `false` |

| `--warnings` | Show warnings | `true` |### Output Format

| `--json` | JSON output | `false` |

| `-v, --verbose` | Verbose output | `false` |**Success:**

| `--help` | Show help message | - |```

✓ Type check passed: app.ps

### Examples  No issues found.

```

**Basic Check:**

```bash**With Errors:**

tps-check app.ps```

# Type checks app.ps✗ Type check failed: app.ps

```

Line 5: Type mismatch

**Strict Mode:**  Expected: number

```bash  Got: string

tps-check app.ps --strict  

# Strict type validationLine 12: Undefined variable 'x'

```  

2 errors found.

**JSON Output:**```

```bash

tps-check app.ps --json**JSON Output:**

# Outputs results as JSON```json

```{

  "file": "app.ps",

### Output Format  "status": "error",

  "errors": [

**Success:**    {

```      "line": 5,

✓ Type check passed: app.ps      "column": 10,

  No issues found.      "message": "Type mismatch",

```      "expected": "number",

      "got": "string"

**With Errors:**    }

```  ],

✗ Type check failed: app.ps  "warnings": []

}

Line 5: Type mismatch```

  Expected: number

  Got: string### Exit Codes

  

Line 12: Undefined variable 'x'| Code | Meaning |

  |------|---------|

2 errors found.| `0` | No errors |

```| `1` | Type errors found |

| `2` | File not found |

**JSON Output:**

```json---

{

  "file": "app.ps",## 🔧 Global Options

  "status": "error",

  "errors": [Available for all commands:

    {

      "line": 5,```bash

      "column": 10,--version    # Show TPS version

      "message": "Type mismatch",--help       # Show command help

      "expected": "number",-v           # Verbose output

      "got": "string"-q           # Quiet mode

    }```

  ],

  "warnings": []### Version Check

}

``````bash

tps-compile --version

### Exit Codes# Output: TPS 1.0.0b1

```

| Code | Meaning |

|------|---------|### Help

| `0` | No errors |

| `1` | Type errors found |```bash

| `2` | File not found |tps-compile --help

# Shows full command documentation

---```



## 🔧 Global Options---



Available for all commands:## 📁 Configuration Files



```bash### powerscript.toml

--version    # Show TPS version

--help       # Show command helpProject-level configuration:

-v           # Verbose output

-q           # Quiet mode```toml

```[project]

name = "my-project"

### Version Checkversion = "1.0.0"

entry = "src/main.ps"

```bashauthor = "Your Name"

tps-compile --versionlicense = "MIT"

# Output: TPS 1.0.0b1

```[compiler]

output_dir = "build"

### Helpstrict_types = true

target_version = "3.9"

```bashoptimize = true

tps-compile --help

# Shows full command documentation[runtime]

```include_builtins = true

async_enabled = true

---

[paths]

## 📁 Configuration Filessource = "src"

build = "build"

### powerscript.tomltests = "tests"

```

Project-level configuration:

### .powerscriptignore

```toml

[project]Exclude files from compilation:

name = "my-project"

version = "1.0.0"```gitignore

entry = "src/main.ps"# Ignore patterns

author = "Your Name"*.test.ps

license = "MIT"tests/

node_modules/

[compiler]__pycache__/

output_dir = "build"*.pyc

strict_types = true```

target_version = "3.9"

optimize = true---



[runtime]## 🔗 Command Chaining

include_builtins = true

async_enabled = true### Build Pipeline



[paths]```bash

source = "src"# Type check → Compile → Run

build = "build"tps-check app.ps && tps-compile app.ps && python app.py

tests = "tests"```

```

### Watch Mode (with external tool)

### .powerscriptignore

```bash

Exclude files from compilation:# Install nodemon

npm install -g nodemon

```gitignore

# Ignore patterns# Auto-compile on changes

*.test.psnodemon --watch src --ext ps --exec "tps-compile src/main.ps"

tests/```

node_modules/

__pycache__/### Batch Compilation

*.pyc

``````bash

# Compile all .ps files in directory

---for file in src/*.ps; do

    tps-compile "$file" -d build/

## 🔗 Command Chainingdone

```

### Build Pipeline

---

```bash

# Type check → Compile → Run## 🎯 Best Practices

tps-check app.ps && tps-compile app.ps && python app.py

```### Development Workflow



### Watch Mode (with external tool)```bash

# 1. Type check first

```bashtps-check src/main.ps

# Install nodemon

npm install -g nodemon# 2. Compile if no errors

tps-compile src/main.ps -d build/

# Auto-compile on changes

nodemon --watch src --ext ps --exec "tps-compile src/main.ps"# 3. Run compiled code

```python build/main.py

```

### Batch Compilation

### Production Build

```bash

# Compile all .ps files in directory```bash

for file in src/*.ps; do# Strict type checking + optimized build

    tps-compile "$file" -d build/tps-compile src/main.ps \

done    --strict \

```    --output-dir dist/ \

    --no-runtime

---```



## 🎯 Best Practices### Testing



### Development Workflow```bash

# Check all test files

```bashfor file in tests/*.ps; do

# 1. Type check first    tps-check "$file" || exit 1

tps-check src/main.psdone

```

# 2. Compile if no errors

tps-compile src/main.ps -d build/---



# 3. Run compiled code## 🐛 Debugging

python build/main.py

```### Verbose Output



### Production Build```bash

tps-compile app.ps -v

```bash# Shows:

# Strict type checking + optimized build# - Parsing stages

tps-compile src/main.ps \# - Type checking

    --strict \# - Code generation

    --output-dir dist/ \# - Output location

    --no-runtime```

```

### Dry Run

### Testing

```bash

```bash# Type check without compiling

# Check all test filestps-check app.ps --strict

for file in tests/*.ps; do```

    tps-check "$file" || exit 1

done---

```

## 📊 Performance Tips

---

1. **Use `--no-cache` sparingly** - Caching speeds up repeated runs

## 🐛 Debugging2. **Compile once, run many** - Prefer `tps-compile` for repeated execution

3. **Batch operations** - Compile multiple files in one command

### Verbose Output4. **Type check early** - Catch errors before compilation



```bash---

tps-compile app.ps -v

# Shows:## 🔄 Coming Soon

# - Parsing stages

# - Type checkingFuture CLI enhancements:

# - Code generation

# - Output location- 🔄 `tps watch` - Auto-compile on file changes

```- 🔄 `tps test` - Run test suite

- 🔄 `tps lint` - Code style checker

### Dry Run- 🔄 `tps format` - Auto-format code

- 🔄 `tps build` - Production builds

```bash- 🔄 `tps init` - Interactive project setup

# Type check without compiling

tps-check app.ps --strict---

```

## 🆘 Troubleshooting

---

### Command Not Found

## 📊 Performance Tips

```bash

1. **Use `--no-cache` sparingly** - Caching speeds up repeated runs# Check installation

2. **Compile once, run many** - Prefer `tps-compile` for repeated executionpip list | grep tps

3. **Batch operations** - Compile multiple files in one command

4. **Type check early** - Catch errors before compilation# Reinstall if missing

pip install --force-reinstall tps

---```



## 🔄 Coming Soon### Permission Denied



Future CLI enhancements:```bash

# On macOS/Linux, make scripts executable

- `tps watch` - Auto-compile on file changes 🔄chmod +x $(which tps-compile)

- `tps test` - Run test suite 🔄```

- `tps lint` - Code style checker 🔄

- `tps format` - Auto-format code 🔄### Import Errors

- `tps build` - Production builds 🔄

- `tps init` - Interactive project setup 🔄```bash

# Ensure TPS installed

---python -c "import powerscript; print(powerscript.__version__)"

```

## 🆘 Troubleshooting

---

### Command Not Found

## 📚 See Also

```bash

# Check installation- **[Quick Start](quickstart.md)** - Basic usage examples

pip list | grep tps- **[VS Code Extension](vscode_extension.md)** - IDE integration

- **[FAQ](faq.md)** - Common questions

# Reinstall if missing

pip install --force-reinstall tps---

```

**Master the CLI and build amazing things with PowerScript! 🚀**

### Permission Denied

```bash
# On macOS/Linux, make scripts executable
chmod +x $(which tps-compile)
```

### Import Errors

```bash
# Ensure TPS installed
python -c "import powerscript; print(powerscript.__version__)"
```

---

## 📚 See Also

- **[Quick Start](quickstart.md)** - Basic usage examples
- **[Installation](installation.md)** - Setup guide
- **[VS Code Extension](vscode_extension.md)** - IDE integration
- **[FAQ](faq.md)** - Common questions

---

<div align="center">

**Master the CLI? Build amazing things! 🚀**

</div>
