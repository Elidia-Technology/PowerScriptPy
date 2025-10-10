"""
PowerScript Advanced Features - Interfaces & Abstract Classes
Extends the AST nodes to support interfaces and abstract classes
"""

from typing import List, Optional, Dict, Any
from .ast_nodes import ASTNode, ClassNode, FunctionNode, SourceLocation


class InterfaceNode(ASTNode):
    """AST node for interface declarations"""
    
    def __init__(self, name: str, methods: List[FunctionNode], 
                 location: Optional[SourceLocation] = None):
        super().__init__(location)
        self.name = name
        self.methods = methods
        self.extends: List[str] = []  # Interface inheritance
    
    def accept(self, visitor):
        return visitor.visit_interface(self)
    
    def __repr__(self):
        return f"InterfaceNode(name='{self.name}', methods={len(self.methods)})"


class AbstractClassNode(ClassNode):
    """AST node for abstract class declarations"""
    
    def __init__(self, name: str, abstract_methods: List[str] = None, **kwargs):
        super().__init__(name, **kwargs)
        self.abstract_methods = abstract_methods or []
        self.is_abstract = True
    
    def accept(self, visitor):
        return visitor.visit_abstract_class(self)
    
    def __repr__(self):
        return f"AbstractClassNode(name='{self.name}', abstract_methods={self.abstract_methods})"


class EnumNode(ASTNode):
    """AST node for enum declarations"""
    
    def __init__(self, name: str, values: List[str], 
                 location: Optional[SourceLocation] = None):
        super().__init__(location)
        self.name = name
        self.values = values
    
    def accept(self, visitor):
        return visitor.visit_enum(self)
    
    def __repr__(self):
        return f"EnumNode(name='{self.name}', values={self.values})"


class GenericConstraintNode(ASTNode):
    """AST node for generic type constraints"""
    
    def __init__(self, type_param: str, constraint: str,
                 location: Optional[SourceLocation] = None):
        super().__init__(location)
        self.type_param = type_param
        self.constraint = constraint  # extends SomeClass, implements SomeInterface
    
    def accept(self, visitor):
        return visitor.visit_generic_constraint(self)
    
    def __repr__(self):
        return f"GenericConstraintNode(type_param='{self.type_param}', constraint='{self.constraint}')"


class PatternMatchNode(ASTNode):
    """AST node for pattern matching expressions"""
    
    def __init__(self, expression: ASTNode, cases: List['MatchCaseNode'],
                 location: Optional[SourceLocation] = None):
        super().__init__(location)
        self.expression = expression
        self.cases = cases
    
    def accept(self, visitor):
        return visitor.visit_pattern_match(self)
    
    def __repr__(self):
        return f"PatternMatchNode(cases={len(self.cases)})"


class MatchCaseNode(ASTNode):
    """AST node for pattern match cases"""
    
    def __init__(self, pattern: str, guard: Optional[ASTNode], 
                 body: ASTNode, location: Optional[SourceLocation] = None):
        super().__init__(location)
        self.pattern = pattern
        self.guard = guard  # Optional when condition
        self.body = body
    
    def accept(self, visitor):
        return visitor.visit_match_case(self)
    
    def __repr__(self):
        return f"MatchCaseNode(pattern='{self.pattern}')"


class DecoratorNode(ASTNode):
    """AST node for decorator declarations"""
    
    def __init__(self, name: str, args: List[ASTNode] = None,
                 location: Optional[SourceLocation] = None):
        super().__init__(location)
        self.name = name
        self.args = args or []
    
    def accept(self, visitor):
        return visitor.visit_decorator(self)
    
    def __repr__(self):
        return f"DecoratorNode(name='{self.name}', args={len(self.args)})"