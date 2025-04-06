# streamlit_homepage.py
"""Fixed homepage launcher with working external links to deployed apps."""

import streamlit as st

st.set_page_config(page_title="🧠 Assistant OS Factory", layout="wide")
st.title("🧠 Modular Assistant OS – Unified Launcher")

st.markdown("Welcome to the Assistant Factory. Explore the system below:")

col1, col2 = st.columns(2)

with col1:
    st.header("🚀 Launch Tools")
    st.markdown("- [Multi-Tab Launcher](https://assistant-os-factory.streamlit.app/)")
    st.markdown("- [DAG Designer](https://assistant-os-factory-dagdesigner.streamlit.app/)")
    st.markdown("- [Showcase Flow Runner](https://assistant-os-factory-showcase.streamlit.app/)")
    st.markdown("- [Run from DAG](https://assistant-os-factory-runner.streamlit.app/)")

with col2:
    st.header("📊 View & Export")
    st.markdown("- [Manifest Dashboard](https://assistant-os-factory-manifest.streamlit.app/)")
    st.markdown("- [Export Pipeline Summary](https://assistant-os-factory-summary.streamlit.app/)")
    st.markdown("- [Export to PDF](https://assistant-os-factory-pdf.streamlit.app/)")
    st.markdown("- [Cloud Bundle Exporter](https://assistant-os-factory-export.streamlit.app/)")

st.divider()
st.markdown("Built with ❤️ using Streamlit, GPT, Colab & GitHub.")
