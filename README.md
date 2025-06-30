 ___  _   _  ___  ___   __  __   ___  ___  __   __      _  _     _        _             
 / __|| | | |/ __|| __| |  \/  | / __|| _ \ \ \ / /__ _ | |(_) __| | __ _ | |_  ___  _ _ 
 \__ \| |_| |\__ \| _|  | |\/| || (__ |  _/  \ V // _` || || |/ _` |/ _` ||  _|/ _ \| '_|
 |___/ \___/ |___/|___| |_|  |_| \___||_|     \_/ \__,_||_||_|\__,_|\__,_| \__|\___/|_|  
                                                                                         
                             


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
