# streamlit_homepage.py
"""Unified dashboard launcher with confirmed tools for Streamlit Cloud deployment."""

import streamlit as st
import os

st.set_page_config(page_title="🧠 Assistant OS Dashboard", layout="wide")
st.title("🧠 Modular Assistant OS – Clean Launcher")

def run_external(path):
    if not os.path.exists(path):
        st.warning(f"❌ Tool not found: `{path}`")
        return
    with open(path) as f:
        code = f.read()
    exec(code, globals())

tool = st.sidebar.selectbox("🔧 Choose a Tool", [
    "v1.0_multi_tab_launcher.py",
    "v1.5_pipeline_designer_phase2.py",
    "v1.10_showcase_runner.py",
    "manifest_dashboard.py",
    "v1.9_cloud_bundle_exporter.py",
    "v5.0_streamlit_ui_template.py",
    "v5.9_colab_flow_orchestrator.py",
    "v10.7_validation_status_highlighter.py",
    "v10.5_recent_activity_viewer.py",
    "v6.9_agent_flow_builder_ui.py",
    "v4.4_agent_evaluator.py"
])

run_external(tool)
