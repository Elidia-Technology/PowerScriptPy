# PowerScript Issues & Bugs Tracker

**Last Updated:** October 11, 2025  
**Total Issues:** 25  
**Critical:** 3 | **Major:** 7 | **Minor:** 10 | **Enhancement:** 5

---

## 🔴 Critical Issues (Priority 1)

### Issue #1: Build Directory Cleanup Fails Automation
**Status:** 🔴 Open  
**Priority:** Critical  
**Severity:** High  
**Component:** Build System  
**Impact:** Breaks CI/CD and automated builds

**Description:**
When running `rm -rf build/*`, the system prompts for user confirmation, breaking automated scripts.

**Location:**
- Build scripts
- Any automation that calls cleanup

**Error:**
```bash
zsh: sure you want to delete all 7 files in /Users/mac/WorkSpace/PowerScriptPy/build [yn]?
```

**Solution:**
1. Add `-f` flag to force deletion without prompt
2. Create dedicated cleanup script
3. Update build automation

**Code Fix:**
```bash
# Before
rm -rf build/*

# After
rm -rf build/* 2>/dev/null || true
# OR
python -c "import shutil; shutil.rmtree('build', ignore_errors=True)"
```

**Affected Files:**
- `build_for_pypi.sh`
- Any CI/CD scripts
- Development workflows

**Assignee:** Unassigned  
**Estimate:** 1 hour  
**Labels:** `bug`, `critical`, `build-system`

---

### Issue #2: Union Type Edge Cases Fail Validation
**Status:** 🔴 Open  
**Priority:** Critical  
**Severity:** High  
**Component:** Type Checker  
**Impact:** Runtime errors slip through type checking

**Description:**
Complex union types with mixed literal and base types fail validation:
```typescript
type Status = string | number | "special" | 200 | null;
```

**Location:**
- `powerscript/typechecker/type_checker.py`
- Lines: ~100-200 (union type handling)

**Reproduction:**
```typescript
type ID = string | number;
type SpecialID = ID | "default" | 0;

function test(id: SpecialID): void {
    console.log(id);
}

test("default");  // Should work
test(0);          // Should work
test("abc");      // Should work
test(123);        // Should work
test(null);       // Should fail but doesn't
```

**Root Cause:**
Type checker doesn't properly flatten nested unions or handle mixed literal/base types.

**Solution:**
1. Implement union type normalization
2. Add literal type subsumption logic
3. Improve union type comparison algorithm

**Tests Needed:**
- Union with literals
- Nested unions
- Mixed base + literal types
- Intersection with unions

**Assignee:** Unassigned  
**Estimate:** 1 week  
**Labels:** `bug`, `critical`, `type-system`

---

### Issue #3: Import Resolution Fails on Relative Paths
**Status:** 🔴 Open  
**Priority:** Critical  
**Severity:** Medium  
**Component:** Transpiler  
**Impact:** Module loading errors in complex projects

**Description:**
Relative imports may fail when transpiling multi-file projects:
```typescript
// file: src/utils/helpers.ps
export function helper() { }

// file: src/main.ps
import { helper } from "./utils/helpers";  // Fails
```

**Location:**
- `powerscript/compiler/transpiler.py`
- Method: `visit_import()`
- Lines: ~870-900

**Error:**
```
ModuleNotFoundError: No module named 'utils.helpers'
```

**Root Cause:**
Transpiler doesn't properly resolve relative paths to Python-compatible imports.

**Solution:**
1. Implement proper path resolution algorithm
2. Convert relative paths to absolute Python imports
3. Handle different project structures
4. Add source root configuration

**Affected Files:**
- `transpiler.py`
- Import test cases

**Assignee:** Unassigned  
**Estimate:** 3 days  
**Labels:** `bug`, `critical`, `transpiler`, `imports`

---

## 🟠 Major Issues (Priority 2)

### Issue #4: LSP Server Crashes on Complex Files
**Status:** 🟠 Open  
**Priority:** Major  
**Severity:** High  
**Component:** LSP Server  
**Impact:** VS Code integration unreliable

**Description:**
LSP server crashes when parsing files with complex type annotations or large class hierarchies.

**Location:**
- `powerscript/lsp/server.py`
- `powerscript/lsp/handlers.py`

**Reproduction:**
1. Open large .ps file (>500 lines)
2. Add complex generic types
3. LSP server stops responding

**Stack Trace:**
```python
Traceback (most recent call last):
  File "powerscript/lsp/server.py", line 123
  RecursionError: maximum recursion depth exceeded
```

**Solution:**
1. Add recursion limit checks
2. Implement incremental parsing
3. Add error recovery mechanisms
4. Improve performance for large files

