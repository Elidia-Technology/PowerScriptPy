#!/bin/bash
# Build script for PyPI release

set -e

echo "🚀 Building PowerScript (TPS) for PyPI..."

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf build/
rm -rf dist/
rm -rf *.egg-info/

# Build the package
echo "📦 Building package..."
python -m build

# Check the package
echo "🔍 Checking package..."
python -m twine check dist/*

echo "✅ Build complete!"
echo ""
echo "📦 Distribution files:"
ls -la dist/
echo ""
echo "🚀 To upload to PyPI:"
echo "   Test PyPI: python -m twine upload --repository testpypi dist/*"
echo "   Real PyPI: python -m twine upload dist/*"
echo ""
echo "✨ Install locally to test:"
echo "   pip install dist/tps-1.0.0-py3-none-any.whl"