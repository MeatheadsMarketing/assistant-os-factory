import os
import json
from pathlib import Path
from typing import Dict, List

REQUIRED_FILES = ["README.md", "manifest.json"]

def validate_assistant_folder(folder: str) -> Dict:
    result = {
        "path": folder,
        "status": "ok",
        "files": {},
        "score": 5
    }

    folder = Path(folder)
    base_name = folder.name

    md_path = folder / f"{base_name}.md"
    py_path = folder / f"{base_name}.py"
    manifest_path = folder / "manifest.json"
    readme_path = folder / "README.md"

    result["files"][".md"] = os.path.exists(md_path)
    result["files"][".py"] = os.path.exists(py_path)
    result["files"]["manifest.json"] = os.path.exists(manifest_path)
    result["files"]["README.md"] = os.path.exists(readme_path)

    missing_count = sum(1 for exists in result["files"].values() if not exists)
    result["score"] = 5 - missing_count

    if missing_count > 0:
        result["status"] = "incomplete"

    return result

def load_manifest(path: str) -> Dict:
    try:
        with open(path) as f:
            return json.load(f)
    except:
        return {}

def display_validation(result: Dict):
    from IPython.display import Markdown, display

    display(Markdown(f"### 🔍 Validation for `{result['path']}`"))
    for file, exists in result["files"].items():
        mark = "✅" if exists else "❌"
        display(Markdown(f"- {mark} `{file}`"))
    display(Markdown(f"- **Score:** {result['score']}/5"))
    display(Markdown(f"- **Status:** `{result['status']}`"))

def generate_zip_manifest(base_dir: str) -> List[Dict]:
    manifest = []
    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)
        if os.path.isdir(folder_path):
            validation = validate_assistant_folder(folder_path)
            assistant_manifest = {
                "slug": folder,
                "score": validation["score"],
                "status": validation["status"],
                "files": validation["files"]
            }
            full_manifest_path = os.path.join(folder_path, "manifest.json")
            if os.path.exists(full_manifest_path):
                raw_manifest = load_manifest(full_manifest_path)
                assistant_manifest.update({
                    "title": raw_manifest.get("title", folder),
                    "category": raw_manifest.get("category", "Uncategorized"),
                    "uses_gpt": raw_manifest.get("uses_gpt", False),
                    "has_run_ui": raw_manifest.get("has_run_ui", False)
                })
            manifest.append(assistant_manifest)

    return manifest