**Assignee:** Unassigned  
**Estimate:** 2 weeks  
**Labels:** `bug`, `major`, `lsp`, `stability`

---

### Issue #5: Parser Error Messages Are Cryptic
**Status:** 🟠 Open  
**Priority:** Major  
**Severity:** Medium  
**Component:** Parser  
**Impact:** Poor developer experience

**Description:**
Parser errors lack context and helpful suggestions:

**Current:**
```
ParseError: Expected '}' after class body. Got IDENTIFIER at line 45, column 5
```

**Should Be:**
```
ParseError: Expected '}' to close class body (opened at line 32)
         Got 'myFunction' at line 45, column 5
         
  32 | class MyClass {
     |               ^ class body started here
  ...
  45 |     myFunction()
     |     ^^^^^^^^^^ unexpected identifier
     
Suggestion: Did you forget to close the class body with '}'?
```

**Location:**
- `powerscript/compiler/parser.py`
- Method: `_error()`, `_consume()`
- Lines: 1385-1395

**Solution:**
1. Add error context (surrounding code)
2. Track opening braces/brackets
3. Provide suggestions
4. Show related locations
5. Color-code error messages

**Files to Update:**
- `parser.py` - Error handling
- `lexer.py` - Source tracking
- `ast_nodes.py` - Location info

**Assignee:** Unassigned  
**Estimate:** 1 week  
**Labels:** `enhancement`, `major`, `parser`, `dx`

---

### Issue #6: Switch/Case Break Statement Handling
**Status:** 🟠 Open  
**Priority:** Major  
**Severity:** Medium  
**Component:** Transpiler  
**Impact:** Unexpected behavior in switch statements

**Description:**
Break statements are filtered out during switch transpilation, which may cause unexpected fall-through behavior.

**Location:**
- `powerscript/compiler/transpiler.py`
- Method: `visit_switch()`
- Line: ~715

**Code:**
```python
# Current implementation filters out breaks
case_body = [stmt for stmt in case_statements if not isinstance(stmt, ast.Break)]
```

**Issue:**
This assumes all cases fall through, but PowerScript should respect explicit breaks.

**Solution:**
1. Preserve break statements
2. Add fall-through annotation
3. Warn on implicit fall-through
4. Document switch behavior

**Test Cases Needed:**
```typescript
switch (x) {
    case 1:
        console.log("one");
        break;  // Should stop here
    case 2:
        console.log("two");
        // Fall through intended
    case 3:
        console.log("two or three");
        break;
}
```

**Assignee:** Unassigned  
**Estimate:** 2 days  
**Labels:** `bug`, `major`, `transpiler`, `control-flow`

---

### Issue #7: Generic Type Constraints Not Enforced
**Status:** 🟠 Open  
**Priority:** Major  
**Severity:** Medium  
**Component:** Type Checker  
**Impact:** Type safety compromised

**Description:**
Generic type constraints are parsed but not validated:

```typescript
interface HasLength {
    length: number;
}

function getLength<T extends HasLength>(item: T): number {
    return item.length;
}

getLength([1, 2, 3]);     // Should work
getLength("hello");       // Should work
getLength(123);           // Should ERROR but doesn't
```

**Location:**
- `powerscript/typechecker/type_checker.py`
- Generic constraint validation (missing)

**Solution:**
1. Implement constraint checking
2. Validate type parameter bounds
3. Add structural typing for interfaces
4. Test inheritance chains

**Assignee:** Unassigned  
**Estimate:** 1 week  
**Labels:** `bug`, `major`, `type-system`, `generics`

---

### Issue #8: Access Modifier Runtime Enforcement Bypassable
**Status:** 🟠 Open  
**Priority:** Major  
**Severity:** Low  
**Component:** Runtime  
**Impact:** Encapsulation not guaranteed

**Description:**
Private/protected members can be accessed using Python's name mangling workarounds:

```typescript
class MyClass {
    private secret: string = "hidden";
}

const obj = new MyClass();
// In Python: obj._MyClass__secret still accessible
```

**Location:**
- `powerscript/runtime/access_modifiers.py`

**Reality Check:**
This is a Python limitation. Cannot be fully fixed without custom import hooks.

**Solution:**
1. Document limitation in README
2. Add runtime warnings
3. Consider property-based access control
4. Use `__slots__` for better encapsulation

**Assignee:** Unassigned  
**Estimate:** 3 days  
**Labels:** `limitation`, `major`, `runtime`, `oop`

---

### Issue #9: Template Literal Nested Interpolation
**Status:** 🟠 Open  
**Priority:** Major  
**Severity:** Low  
**Component:** Parser/Transpiler  
**Impact:** Edge cases may fail

**Description:**
Nested template literals with complex expressions not fully tested:

