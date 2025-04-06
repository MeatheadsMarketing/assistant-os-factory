# streamlit_homepage.py
"""Final unified dashboard launcher with validated tool paths."""

import streamlit as st
import os

st.set_page_config(page_title="🧠 Modular Assistant OS", layout="wide")
st.title("🧠 Modular Assistant OS – Multi-Tool Dashboard")

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
    "Run from DAG",
    "Showcase Flow Runner",
    "Manifest Dashboard",
    "Export Pipeline Summary",
    "Export to PDF",
    "Cloud Bundle Exporter",
    "Agent Trace Replay",
    "GPT Suggest Next Tool",
    "Streamlit UI Template",
    "Colab Flow Orchestrator",
    "Validation Status Highlighter",
    "Recent Activity Viewer",
    "Agent Flow Builder UI",
    "Agent Evaluator",
])

tool_paths = {
    "Multi-Tab Launcher": "streamlit_ready/v1.0_multi_tab_launcher.py",
    "DAG Designer": "streamlit_ready/v1.5_pipeline_designer_phase2.py",
    "Run from DAG": "streamlit_ready/v2.0_run_from_dag.py",
    "Showcase Flow Runner": "streamlit_ready/v1.10_showcase_runner.py",
    "Manifest Dashboard": "streamlit_ready/manifest_dashboard.py",
    "Export Pipeline Summary": "tools/v9.2_export_pipeline_summary.py",
    "Export to PDF": "tools/v9.0_export_to_pdf.py",
    "Cloud Bundle Exporter": "streamlit_ready/v1.9_cloud_bundle_exporter.py",
    "Agent Trace Replay": "tools/v6.8_agent_trace_replay_ui.py",
    "GPT Suggest Next Tool": "tools/v6.7_gpt_suggest_next.py",
    "Streamlit UI Template": "tools/v5.0_streamlit_ui_template.py",
    "Colab Flow Orchestrator": "tools/v5.9_colab_flow_orchestrator.py",
    "Validation Status Highlighter": "tools/v10.7_validation_status_highlighter.py",
    "Recent Activity Viewer": "tools/v10.5_recent_activity_viewer.py",
    "Agent Flow Builder UI": "tools/v6.9_agent_flow_builder_ui.py",
    "Agent Evaluator": "agent_core/v4.4_agent_evaluator.py",
}

run_external(tool_paths.get(tool))
