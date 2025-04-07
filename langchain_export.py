import os
import json
from pathlib import Path

def export_to_langchain_tool(folder_path: str) -> dict:
    folder = Path(folder_path)
    manifest_file = folder / "manifest.json"
    if not manifest_file.exists():
        raise FileNotFoundError(f"No manifest.json found in {folder_path}")

    with open(manifest_file, "r") as f:
        data = json.load(f)

    title = data.get("title", folder.name)
    description = data.get("description", f"A LangChain-compatible tool for {title}")
    inputs = data.get("inputs", ["input"])

    return {
        "name": folder.name,
        "description": description,
        "parameters": {
            "type": "object",
            "properties": {
                inp: {
                    "type": "string",
                    "description": f"{inp} input"
                } for inp in inputs
            },
            "required": inputs
        }
    }

def export_all_to_json(base_dir: str, output_path: str):
    tools = []
    for folder in os.listdir(base_dir):
        path = os.path.join(base_dir, folder)
        if os.path.isdir(path):
            try:
                tools.append(export_to_langchain_tool(path))
            except Exception as e:
                print(f"⚠️ Skipping {folder}: {e}")

    with open(output_path, "w") as f:
        json.dump(tools, f, indent=2)
    print(f"✅ Exported {len(tools)} LangChain tools to {output_path}")
