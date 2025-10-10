"""
PowerScript Pyright Integration

Integrates with the Pyright type checker for enhanced type checking
"""

import subprocess
import json
from typing import List, Dict, Any, Optional
from pathlib import Path


class PyrightIntegration:
    """Integration with Pyright type checker"""
    
    def __init__(self):
        self.pyright_available = self._check_pyright_available()
    
    def _check_pyright_available(self) -> bool:
        """Check if Pyright is available"""
        try:
            subprocess.run(['pyright', '--version'], capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def check_python_file(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """Run Pyright on a Python file"""
        if not self.pyright_available:
            return None
        
        try:
            result = subprocess.run(
                ['pyright', '--outputjson', str(file_path)],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.stdout:
                return json.loads(result.stdout)
            
        except (subprocess.CalledProcessError, json.JSONDecodeError):
            pass
        
        return None