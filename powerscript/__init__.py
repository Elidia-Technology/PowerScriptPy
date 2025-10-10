"""
PowerScript - A fully structured development language that transpiles to Python.

This package provides:
- Lexer and Parser for PowerScript syntax
- AST to Python transpilation
- Static and runtime type checking
- CLI tools for development workflow
- LSP server for IDE support
- VS Code extension integration
"""

__version__ = "0.1.0"
__author__ = "PowerScript Team"

from .compiler import Lexer, Parser, Transpiler
from .runtime import RuntimeValidator, AccessModifiers
from .typechecker import TypeChecker, StaticAnalyzer
from .cli import CLI

__all__ = [
    "Lexer",
    "Parser", 
    "Transpiler",
    "RuntimeValidator",
    "AccessModifiers",
    "TypeChecker",
    "StaticAnalyzer",
    "CLI"
]