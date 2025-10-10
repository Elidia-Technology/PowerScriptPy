"""
PowerScript - A fully structured development language that transpiles to Python

Setup script for installing PowerScript
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="powerscript",
    version="0.1.0",
    description="A fully structured development language that transpiles to Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="PowerScript Team",
    author_email="team@powerscript.dev",
    url="https://github.com/powerscript/powerscript",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Compilers",
        "Topic :: Software Development :: Code Generators",
    ],
    python_requires=">=3.8",
    install_requires=[
        "beartype>=0.10.0",
        "lark>=1.1.0",
        "watchdog>=2.1.0",
        "rich>=10.0.0",
        "click>=8.0.0",
        "typing-extensions>=4.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.10.0",
            "black>=21.0.0",
            "flake8>=3.8.0",
            "mypy>=0.910",
        ],
        "lsp": [
            "pygls>=0.11.0",
            "pyright>=1.1.0",
        ],
        "ai": [
            "numpy>=1.21.0",
            "pandas>=1.3.0",
            "scikit-learn>=1.0.0",
            "torch>=1.9.0",
        ],
        "web": [
            "flask>=2.0.0",
            "fastapi>=0.70.0",
            "uvicorn>=0.15.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "powerscript=powerscript.cli.cli:main",
            "powerscriptc=powerscript.cli.cli:powerscriptc_main",
            "ps-run=powerscript.cli.cli:ps_run_main",
            "ps-create=powerscript.cli.cli:ps_create_main",
            "psc=powerscript.cli.cli:psc_main",
        ],
    },
    include_package_data=True,
    package_data={
        "powerscript": [
            "vscode-extension/**/*",
            "examples/**/*",
            "docs/**/*",
        ],
    },
    keywords="powerscript python transpiler compiler language ai",
    project_urls={
        "Bug Reports": "https://github.com/powerscript/powerscript/issues",
        "Source": "https://github.com/powerscript/powerscript",
        "Documentation": "https://powerscript.dev/docs",
    },
)