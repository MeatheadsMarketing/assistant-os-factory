import streamlit as st
import os
import json

st.set_page_config(page_title="🎉 Showcase Flow Runner", layout="wide")
st.title("🎉 Public Showcase: Modular Assistant Flow")

dag_path = os.path.join(os.path.dirname(__file__), "..", "dag_flows", "showcase_ai_data_pipeline.json")

if not os.path.exists(dag_path):
    st.warning("No showcase DAG found.")
    st.stop()

with open(dag_path, "r") as f:
    flow = json.load(f)

st.markdown("## 📋 Flow Preview")
for step in flow:
    st.markdown(f"- **Step {step['step']}:** {step['title']}")

if st.button("▶️ Simulate Flow Run"):
    st.markdown("## 🚀 Simulated Execution Log")
    for step in flow:
        st.success(f"✅ Executing: {step['title']}")

    st.balloons()
    st.success("🎯 Showcase flow complete.")
