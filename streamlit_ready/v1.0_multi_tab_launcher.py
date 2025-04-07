import streamlit as st
import importlib.util
import os

tools = {
    "Showcase Runner": "v1.10_showcase_runner.py",
    "Manifest Dashboard": "manifest_dashboard.py",
    "Pipeline Designer Phase 1": "pipeline_designer_phase1.py",
    "Pipeline Designer Phase 2": "pipeline_designer_phase2.py",
    "Cloud Bundle Exporter": "v1.9_cloud_bundle_exporter.py"
}

choice = st.sidebar.selectbox("🛠 Choose a Tool:", list(tools.keys()))

module_path = os.path.join(os.path.dirname(__file__), tools[choice])

if os.path.exists(module_path):
    spec = importlib.util.spec_from_file_location(choice, module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.run_ui()
else:
    st.error(f"❌ Tool not found: {module_path}")
