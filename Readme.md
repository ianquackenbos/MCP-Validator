# MCP Validator

A Python CLI tool to validate MCP-compatible services against internal guidelines.

## Features

- Validates `.well-known/mcp.yaml` using a defined JSON Schema
- Checks for required fields and naming conventions
- Confirms that required endpoints are reachable

## Installation

To install locally for testing:

```bash
pip install .

Usage
Run it from your terminal like this:
mcp-check --base-url http://localhost:8000


Or run directly with Python:
python mcp_validator.py --base-url http://localhost:8000

Project Structure
mcp-validator/
├── mcp_validator.py
├── setup.py
├── requirements.txt
├── README.md
└── schemas/
    └── mcp.schema.json
