"""
PowerScript Type Checker Package

Provides static type checking functionality:
- Static type analysis
- Type inference
- Error reporting
- Integration with external type checkers
"""

from .type_checker import TypeChecker, TypeCheckResult, TypeCheckError
from .static_analyzer import StaticAnalyzer, AnalysisResult
from .type_inference import TypeInference, InferredType
from .pyright_integration import PyrightIntegration

__all__ = [
    "TypeChecker",
    "TypeCheckResult", 
    "TypeCheckError",
    "StaticAnalyzer",
    "AnalysisResult",
    "TypeInference",
    "InferredType",
    "PyrightIntegration"
]