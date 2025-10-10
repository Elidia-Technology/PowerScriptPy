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

from typing import Any, List, Dict, Union, Optional
from .file_system import FileSystem, JSONFile, CSVFile, FileStream, FileError
import sys
import json
import math
import random
import time
import datetime
import re


class Console:
    """Console I/O operations"""
    
    @staticmethod
    def log(*args, sep: str = ' ', end: str = '\n'):
        """Print to console (equivalent to console.log)"""
        __builtins__['print'](*args, sep=sep, end=end)
    
    @staticmethod
    def error(*args, sep: str = ' ', end: str = '\n'):
        """Print to stderr"""
        __builtins__['print'](*args, sep=sep, end=end, file=sys.stderr)
    
    @staticmethod
    def warn(*args, sep: str = ' ', end: str = '\n'):
        """Print warning to stderr"""
        print("WARNING:", *args, sep=sep, end=end, file=sys.stderr)
    
    @staticmethod
    def input(prompt: str = "") -> str:
        """Get user input"""
        return __builtins__['input'](prompt)
    
    @staticmethod
    def clear():
        """Clear console (platform specific)"""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')


class File:
    """File operations built-in class"""
    
    @staticmethod
    def read_text(path: str, encoding: str = 'utf-8') -> str:
        """Read file as text"""
        return FileSystem.read_text(path, encoding)
    
    @staticmethod
    def write_text(path: str, content: str, encoding: str = 'utf-8') -> None:
        """Write text to file"""
        FileSystem.write_text(path, content, encoding)
    
    @staticmethod
    def append_text(path: str, content: str, encoding: str = 'utf-8') -> None:
        """Append text to file"""
        FileSystem.append_text(path, content, encoding)
    
    @staticmethod
    def read_lines(path: str, encoding: str = 'utf-8') -> List[str]:
        """Read file as lines"""
        return FileSystem.read_lines(path, encoding)
    
    @staticmethod
    def write_lines(path: str, lines: List[str], encoding: str = 'utf-8') -> None:
        """Write lines to file"""
        FileSystem.write_lines(path, lines, encoding)
    
    @staticmethod
    def exists(path: str) -> bool:
        """Check if file exists"""
        return FileSystem.exists(path)
    
    @staticmethod
    def delete(path: str) -> None:
        """Delete file"""
        FileSystem.delete_file(path)
    
    @staticmethod
    def copy(src: str, dst: str) -> None:
        """Copy file"""
        FileSystem.copy_file(src, dst)
    
    @staticmethod
    def move(src: str, dst: str) -> None:
        """Move/rename file"""
        FileSystem.move_file(src, dst)
    
    @staticmethod
    def size(path: str) -> int:
        """Get file size"""
        return FileSystem.get_size(path)
    
    @staticmethod
    def modified_time(path: str) -> float:
        """Get last modified time"""
        return FileSystem.get_modified_time(path)
    
    @staticmethod
    def read_json(path: str) -> Any:
        """Read JSON file"""
        return JSONFile.read(path)
    
    @staticmethod
    def write_json(path: str, data: Any, indent: int = 2) -> None:
        """Write JSON file"""
        JSONFile.write(path, data, indent)
    
    @staticmethod
    def read_csv(path: str, has_header: bool = True) -> List[Dict[str, str]]:
        """Read CSV file"""
        return CSVFile.read(path, has_header)
    
    @staticmethod
    def write_csv(path: str, data: List[Dict[str, Any]], fieldnames: Optional[List[str]] = None) -> None:
        """Write CSV file"""
        CSVFile.write(path, data, fieldnames)


class Directory:
    """Directory operations built-in class"""
    
    @staticmethod
    def create(path: str) -> None:
        """Create directory"""
        FileSystem.create_directory(path)
    
    @staticmethod
    def delete(path: str, recursive: bool = False) -> None:
        """Delete directory"""
        FileSystem.delete_directory(path, recursive)
    
    @staticmethod
    def exists(path: str) -> bool:
        """Check if directory exists"""
        return FileSystem.is_directory(path)
    
    @staticmethod
    def list(path: str) -> List[str]:
        """List directory contents"""
        return FileSystem.list_directory(path)
    
    @staticmethod
    def list_files(path: str, pattern: str = "*") -> List[str]:
        """List files in directory"""
        return FileSystem.list_files(path, pattern)
    
    @staticmethod
    def list_directories(path: str) -> List[str]:
        """List subdirectories"""
        return FileSystem.list_directories(path)
    
    @staticmethod
    def current() -> str:
        """Get current directory"""
        return FileSystem.get_current_directory()
    
    @staticmethod
    def change(path: str) -> None:
        """Change current directory"""
        FileSystem.set_current_directory(path)


class Path:
    """Path manipulation utilities"""
    
    @staticmethod
    def join(*parts: str) -> str:
        """Join path components"""
        return FileSystem.join_path(*parts)
    
    @staticmethod
    def absolute(path: str) -> str:
        """Get absolute path"""
        return FileSystem.get_absolute_path(path)
    
    @staticmethod
    def parent(path: str) -> str:
        """Get parent directory"""
        return FileSystem.get_parent_directory(path)
    
    @staticmethod
    def filename(path: str) -> str:
        """Get filename"""
        return FileSystem.get_filename(path)
    
    @staticmethod
    def extension(path: str) -> str:
        """Get file extension"""
        return FileSystem.get_file_extension(path)
    
    @staticmethod
    def name_without_extension(path: str) -> str:
        """Get filename without extension"""
        return FileSystem.get_filename_without_extension(path)
    
    @staticmethod
    def exists(path: str) -> bool:
        """Check if path exists"""
        return FileSystem.exists(path)
    
    @staticmethod
    def is_file(path: str) -> bool:
        """Check if path is file"""
        return FileSystem.is_file(path)
    
    @staticmethod
    def is_directory(path: str) -> bool:
        """Check if path is directory"""
        return FileSystem.is_directory(path)


