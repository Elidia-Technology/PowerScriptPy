# W3Schools Python Tutorial Test Suite for PowerScript

This directory contains comprehensive PowerScript test files based on W3Schools Python tutorials.

## Purpose

These test files serve multiple purposes:
1. **Feature Documentation** - Document Python features and their PowerScript equivalents
2. **Future Implementation** - Track features not yet available in PowerScript
3. **Learning Resource** - Help developers understand both Python and PowerScript syntax
4. **Testing Framework** - Test PowerScript capabilities as features are added

## Test Files

### Basic Python Concepts
- `w3c_01_intro.ps` - Python Introduction
- `w3c_02_syntax.ps` - Python Syntax
- `w3c_03_comments.ps` - Comments (single-line, multi-line)
- `w3c_04_variables.ps` - Variables (declaration, types, naming)
- `w3c_05_data_types.ps` - Data Types (str, int, float, list, dict, bool)
- `w3c_06_numbers.ps` - Numbers (int, float, operations, conversion)
- `w3c_07_casting.ps` - Type Casting (int(), float(), str(), bool())
- `w3c_08_strings.ps` - Strings (literals, methods, formatting)
- `w3c_09_booleans.ps` - Booleans (true/false, operators, conditions)
- `w3c_10_operators.ps` - Operators (arithmetic, comparison, logical, bitwise)

### Data Structures
- `w3c_11_lists.ps` - Lists (creation, access, methods, operations)
- `w3c_12_tuples.ps` - Tuples (immutable sequences)
- `w3c_13_sets.ps` - Sets (unique elements, operations)
- `w3c_14_dictionaries.ps` - Dictionaries (key-value pairs, methods)
- `w3c_20_arrays.ps` - Arrays (list operations, multi-dimensional)
- `w3c_33_list_methods.ps` - List Methods (append, extend, sort, etc.)
- `w3c_34_dict_methods.ps` - Dictionary Methods (get, keys, values, etc.)

### Control Flow
- `w3c_15_if_else.ps` - If...Else Statements (conditions, elif, nested)
- `w3c_16_while_loops.ps` - While Loops (iteration, break, continue)
- `w3c_17_for_loops.ps` - For Loops (iteration, range, nested)

### Functions
- `w3c_18_functions.ps` - Functions (definition, parameters, return values)
- `w3c_19_lambda.ps` - Lambda Functions (anonymous functions, closures)
- `w3c_24_scope.ps` - Variable Scope (local, global, enclosing)

### Object-Oriented Programming
- `w3c_21_classes.ps` - Classes and Objects (⚠️ Limited support)
- `w3c_22_inheritance.ps` - Inheritance (⚠️ Limited support)
- `w3c_23_iterators.ps` - Iterators (⚠️ Limited support)

### Modules and Packages
- `w3c_25_modules.ps` - Modules (import, export, organization)
- `w3c_35_pip.ps` - PIP Package Manager (⚠️ Conceptual)

### Advanced Topics
- `w3c_26_dates.ps` - Date/Time Handling (⚠️ Limited support)
- `w3c_27_math.ps` - Math Operations (calculations, functions)
- `w3c_28_json.ps` - JSON (parsing, serialization)
- `w3c_29_regex.ps` - Regular Expressions (⚠️ Limited support)
- `w3c_30_try_except.ps` - Error Handling (try-catch, exceptions)
- `w3c_31_file_handling.ps` - File I/O (read, write, delete)
- `w3c_32_string_methods.ps` - String Methods (manipulation, formatting)
- `w3c_36_user_input.ps` - User Input (⚠️ Conceptual)

### W3Schools Advanced Topics
- `w3c_37_file_advanced.ps` - Advanced File Handling (modes, position, context managers)
- `w3c_38_dsa.ps` - Data Structures & Algorithms (arrays, linked lists, sorting, searching)
- `w3c_39_mysql.ps` - MySQL Database (connections, queries, CRUD operations)
- `w3c_40_mongodb.ps` - MongoDB Database (NoSQL, documents, collections)
- `w3c_41_modules_extended.ps` - Extended Modules (built-in, third-party, custom)
- `w3c_42_machine_learning.ps` - Machine Learning (scikit-learn, models, training)
- `w3c_43_matplotlib.ps` - Data Visualization (plots, charts, graphs)

## Status Legend

- ✅ **Fully Supported** - Feature works in current PowerScript version
- 🟡 **Partially Supported** - Feature works with limitations
- ⚠️ **Limited Support** - Feature has significant limitations or workarounds
- ❌ **Not Supported** - Feature not yet implemented

## Current PowerScript Limitations

### Features Requiring Workarounds
1. **Object Property Access** - Use bracket notation `obj["property"]` instead of `obj.property`
2. **Array Methods** - Use `append()` instead of `push()`, `len()` instead of `.length`
3. **Type Conversion** - Use `int()`, `float()`, `str()`, `bool()` functions
4. **String Concatenation** - Numbers must be converted: `str(num)` before concatenating

### Features Not Yet Available
1. **Class Declarations** - Traditional class syntax not fully supported
2. **Inheritance** - Class inheritance not implemented
3. **Decorators** - Python-style decorators not available
4. **Generators** - `yield` keyword not supported
5. **List Comprehensions** - Must use loops instead
6. **String Slicing** - `text[1:5]` not fully supported
7. **Multiple Assignment** - `a, b = 1, 2` not supported
8. **Tuple Unpacking** - Must access by index
9. **Context Managers** - `with` statement limited
10. **Async/Await** - Partial support

## Running Tests

### Run All W3C Tests
```bash
# Activate virtual environment
source .venv/bin/activate

# Run all tests in w3c folder
for file in test_suits/w3c/*.ps; do
    echo "Testing: $file"
    tps run "$file"
done
```

### Run Individual Test
```bash
tps run test_suits/w3c/w3c_01_intro.ps
```

### Compile Test
```bash
tps compile test_suits/w3c/w3c_01_intro.ps
```

## Expected Behavior

Many tests will:
- **Show Syntax** - Display Python syntax for reference
- **Demonstrate Concepts** - Show how features work conceptually
- **Provide Workarounds** - Show PowerScript alternatives
- **Note Limitations** - Document features not yet available

Tests use `console.log()` to show what Python code would look like and how it translates to PowerScript.

## Future Enhancements

As PowerScript evolves, these tests can be updated to:
1. Remove workarounds when features are implemented
2. Add actual executable code for conceptual features
3. Test new PowerScript-specific features
4. Benchmark performance improvements

## Contributing

When adding features to PowerScript:
1. Check relevant w3c test files
2. Update tests to use new features
3. Remove workaround notes
4. Add to "Fully Supported" list

## References

- W3Schools Python Tutorial: https://www.w3schools.com/python/
- PowerScript Documentation: See main README.md
- Python Documentation: https://docs.python.org/

## Notes

- Tests are designed to be educational and informative
- Some tests demonstrate features not yet in PowerScript
- Tests show both Python and PowerScript approaches
- Comments explain differences and limitations
- All tests should run without errors (even if showing concepts)

---

**Created:** October 11, 2025  
**Based on:** W3Schools Python Tutorial  
**PowerScript Version:** 1.0.0b1
