import streamlit as st
import importlib.util
import os

tools = {
    "Showcase Runner": "streamlit_ready/v1.10_showcase_runner.py",
    "Manifest Dashboard": "streamlit_ready/v1.2manifest_dashboard.py",
    "Pipeline Designer Phase 1": "streamlit_ready/v1.4_pipeline_designer_phase1.py",
    "Pipeline Designer Phase 2": "streamlit_ready/v1.5_pipeline_designer_phase2.py",
    "Cloud Bundle Exporter": "streamlit_ready/v1.9_cloud_bundle_exporter.py"
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
