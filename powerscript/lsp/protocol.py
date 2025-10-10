"""
PowerScript LSP Protocol Implementation

Custom protocol extensions and utilities
"""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass


@dataclass
class PowerScriptDiagnostic:
    """PowerScript-specific diagnostic information"""
    line: int
    column: int
    message: str
    severity: str  # "error", "warning", "info"
    code: Optional[str] = None
    source: str = "powerscript"


@dataclass
class PowerScriptSymbol:
    """Symbol information for LSP"""
    name: str
    kind: str  # "class", "function", "variable", "method"
    type_info: Optional[str] = None
    line: int = 0
    column: int = 0
    doc_string: Optional[str] = None


class PowerScriptLSPProtocol:
    """PowerScript-specific LSP protocol extensions"""
    
    @staticmethod
    def create_completion_item(symbol: PowerScriptSymbol) -> Dict[str, Any]:
        """Create LSP completion item from PowerScript symbol"""
        kind_map = {
            "class": 7,      # CompletionItemKind.Class
            "function": 3,   # CompletionItemKind.Function
            "method": 2,     # CompletionItemKind.Method
            "variable": 6,   # CompletionItemKind.Variable
            "keyword": 14,   # CompletionItemKind.Keyword
            "type": 25,      # CompletionItemKind.TypeParameter
        }
        
        return {
            "label": symbol.name,
            "kind": kind_map.get(symbol.kind, 1),
            "detail": symbol.type_info or "",
            "documentation": symbol.doc_string or "",
            "insertText": symbol.name,
        }
    
    @staticmethod
    def create_hover_content(symbol: PowerScriptSymbol) -> Dict[str, Any]:
        """Create LSP hover content from PowerScript symbol"""
        content = f"```powerscript\n{symbol.name}"
        if symbol.type_info:
            content += f": {symbol.type_info}"
        content += "\n```"
        
        if symbol.doc_string:
            content += f"\n\n{symbol.doc_string}"
        
        return {
            "kind": "markdown",
            "value": content
        }
    
    @staticmethod
    def create_diagnostic(diag: PowerScriptDiagnostic) -> Dict[str, Any]:
        """Create LSP diagnostic from PowerScript diagnostic"""
        severity_map = {
            "error": 1,    # DiagnosticSeverity.Error
            "warning": 2,  # DiagnosticSeverity.Warning
            "info": 3,     # DiagnosticSeverity.Information
            "hint": 4,     # DiagnosticSeverity.Hint
        }
        
        return {
            "range": {
                "start": {"line": diag.line - 1, "character": diag.column},
                "end": {"line": diag.line - 1, "character": diag.column + 100}
            },
            "message": diag.message,
            "severity": severity_map.get(diag.severity, 1),
            "source": diag.source,
            "code": diag.code
        }