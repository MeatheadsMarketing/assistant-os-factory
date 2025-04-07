import streamlit as st
import importlib.util
import os

HEAD
st.set_page_config(page_title="Assistant Launcher", layout="wide")
st.title("🧠 Modular Assistant Launcher")

# ✅ Cloud-safe directory fix
ASSISTANT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))

tabs = []
modules = []

# Discover assistant modules
for folder in sorted(os.listdir(ASSISTANT_DIR)):
    folder_path = os.path.join(ASSISTANT_DIR, folder)
    if not os.path.isdir(folder_path):
        continue

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

    with st.expander("💡 GPT Suggestion"):
        selected_title = tabs[selected_index]
        suggestion_prompt = f"""Based on this assistant, suggest a useful next assistant idea:
{selected_title}
Return only the assistant title and a one-line description."""
        st.code(suggestion_prompt, language="markdown")

else:
    st.info("No assistants with `run_ui()` found.")

tools = {
    "Showcase Runner": "streamlit_ready/v1.10_showcase_runner.py",
    "Manifest Dashboard": "streamlit_ready/manifest_dashboard.py",
    "Pipeline Designer Phase 1": "streamlit_ready/pipeline_designer_phase1.py",
    "Pipeline Designer Phase 2": "streamlit_ready/pipeline_designer_phase2.py",
    "Cloud Bundle Exporter": "streamlit_ready/v1.9_cloud_bundle_exporter.py"
}

choice = st.sidebar.selectbox("🛠 Choose a Tool", list(tools.keys()))

module_path = tools[choice]

if os.path.exists(module_path):
    spec = importlib.util.spec_from_file_location(choice, module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.run_ui()
else:
    st.error(f"❌ Tool not found: {module_path}")
 5f7d951 (🚀 Initial commit including fixed multi_tab_launcher)
