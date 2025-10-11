"""
GUI module for PowerScript using Tkinter
Provides basic GUI components
"""

import tkinter as tk
from tkinter import messagebox, filedialog
from typing import Callable, Any


class Window:
    """Basic window class"""
    
    def __init__(self, title: str = "PowerScript App", width: int = 400, height: int = 300):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.widgets = []
    
    def add_button(self, text: str, command: Callable[[], Any], x: int = 0, y: int = 0) -> None:
        """Add a button"""
        button = tk.Button(self.root, text=text, command=command)
        button.place(x=x, y=y)
        self.widgets.append(button)
    
    def add_label(self, text: str, x: int = 0, y: int = 0) -> None:
        """Add a label"""
        label = tk.Label(self.root, text=text)
        label.place(x=x, y=y)
        self.widgets.append(label)
    
    def add_entry(self, x: int = 0, y: int = 0) -> tk.Entry:
        """Add an entry field"""
        entry = tk.Entry(self.root)
        entry.place(x=x, y=y)
        self.widgets.append(entry)
        return entry
    
    def show_message(self, title: str, message: str, type_: str = "info") -> None:
        """Show a message box"""
        if type_ == "info":
            messagebox.showinfo(title, message)
        elif type_ == "warning":
            messagebox.showwarning(title, message)
        elif type_ == "error":
            messagebox.showerror(title, message)
    
    def run(self) -> None:
        """Start the GUI event loop"""
        self.root.mainloop()
    
    def close(self) -> None:
        """Close the window"""
        self.root.destroy()


def create_window(title: str = "PowerScript App", width: int = 400, height: int = 300) -> Window:
    """Create a new window"""
    return Window(title, width, height)