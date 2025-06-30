  _____ _    _  _____ ______ 
 / ____| |  | |/ ____|  ____|
| (___ | |  | | (___ | |__   
 \___ \| |  | |\___ \|  __|  
 ____) | |__| |____) | |____ 
|_____/ \____/|_____/|______|
                             


# MCP Validator

A Python CLI tool to validate MCP-compatible services against internal guidelines.

## Features

- Validates structure and schema of `.well-known/mcp.yaml`
- Ensures naming conventions and endpoint availability
- Checks presence of required fields and correct auth metadata
- Easy integration into CI/CD pipelines

## Usage

```bash
pip install .
mcp-check --base-url http://localhost:8000
