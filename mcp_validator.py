import argparse
import os
import sys
import json
import yaml
import requests
from jsonschema import validate, ValidationError

# Load MCP schema (can also be remote or included in package)
MCP_SCHEMA_PATH = "schemas/mcp.schema.json"
REQUIRED_ENDPOINTS = ["/invoke", "/.well-known/mcp.yaml"]
OPTIONAL_ENDPOINTS = ["/status", "/sse"]


def load_yaml_file(path):
    try:
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Failed to load YAML: {e}")
        sys.exit(1)


def load_json_schema(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Failed to load schema: {e}")
        sys.exit(1)


def validate_mcp_yaml(mcp_yaml, schema):
    try:
        validate(instance=mcp_yaml, schema=schema)
        print("✅ mcp.yaml is valid")
    except ValidationError as e:
        print(f"❌ mcp.yaml validation failed: {e.message}")
        sys.exit(1)


def check_required_fields(mcp_yaml):
    required = ["id", "name", "version", "description", "auth"]
    for field in required:
        if field not in mcp_yaml:
            print(f"❌ Missing required field in mcp.yaml: {field}")
            sys.exit(1)
    print("✅ All required fields are present in mcp.yaml")


def check_naming_convention(service_id):
    if not service_id.startswith("mcp-"):
        print("❌ Service ID does not follow naming convention 'mcp-<team>-<function>'")
        sys.exit(1)
    print("✅ Naming convention is valid")


def check_endpoints(base_url):
    for endpoint in REQUIRED_ENDPOINTS:
        url = base_url + endpoint
        try:
            response = requests.get(url)
            if response.status_code != 200:
                print(f"❌ Endpoint {endpoint} not reachable (HTTP {response.status_code})")
                sys.exit(1)
            print(f"✅ Endpoint {endpoint} reachable")
        except Exception as e:
            print(f"❌ Error reaching endpoint {endpoint}: {e}")
            sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Validate an MCP server for compliance.")
    parser.add_argument("--base-url", required=True, help="Base URL of the MCP server, e.g. http://localhost:8000")
    parser.add_argument("--yaml-path", default=".well-known/mcp.yaml", help="Path to mcp.yaml file")
    parser.add_argument("--schema-path", default=MCP_SCHEMA_PATH, help="Path to MCP JSON schema")

    args = parser.parse_args()

    mcp_yaml = load_yaml_file(args.yaml_path)
    schema = load_json_schema(args.schema_path)

    validate_mcp_yaml(mcp_yaml, schema)
    check_required_fields(mcp_yaml)
    check_naming_convention(mcp_yaml["id"])
    check_endpoints(args.base_url)

    print("🎉 MCP service passed all validation checks.")


if __name__ == "__main__":
    main()
