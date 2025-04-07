# streamlit_homepage.py
"""Homepage launcher with dashboard cards, links, and navigation."""

import streamlit as st
import os

st.set_page_config(page_title="🧠 Assistant OS Factory", layout="wide")
st.title("🧠 Modular Assistant OS – Unified Launcher")

st.markdown("Welcome to the Assistant Factory. Explore the system below:")

col1, col2 = st.columns(2)

with col1:
    st.header("🚀 Launch Tools")
    st.markdown("- [Multi-Tab Launcher](./multi_tab_launcher.py)")
    st.markdown("- [DAG Designer](./pipeline_designer_phase2.py)")
    st.markdown("- [Showcase Flow Runner](./v1.10_showcase_runner.py)")
    st.markdown("- [Run from DAG](./v2.0_run_from_dag.py)")

with col2:
    st.header("📊 View & Export")
    st.markdown("- [Manifest Dashboard](./manifest_dashboard.py)")
    st.markdown("- [Export Pipeline Summary](./v9.2_export_pipeline_summary.py)")
    st.markdown("- [Export to PDF](./v9.0_export_to_pdf.py)")
    st.markdown("- [Cloud Bundle Exporter](./v1.9_cloud_bundle_exporter.py)")

st.divider()
st.markdown("Built with ❤️ using Streamlit, GPT, Colab & GitHub.")
