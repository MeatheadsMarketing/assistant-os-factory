# dag_selector_runner.py
"""Streamlit UI for selecting and running DAG flows using dag_index.json."""

import streamlit as st
import json
import os

st.set_page_config(page_title="🧩 DAG Flow Selector", layout="wide")
st.title("🧩 DAG Pipeline Selector + Runner")

index_path = "dag_index.json"

if not os.path.exists(index_path):
    st.error("❌ dag_index.json not found.")
    st.stop()

with open(index_path) as f:
    dag_index = json.load(f)

# Sidebar selector
dag_names = [d["name"] for d in dag_index]
selected = st.selectbox("📂 Choose a DAG to view or run", dag_names)

# Show info
selected_dag = next(d for d in dag_index if d["name"] == selected)
st.subheader(f"📄 `{selected_dag['name']}`")
st.markdown(f"**Description:** {selected_dag['description']}")
st.markdown(f"**Tags:** `{', '.join(selected_dag['tags'])}`")

# Optional trigger
if st.button("▶️ Run DAG"):
    st.success(f"Running `{selected_dag['name']}`...")
    # Replace with actual DAG execution logic here

st.divider()
st.markdown("To customize this DAG or create new ones, edit files in `/dag_flows/`")
