import streamlit as st
import importlib.util
import os

tools = {
    "Multi-Tab Launcher": "streamlit_ready/v1.0_multi_tab_launcher.py",
    # add any other tools you have...
}

choice = st.sidebar.selectbox("🔧 Choose a Tool:", list(tools.keys()))

module_path = tools[choice]

if os.path.exists(module_path):
    spec = importlib.util.spec_from_file_location(choice, module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.run_ui()
else:
    st.error(f"❌ Tool not found: {module_path}")
