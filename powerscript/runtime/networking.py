"""
Networking module for PowerScript
Provides basic HTTP operations
"""

import requests
from typing import Dict, Any, Optional


class HTTPClient:
    """Simple HTTP client"""
    
    def __init__(self, base_url: str = ""):
        self.base_url = base_url
        self.session = requests.Session()
    
    def get(self, url: str, params: Optional[Dict[str, Any]] = None, 
            headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """GET request"""
        full_url = self.base_url + url if self.base_url else url
        response = self.session.get(full_url, params=params, headers=headers)
        return {
            "status_code": response.status_code,
            "text": response.text,
            "json": response.json() if response.headers.get('content-type', '').startswith('application/json') else None,
            "headers": dict(response.headers)
        }
    
    def post(self, url: str, data: Optional[Dict[str, Any]] = None, 
             json: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """POST request"""
        full_url = self.base_url + url if self.base_url else url
        response = self.session.post(full_url, data=data, json=json, headers=headers)
        return {
            "status_code": response.status_code,
            "text": response.text,
            "json": response.json() if response.headers.get('content-type', '').startswith('application/json') else None,
            "headers": dict(response.headers)
        }


def create_http_client(base_url: str = "") -> HTTPClient:
    """Create an HTTP client"""
    return HTTPClient(base_url)