```typescript
const x = 5;
const y = 10;
const msg = `Result: ${`${x} + ${y} = ${x + y}`}`;
```

**Location:**
- `powerscript/compiler/parser.py` - Template literal parsing
- `powerscript/compiler/transpiler.py` - Template literal transpilation

**Solution:**
1. Add comprehensive tests
2. Handle nested template literals
3. Test edge cases (escaped backticks, newlines, etc.)
4. Document limitations if any

**Assignee:** Unassigned  
**Estimate:** 2 days  
**Labels:** `bug`, `major`, `parser`, `transpiler`

---

### Issue #10: File Path Cross-Platform Compatibility
**Status:** 🟠 Open  
**Priority:** Major  
**Severity:** Medium  
**Component:** File System  
**Impact:** Windows compatibility issues

**Description:**
File path operations may fail on Windows due to hardcoded `/` separators.

**Location:**
- `powerscript/runtime/file_system.py`
- Path manipulation functions

**Solution:**
1. Use `os.path.join()` everywhere
2. Test on Windows
3. Use `pathlib.Path` for modern path handling
4. Add Windows-specific tests

**Test Scenarios:**
- Windows absolute paths (`C:\Users\...`)
- Unix absolute paths (`/home/...`)
- Relative paths on both platforms
- UNC paths (`\\server\share`)

**Assignee:** Unassigned  
**Estimate:** 1 week  
**Labels:** `bug`, `major`, `file-system`, `cross-platform`

---

## 🟡 Minor Issues (Priority 3)

### Issue #11: CLI Help Text Formatting
**Status:** 🟡 Open  
**Priority:** Minor  
**Severity:** Low  
**Component:** CLI  
**Impact:** Cosmetic

**Description:**
CLI help text could be better formatted with colors and examples.

**Location:**
- `powerscript/cli/cli.py`
- Help text strings

**Enhancement:**
```python
# Add rich formatting
from rich.console import Console
console = Console()
console.print("[bold green]PowerScript CLI[/bold green]")
```

**Assignee:** Unassigned  
**Estimate:** 2 hours  
**Labels:** `enhancement`, `minor`, `cli`, `ui`

---

### Issue #12: Snippet Placeholder Values Generic
**Status:** 🟡 Open  
**Priority:** Minor  
**Severity:** Low  
**Component:** VS Code Extension  
**Impact:** User experience

**Description:**
Code snippets use generic placeholders like `${1:param}` - could be more descriptive.

**Location:**
- `powerscript/vscode-extension/snippets/powerscript.json`

**Enhancement:**
```json
{
  "class": {
    "prefix": "class",
    "body": [
      "class ${1:ClassName} {",
      "    constructor(${2:params}) {",
      "        ${3:// Initialize}",
      "    }",
      "}"
    ]
  }
}
```

**Assignee:** Unassigned  
**Estimate:** 1 hour  
**Labels:** `enhancement`, `minor`, `vscode`, `snippets`

---

### Issue #13: README Too Long
**Status:** 🟡 Open  
**Priority:** Minor  
**Severity:** Low  
**Component:** Documentation  
**Impact:** Navigation

**Description:**
README.md is 913 lines - should be split into multiple docs.

**Solution:**
1. Create `docs/` directory
2. Split into:
   - README.md (overview, quick start)
   - FEATURES.md (feature list)
   - INSTALLATION.md (install guide)
   - EXAMPLES.md (code examples)
   - API.md (API reference)

**Assignee:** Unassigned  
**Estimate:** 4 hours  
**Labels:** `documentation`, `minor`, `organization`

---

### Issue #14-20: Additional Minor Issues
*(Listed for tracking, details available on request)*

- #14: Type annotation coverage incomplete (40% missing)
- #15: Magic numbers in lexer token patterns
- #16: Circular dependency warnings (compiler ↔ typechecker)
- #17: Global state in some components
- #18: Inconsistent naming conventions (mixed snake_case/camelCase)
- #19: Missing docstrings in ~40% of functions
- #20: Code duplication in file operations error handling

---

## 💡 Enhancement Requests (Priority 4)

### Enhancement #21: REPL Mode
**Status:** 💡 Idea  
**Priority:** Enhancement  
**Component:** CLI  
**Impact:** Developer experience

**Description:**
Add interactive REPL for quick testing:
```bash
$ tps repl
PowerScript REPL v1.0.0
>>> let x = 5;
>>> console.log(x * 2);
10
>>> 
```

**Assignee:** Unassigned  
**Estimate:** 2 weeks  
**Labels:** `enhancement`, `feature`, `repl`

---

### Enhancement #22: Jupyter Kernel Integration
**Status:** 💡 Idea  
**Priority:** Enhancement  
**Component:** Integration  
**Impact:** Data science workflows