class Math:
    """Math utilities"""
    
    PI = math.pi
    E = math.e
    
    @staticmethod
    def abs(x: float) -> float:
        return abs(x)
    
    @staticmethod
    def ceil(x: float) -> int:
        return math.ceil(x)
    
    @staticmethod
    def floor(x: float) -> int:
        return math.floor(x)
    
    @staticmethod
    def round(x: float, digits: int = 0) -> float:
        return round(x, digits)
    
    @staticmethod
    def sqrt(x: float) -> float:
        return math.sqrt(x)
    
    @staticmethod
    def pow(x: float, y: float) -> float:
        return math.pow(x, y)
    
    @staticmethod
    def min(*args) -> float:
        return min(args)
    
    @staticmethod
    def max(*args) -> float:
        return max(args)
    
    @staticmethod
    def random() -> float:
        return random.random()
    
    @staticmethod
    def random_int(min_val: int, max_val: int) -> int:
        return random.randint(min_val, max_val)


class DateTime:
    """Date and time utilities"""
    
    @staticmethod
    def now() -> float:
        """Get current timestamp"""
        return time.time()
    
    @staticmethod
    def format(timestamp: float, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
        """Format timestamp as string"""
        return datetime.datetime.fromtimestamp(timestamp).strftime(format_str)
    
    @staticmethod
    def parse(date_str: str, format_str: str = "%Y-%m-%d %H:%M:%S") -> float:
        """Parse date string to timestamp"""
        return datetime.datetime.strptime(date_str, format_str).timestamp()
    
    @staticmethod
    def sleep(seconds: float) -> None:
        """Sleep for specified seconds"""
        time.sleep(seconds)


class JSON:
    """JSON utilities"""
    
    @staticmethod
    def parse(json_str: str) -> Any:
        """Parse JSON string"""
        return json.loads(json_str)
    
    @staticmethod
    def stringify(obj: Any, indent: int = None) -> str:
        """Convert object to JSON string"""
        return json.dumps(obj, indent=indent, ensure_ascii=False)


class RegExp:
    """Regular expression utilities"""
    
    @staticmethod
    def match(pattern: str, text: str, flags: int = 0) -> Optional[List[str]]:
        """Find first match"""
        match = re.search(pattern, text, flags)
        return list(match.groups()) if match else None
    
    @staticmethod
    def match_all(pattern: str, text: str, flags: int = 0) -> List[List[str]]:
        """Find all matches"""
        return [list(match.groups()) for match in re.finditer(pattern, text, flags)]
    
    @staticmethod
    def replace(pattern: str, replacement: str, text: str, flags: int = 0) -> str:
        """Replace matches"""
        return re.sub(pattern, replacement, text, flags=flags)
    
    @staticmethod
    def split(pattern: str, text: str, flags: int = 0) -> List[str]:
        """Split by pattern"""
        return re.split(pattern, text, flags=flags)
    
    @staticmethod
    def test(pattern: str, text: str, flags: int = 0) -> bool:
        """Test if pattern matches"""
        return bool(re.search(pattern, text, flags))


# Built-in functions that can be called directly
def print(*args, sep: str = ' ', end: str = '\n'):
    """Print to console"""
    Console.log(*args, sep=sep, end=end)

def input(prompt: str = "") -> str:
    """Get user input"""
    return Console.input(prompt)

def len(obj) -> int:
    """Get length of object"""
    return obj.__len__() if hasattr(obj, '__len__') else 0

def str(obj) -> str:
    """Convert to string"""
    return obj.__str__() if hasattr(obj, '__str__') else repr(obj)

def int(obj):
    """Convert to integer"""
    return __builtins__['int'](obj)

def float(obj):
    """Convert to float"""
    return __builtins__['float'](obj)

def bool(obj):
    """Convert to boolean"""
    return __builtins__['bool'](obj)


# Global built-in objects
_fs = FileSystem()
_console = Console()

BUILT_IN_GLOBALS = {
    # File system operations  
    'FileSystem': FileSystem,
    'file_write': _fs.write_text,
    'file_read': _fs.read_text,
    'file_append': _fs.append_text,
    'file_exists': _fs.exists,
    'file_delete': _fs.delete_file,
    'file_copy': _fs.copy_file,
    'file_move': _fs.move_file,
    'file_size': _fs.get_size,
    'file_modified_time': _fs.get_modified_time,
    'file_stream': FileStream,
    'dir_create': _fs.create_directory,
    'dir_delete': _fs.delete_directory,
    'dir_exists': _fs.exists,
    'dir_list': _fs.list_directory,
    'path_join': _fs.join_path,
    'path_absolute': _fs.get_absolute_path,
    'temp_file_create': _fs.create_temp_file,
    'temp_dir_create': _fs.create_temp_directory,
    'json_write': JSONFile.write,
    'json_read': JSONFile.read,
    'csv_write': CSVFile.write,
    'csv_read': CSVFile.read,
    
    # Classes
    'Console': Console,
    'File': File,
    'Directory': Directory,
    'Path': Path,
    'Math': Math,
    'DateTime': DateTime,
    'JSON': JSON,
    'RegExp': RegExp,
    'FileStream': FileStream,
    'FileError': FileError,
    
    # Functions
    'console': _console,
    'range': range,
    'print': print,
    'input': input,
    'len': len,
    'str': str,
    'int': int,
    'float': float,
    'bool': bool,
    
    # Constants
    'PI': math.pi,
    'E': math.e,
    'Infinity': float('inf'),
    'NaN': float('nan'),
}

# Export all built-ins to module globals
globals().update(BUILT_IN_GLOBALS)