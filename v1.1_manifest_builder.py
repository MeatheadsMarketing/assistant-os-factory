import os
import json
from pathlib import Path

def validate_assistant_folder(folder: str) -> dict:
    folder = Path(folder)
    base = folder.name
    results = {
        "slug": base,
        "score": 5,
        "status": "ok",
        "files": {
            ".md": os.path.exists(folder / f"{base}.md"),
            ".py": os.path.exists(folder / f"{base}.py"),
            "manifest.json": os.path.exists(folder / "manifest.json"),
            "README.md": os.path.exists(folder / "README.md")
        }
    }
    missing = sum(1 for ok in results["files"].values() if not ok)
    results["score"] -= missing
    if missing > 0:
        results["status"] = "incomplete"
    return results

def generate_zip_manifest(base_path: str, output_path: str) -> list:
    manifest = []
    for folder in os.listdir(base_path):
        path = os.path.join(base_path, folder)
        if not os.path.isdir(path):
            continue
        result = validate_assistant_folder(path)
        try:
            with open(os.path.join(path, "manifest.json")) as f:
                meta = json.load(f)
                result.update({
                    "title": meta.get("title", result["slug"]),
                    "category": meta.get("category", "Uncategorized"),
                    "uses_gpt": meta.get("uses_gpt", False),
                    "has_run_ui": meta.get("has_run_ui", False)
                })
        except Exception:
            pass
        manifest.append(result)

    with open(output_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"✅ Manifest written: {output_path}")
    return manifest

# Example use
if __name__ == "__main__":
    base = "/content/drive/MyDrive/assistant_markdown/streamlit_ready/"
    out = "/content/drive/MyDrive/assistant_markdown/zip_manifest.json"
    generate_zip_manifest(base, out)
