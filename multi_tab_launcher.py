import streamlit as st
import importlib.util
import os

st.set_page_config(page_title="Assistant Launcher", layout="wide")
st.title("🧠 Modular Assistant Launcher")

ASSISTANT_DIR = os.path.dirname(__file__)

tabs = []
modules = []

# Discover assistant modules
for folder in sorted(os.listdir(ASSISTANT_DIR)):
    folder_path = os.path.join(ASSISTANT_DIR, folder)
    if not os.path.isdir(folder_path):
        continue  # Skip files like this launcher itself

    py_files = [f for f in os.listdir(folder_path) if f.endswith(".py")]
    for py_file in py_files:
        full_path = os.path.join(folder_path, py_file)
        spec = importlib.util.spec_from_file_location(folder, full_path)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
            if hasattr(module, "run_ui"):
                tabs.append(folder.replace("_", " ").title())
                modules.append(module)
        except Exception as e:
            print(f"Error loading {folder}: {e}")

if tabs:
    selected = st.selectbox("Choose an Assistant", tabs)
    selected_index = tabs.index(selected)
    st.divider()
    modules[selected_index].run_ui()

    # GPT Suggestion Area (validated)
    with st.expander("💡 GPT Suggestion"):
        selected_title = tabs[selected_index]
        suggestion_prompt = f"""Based on this assistant, suggest a useful next assistant idea:
{selected_title}
Return only the assistant title and a one-line description."""
        st.code(suggestion_prompt, language="markdown")
else:
    st.info("No assistants with `run_ui()` found.")
