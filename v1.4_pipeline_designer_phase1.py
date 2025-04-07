import streamlit as st
import json
import os
import pandas as pd

st.set_page_config(page_title="🧱 DAG Flow Builder", layout="wide")
st.title("🧱 Assistant DAG Flow Builder")

manifest_path = os.path.join(os.path.dirname(__file__), "zip_manifest.json")
dag_save_dir = os.path.join(os.path.dirname(__file__), "..", "dag_flows")
os.makedirs(dag_save_dir, exist_ok=True)

if not os.path.exists(manifest_path):
    st.warning("⚠️ zip_manifest.json not found.")
    st.stop()

# Load assistant manifest
with open(manifest_path, "r") as f:
    manifest = json.load(f)

# DAG Design UI
st.markdown("## 📋 Build Your Assistant Flow")

assistant_titles = [item["title"] for item in manifest]
dag_name = st.text_input("Flow Name", value="my_dag_flow")
flow = []

col1, col2 = st.columns([1, 2])
with col1:
    st.markdown("### 🔧 Add Node")
    selected = st.selectbox("Select Assistant", assistant_titles)
    if st.button("➕ Add to Flow"):
        flow.append({"step": len(flow)+1, "title": selected})

with col2:
    st.markdown("### 🧠 Current Flow")
    if flow:
        for step in flow:
            st.markdown(f"**Step {step['step']}:** {step['title']}")
    else:
        st.info("No steps added yet.")

# Save Flow
if flow and st.button("💾 Save Flow"):
    dag_path = os.path.join(dag_save_dir, f"{dag_name}.json")
    with open(dag_path, "w") as f:
        json.dump(flow, f, indent=2)
    st.success(f"Flow saved to `{dag_path}`")
