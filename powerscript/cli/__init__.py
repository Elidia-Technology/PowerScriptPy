"""
PowerScript CLI Package

Provides command-line interface tools:
- powerscriptc: Compiler command
- ps-run: Run PowerScript files
- ps-create: Create new projects  
- psc: Type checker command
"""

from .cli import CLI, main
from .commands import CompileCommand, RunCommand, CreateCommand, CheckCommand
from .project_creator import ProjectCreator

__all__ = [
    "CLI",
    "main",
    "CompileCommand",
    "RunCommand", 
    "CreateCommand",
    "CheckCommand",
    "ProjectCreator"
]