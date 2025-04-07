import streamlit as st
import importlib.util
import os
import json
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Smart Assistant Launcher", layout="wide")
st.title("🧠 Modular Assistant Launcher")

ASSISTANT_DIR = os.path.dirname(__file__)
tabs = []
modules = []
summaries = []

# Discover assistant modules
for folder in sorted(os.listdir(ASSISTANT_DIR)):
    folder_path = os.path.join(ASSISTANT_DIR, folder)
    if os.path.isdir(folder_path):
        manifest_path = os.path.join(folder_path, "manifest.json")
        py_files = [f for f in os.listdir(folder_path) if f.endswith(".py")]

        summary = {"title": folder.replace("_", " ").title(), "gpt": False, "ui": False, "folder": folder}
        if os.path.exists(manifest_path):
            with open(manifest_path) as f:
                data = json.load(f)
                summary["title"] = data.get("title", summary["title"])
                summary["gpt"] = data.get("uses_gpt", False)
                summary["ui"] = data.get("has_run_ui", False)

        for py_file in py_files:
            full_path = os.path.join(folder_path, py_file)
            spec = importlib.util.spec_from_file_location(folder, full_path)
            module = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(module)
                if hasattr(module, "run_ui"):
                    tabs.append(summary["title"])
                    modules.append(module)
                    summaries.append(summary)
            except Exception as e:
                print(f"Error loading {folder}: {e}")

if tabs:
    selected = st.selectbox("Choose an Assistant", tabs)
    selected_index = tabs.index(selected)
    st.divider()
    
    st.markdown(f"**Folder:** `{summaries[selected_index]['folder']}`")
    st.markdown("### ✅ Validation")
    col1, col2, col3 = st.columns(3)
    col1.success("Has `run_ui()`") if summaries[selected_index]["ui"] else col1.error("Missing `run_ui()`")
    col2.info("Uses GPT") if summaries[selected_index]["gpt"] else col2.warning("No GPT reference")
    col3.success("Manifest Found")

    # GPT Suggestion Area
    folder_path = os.path.join(ASSISTANT_DIR, summaries[selected_index]["folder"])
    md_file = next((f for f in os.listdir(folder_path) if f.endswith(".md")), None)

    if md_file:
        st.divider()
        st.markdown("### 💡 GPT Suggestions")
        with open(os.path.join(folder_path, md_file)) as f:
            md_content = f.read()

        if st.button("🔮 Suggest Next Assistant"):
            try:
                suggestion_prompt = f"Based on this assistant, suggest a useful next assistant idea:

{md_content}"
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": suggestion_prompt}],
                    temperature=0.5
                )
                st.success(response.choices[0].message.content.strip())
            except Exception as e:
                st.error(f"GPT error: {e}")
else:
    st.info("No assistants with `run_ui()` found.")
