"""
MIT License

Copyright (c) 2025 Saleem Ahmad (Elite India Org Team)
Email: team@eliteindia.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import argparse
import sys
import os
from typing import List, Optional
from .commands import CompileCommand, RunCommand, CreateCommand, CheckCommand


class CLI:
    """Main CLI class for PowerScript"""
    
    def __init__(self):
        self.parser = self._create_parser()
        self.commands = {
            'compile': CompileCommand(),
            'run': RunCommand(),
            'create': CreateCommand(),
            'check': CheckCommand()
        }
    
    def _create_parser(self) -> argparse.ArgumentParser:
        """Create the main argument parser"""
        parser = argparse.ArgumentParser(
            prog='powerscript',
            description='PowerScript - A fully structured development language that transpiles to Python',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Commands:
  compile (c)     Compile PowerScript files to Python
  run (r)         Run PowerScript files directly
  create          Create a new PowerScript project
  check           Run type checker on PowerScript files

Examples:
  powerscript compile src/ -o build/
  powerscript run src/main.ps
  powerscript create my_project
  powerscript check src/
            """
        )
        
        parser.add_argument(
            '--version', '-v',
            action='version',
            version='PowerScript 0.1.0'
        )
        
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        
        # Compile command
        compile_parser = subparsers.add_parser(
            'compile', aliases=['c'],
            help='Compile PowerScript files to Python'
        )
        compile_parser.add_argument(
            'source',
            help='Source file or directory to compile'
        )
        compile_parser.add_argument(
            '-o', '--output',
            default='build/',
            help='Output directory (default: build/)'
        )
        compile_parser.add_argument(
            '-w', '--watch',
            action='store_true',
            help='Watch for file changes and recompile'
        )
        compile_parser.add_argument(
            '--strict',
            action='store_true',
            help='Enable strict type checking'
        )
        compile_parser.add_argument(
            '--no-runtime-checks',
            action='store_true',
            help='Disable runtime type checks'
        )
        compile_parser.add_argument(
            '--generate-stubs',
            action='store_true',
            help='Generate .pyi stub files'
        )
        
        # Run command
        run_parser = subparsers.add_parser(
            'run', aliases=['r'],
            help='Run PowerScript files directly'
        )
        run_parser.add_argument(
            'file',
            help='PowerScript file to run'
        )
        run_parser.add_argument(
            'args',
            nargs='*',
            help='Arguments to pass to the script'
        )
        run_parser.add_argument(
            '--no-cache',
            action='store_true',
            help='Don\'t use cached compiled files'
        )
        
        # Create command
        create_parser = subparsers.add_parser(
            'create',
            help='Create a new PowerScript project'
        )
        create_parser.add_argument(
            'name',
            help='Project name'
        )
        create_parser.add_argument(
            '--template',
            choices=['basic', 'ai', 'web', 'cli'],
            default='basic',
            help='Project template (default: basic)'
        )
        create_parser.add_argument(
            '--no-git',
            action='store_true',
            help='Don\'t initialize git repository'
        )
        
        # Check command
        check_parser = subparsers.add_parser(
            'check',
            help='Run type checker on PowerScript files'
        )
        check_parser.add_argument(
            'source',
            help='Source file or directory to check'
        )
        check_parser.add_argument(
            '--strict',
            action='store_true',
            help='Enable strict type checking'  
        )
        check_parser.add_argument(
            '--json',
            action='store_true',
            help='Output results in JSON format'
        )
        
        return parser
    
    def run(self, args: Optional[List[str]] = None) -> int:
        """Run the CLI with given arguments"""
        if args is None:
            args = sys.argv[1:]
        
        try:
            parsed_args = self.parser.parse_args(args)
            
            if not parsed_args.command:
                self.parser.print_help()
                return 1
            
            # Map aliases to full command names
            command_name = parsed_args.command
            if command_name == 'c':
                command_name = 'compile'
            elif command_name == 'r':
                command_name = 'run'
            
            command = self.commands.get(command_name)
            if not command:
                print(f"Unknown command: {command_name}", file=sys.stderr)
                return 1
            
            return command.execute(parsed_args)
            
        except KeyboardInterrupt:
            print("\nOperation cancelled by user", file=sys.stderr)
            return 130
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1


def main() -> int:
    """Main entry point for PowerScript CLI"""
    cli = CLI()
    return cli.run()


# Entry points for different commands
def powerscriptc_main() -> int:
    """Entry point for powerscriptc command"""
    sys.argv[0] = 'powerscriptc'
    args = ['compile'] + sys.argv[1:]
    cli = CLI()
    return cli.run(args)


def ps_run_main() -> int:
    """Entry point for ps-run command"""
    sys.argv[0] = 'ps-run'
    args = ['run'] + sys.argv[1:]
    cli = CLI()
    return cli.run(args)


def ps_create_main() -> int:
    """Entry point for ps-create command"""
    sys.argv[0] = 'ps-create'
    args = ['create'] + sys.argv[1:]
    cli = CLI()
    return cli.run(args)


def psc_main() -> int:
    """Entry point for psc (type checker) command"""
    sys.argv[0] = 'psc'
    args = ['check'] + sys.argv[1:]
    cli = CLI()
    return cli.run(args)


if __name__ == '__main__':
    sys.exit(main())