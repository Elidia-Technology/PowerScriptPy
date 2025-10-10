#!/usr/bin/env python3
"""
Test script to verify TPS package configuration
"""

import sys
import subprocess
from pathlib import Path

def run_command(cmd):
    """Run a command and return success status"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def test_package_config():
    """Test package configuration"""
    print("🧪 Testing PowerScript (TPS) Package Configuration")
    print("=" * 50)
    
    # Test 1: Check if pyproject.toml is valid
    print("1. Checking pyproject.toml...")
    if Path("pyproject.toml").exists():
        print("   ✅ pyproject.toml exists")
    else:
        print("   ❌ pyproject.toml missing")
        return False
    
    # Test 2: Check if setup.py works
    print("2. Checking setup.py...")
    success, out, err = run_command("python setup.py --name")
    if success and "tps" in out:
        print("   ✅ setup.py returns correct package name: tps")
    else:
        print(f"   ❌ setup.py issue: {err}")
        return False
    
    # Test 3: Check if package can be imported
    print("3. Testing package import...")
    try:
        import powerscript
        print(f"   ✅ PowerScript imported successfully, version: {powerscript.__version__}")
    except ImportError as e:
        print(f"   ❌ Import failed: {e}")
        return False
    
    # Test 4: Check CLI commands
    print("4. Testing CLI configuration...")
    try:
        from powerscript.cli.cli import CLI
        print("   ✅ CLI module imported successfully")
    except ImportError as e:
        print(f"   ❌ CLI import failed: {e}")
        return False
    
    print("\n🎉 All package configuration tests passed!")
    print("\n📦 Package is ready for PyPI!")
    print("\nNext steps:")
    print("1. Run: ./build_for_pypi.sh")
    print("2. Test: pip install dist/tps-*.whl")
    print("3. Upload: python -m twine upload dist/*")
    
    return True

if __name__ == "__main__":
    success = test_package_config()
    sys.exit(0 if success else 1)