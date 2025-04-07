import os
import json
import streamlit as st

st.set_page_config(page_title="🧠 Assistant Agent Wrapper", layout="wide")
st.title("🧠 Auto-Agent Wrapper")

base_dir = os.path.join(os.path.dirname(__file__), "..", "streamlit_ready")
assistant_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

selected = st.selectbox("Select Assistant to Wrap", assistant_dirs)

if selected:
    manifest_path = os.path.join(base_dir, selected, "manifest.json")
    if not os.path.exists(manifest_path):
        st.warning("No manifest.json found.")
        st.stop()

    with open(manifest_path) as f:
        manifest = json.load(f)

    tool = {
        "name": selected,
        "description": manifest.get("description", selected),
        "parameters": {
            "type": "object",
            "properties": {
                i: {"type": "string", "description": f"{i} input"}
                for i in manifest.get("inputs", ["input"])
            },
            "required": manifest.get("inputs", ["input"])
        }
    }

    st.markdown("### 🧩 GPT/Function Tool Schema")
    st.json(tool)

    if st.button("💾 Save Agent Tool"):
        path = os.path.join(base_dir, selected, "tool.json")
        with open(path, "w") as f:
            json.dump(tool, f, indent=2)
        st.success(f"Saved: {path}")