**Description:**
Create Jupyter kernel for PowerScript notebooks.

**Benefits:**
- Use PowerScript in Jupyter
- Mix with Python cells
- AI/ML prototyping

**Assignee:** Unassigned  
**Estimate:** 3 weeks  
**Labels:** `enhancement`, `feature`, `jupyter`, `ai-ml`

---

### Enhancement #23: Watch Mode Performance
**Status:** 💡 Idea  
**Priority:** Enhancement  
**Component:** Compiler  
**Impact:** Development speed

**Description:**
Optimize watch mode to only recompile changed files, not entire project.

**Current:** Full recompile on any change  
**Desired:** Incremental compilation  

**Assignee:** Unassigned  
**Estimate:** 1 week  
**Labels:** `enhancement`, `performance`, `watch-mode`

---

### Enhancement #24: Package Registry
**Status:** 💡 Idea  
**Priority:** Enhancement  
**Component:** Ecosystem  
**Impact:** Community growth

**Description:**
Create PowerScript package registry similar to npm.

**Features:**
- Package publishing
- Dependency management
- Version resolution
- Documentation hosting

**Assignee:** Unassigned  
**Estimate:** 3 months  
**Labels:** `enhancement`, `feature`, `ecosystem`, `major`

---

### Enhancement #25: Debugging Support
**Status:** 💡 Idea  
**Priority:** Enhancement  
**Component:** VS Code Extension  
**Impact:** Developer experience

**Description:**
Add VS Code debugging support:
- Breakpoints
- Step through code
- Variable inspection
- Call stack
- Watch expressions

**Requires:**
- Debug adapter protocol implementation
- Source map generation
- VS Code debug extension

**Assignee:** Unassigned  
**Estimate:** 1 month  
**Labels:** `enhancement`, `feature`, `vscode`, `debugging`

---

## 📊 Issue Statistics

### By Priority
- 🔴 Critical: 3 (12%)
- 🟠 Major: 7 (28%)
- 🟡 Minor: 10 (40%)
- 💡 Enhancement: 5 (20%)

### By Component
- Type System: 4
- Transpiler: 4
- Parser: 3
- LSP: 2
- Runtime: 2
- CLI: 2
- VS Code: 3
- Documentation: 2
- Other: 3

### By Status
- 🔴 Open: 20 (80%)
- 🟡 In Progress: 0 (0%)
- ✅ Closed: 0 (0%)
- 💡 Idea/Future: 5 (20%)

### Estimated Effort
- Critical fixes: 2-3 weeks
- Major fixes: 6-8 weeks
- Minor fixes: 2-3 weeks
- Enhancements: 4-6 months

---

## 🎯 Issue Resolution Plan

### Week 1-2: Critical Issues
- [ ] Fix build cleanup (#1)
- [ ] Fix union type validation (#2)
- [ ] Fix import resolution (#3)

### Week 3-4: Major Bugs
- [ ] Stabilize LSP server (#4)
- [ ] Improve error messages (#5)
- [ ] Fix switch/case breaks (#6)

### Month 2: Type System
- [ ] Generic constraints (#7)
- [ ] Advanced type inference
- [ ] Static analysis improvements

### Month 3: Quality & Polish
- [ ] Minor bug fixes (#11-20)
- [ ] Documentation improvements
- [ ] Cross-platform testing (#10)

### Future: Enhancements
- [ ] REPL mode (#21)
- [ ] Jupyter kernel (#22)
- [ ] Watch mode optimization (#23)
- [ ] Debugging support (#25)

---

## 📝 Issue Reporting Guidelines

### Bug Report Template
```markdown
**Title:** Brief description

**Environment:**
- OS: macOS/Windows/Linux
- PowerScript version: 1.0.0b1
- Python version: 3.11

**Description:**
Clear description of the bug

**Reproduction Steps:**
1. Step 1
2. Step 2
3. Expected result
4. Actual result

**Code Sample:**
```typescript
// Minimal reproducible example
```

**Error Message:**
```
Full error output
```

**Additional Context:**
Any other relevant information
```

### Feature Request Template
```markdown
**Title:** Feature name

**Use Case:**
Why is this feature needed?

**Proposed Solution:**
How should it work?

**Alternatives:**
Other ways to solve the problem

**Priority:**
Low/Medium/High

**Complexity:**
Easy/Medium/Hard
```

---

## 🔗 Related Documents

- [Master Development Plan](./MASTER_DEVELOPMENT_PLAN.md)
- [Project Status](./PROJECT_STATUS.md)
- [README](./README.md)
- [Contributing Guide](./CONTRIBUTING.md) *(to be created)*

---

**Document maintained by:** Development Team  
**Update Frequency:** Weekly  
**Next Review:** October 18, 2025
