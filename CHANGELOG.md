# Changelog

All notable changes to PowerScript (TPS) will be documented in this file.

## [1.0.0] - 2025-10-10

### Added
- Initial release of Typed PowerScript (TPS)
- Complete compiler toolchain (Lexer, Parser, Transpiler)
- Full CLI tools suite (`tps`, `tps-run`, `tps-compile`, `tps-create`, `tps-build`)
- VS Code extension with LSP support
- Type system with static and runtime validation
- Access modifiers (public, private, protected)
- Modern language features:
  - F-string interpolation
  - Template literals
  - Switch/case statements
  - Arrow functions
  - Import/export system
  - Default parameters
- Auto-compilation for .ps files
- 38+ Python standard library modules support
- AI/ML integration examples
- Comprehensive documentation

### Features
- **Languages**: PowerScript (.ps files) transpiling to Python
- **Commands**: 6 easy-to-use CLI commands
- **IDE Support**: Complete VS Code integration
- **Type Safety**: Static typing with runtime validation
- **Modern Syntax**: JavaScript/ES6-inspired features
- **Python Compatibility**: 75%+ Python feature parity
- **Package Management**: Full PyPI support as `tps`

### PyPI Package
- Package name: `tps`
- Install: `pip install tps`
- Quick start: `echo 'console.log("Hello!");' > test.ps && tps-run test.ps`