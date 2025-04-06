# streamlit_homepage.py
"""Unified dashboard with dynamic tab loading from one Streamlit app."""

import streamlit as st

st.set_page_config(page_title="🧠 Modular Assistant OS", layout="wide")
st.title("🧠 Modular Assistant OS – Multi-Tool Dashboard")

# Sidebar tool selector
tool = st.sidebar.selectbox("🔧 Choose a Tool", [
    "Multi-Tab Launcher",
    "DAG Designer",
    "Run from DAG",
    "Showcase Flow Runner",
    "Manifest Dashboard",
    "Export Pipeline Summary",
    "Export to PDF",
    "Cloud Bundle Exporter"
])

# Routing logic
if tool == "Multi-Tab Launcher":
    import streamlit_ready.multi_tab_launcher as tool_mod
elif tool == "DAG Designer":
    import streamlit_ready.pipeline_designer_phase2 as tool_mod
elif tool == "Run from DAG":
    import streamlit_ready.v2_0_run_from_dag as tool_mod
elif tool == "Showcase Flow Runner":
    import streamlit_ready.v1_10_showcase_runner as tool_mod
elif tool == "Manifest Dashboard":
    import streamlit_ready.manifest_dashboard as tool_mod
elif tool == "Export Pipeline Summary":
    import tools.v9_2_export_pipeline_summary as tool_mod
elif tool == "Export to PDF":
    import tools.v9_0_export_to_pdf as tool_mod
elif tool == "Cloud Bundle Exporter":
    import streamlit_ready.v1_9_cloud_bundle_exporter as tool_mod
else:
    st.warning("Tool not yet connected.")
    st.stop()

# Run tool (must expose run_ui() inside each file)
try:
    tool_mod.run_ui()
except AttributeError:
    st.warning("This tool doesn't have a `run_ui()` function defined.")
