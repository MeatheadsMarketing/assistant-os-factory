import streamlit as st
import os
import json

st.set_page_config(page_title="⚙️ DAG Executor", layout="wide")
st.title("⚙️ Run Assistant DAG")

dag_dir = os.path.join(os.path.dirname(__file__), "..", "dag_flows")
dag_files = [f for f in os.listdir(dag_dir) if f.endswith(".json")]

selected_dag = st.selectbox("Select a DAG to Execute", dag_files)

if selected_dag:
    with open(os.path.join(dag_dir, selected_dag)) as f:
        flow = json.load(f)

    st.markdown("## 🔁 Execution Preview")
    for step in flow:
        st.markdown(f"- **{step['step']}:** {step['title']}")

    if st.button("▶️ Run DAG (Mock Execution)"):
        st.markdown("## ✅ Execution Log")
        for step in flow:
            st.success(f"Executed: {step['title']}")
        st.balloons()
