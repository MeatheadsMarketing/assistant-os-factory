# streamlit_homepage.py
"""Final unified launcher with assistant tools, DAG runners, and index viewer."""

import streamlit as st
import os

st.set_page_config(page_title="🧠 Modular Assistant OS", layout="wide")
st.title("🧠 Modular Assistant OS – Dashboard Launcher")

def run_external(path):
    if not os.path.exists(path):
        st.warning(f"❌ Tool not found: `{path}`")
        return
    with open(path) as f:
        code = f.read()
    exec(code, globals())

tool = st.sidebar.selectbox("🔧 Choose a Tool", [
    "Multi-Tab Launcher",
    "DAG Designer",
    "Run from DAG JSON",
    "DAG Index Selector",
    "Showcase Flow Runner",
    "Manifest Dashboard",
    "Export Pipeline Summary",
    "Export to PDF",
    "Cloud Bundle Exporter"
])

tool_paths = {
    "Multi-Tab Launcher": "v1.0_multi_tab_launcher.py",
    "DAG Designer": "v1.5_pipeline_designer_phase2.py",
    "Run from DAG JSON": "v2.0_run_from_dag.py",
    "DAG Index Selector": "dag_selector_runner.py",
    "Showcase Flow Runner": "v1.10_showcase_runner.py",
    "Manifest Dashboard": "manifest_dashboard.py",
    "Export Pipeline Summary": "v9.2_export_pipeline_summary.py",
    "Export to PDF": "v9.0_export_to_pdf.py",
    "Cloud Bundle Exporter": "v1.9_cloud_bundle_exporter.py"
}

run_external(tool_paths.get(tool))
