from setuptools import setup

setup(
    name="mcp-validator",
    version="0.1.0",
    py_modules=["mcp_validator"],
    install_requires=[
        "PyYAML",
        "jsonschema",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "mcp-check=mcp_validator:main",
        ],
    },
    author="Your Name",
    description="Validator for MCP-compatible services",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
