import json
import os

def assistant_to_tool_schema(manifest_path):
    with open(manifest_path) as f:
        data = json.load(f)

    return {
        "name": data.get("title", "assistant"),
        "description": data.get("description", "Assistant tool"),
        "parameters": {
            "type": "object",
            "properties": {
                inp: {"type": "string", "description": f"{inp} input"}
                for inp in data.get("inputs", ["input"])
            },
            "required": data.get("inputs", ["input"])
        }
    }
