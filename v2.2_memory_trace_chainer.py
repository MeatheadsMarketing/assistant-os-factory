import streamlit as st
import os
import json
from datetime import datetime

st.set_page_config(page_title="🔗 Assistant Chain Trace", layout="wide")
st.title("🔗 Trace Memory Between Assistant Steps")

dag_path = os.path.join(os.path.dirname(__file__), "..", "dag_flows", "showcase_ai_data_pipeline.json")
trace_log_path = os.path.join(os.path.dirname(__file__), "..", "dag_flows", "trace_log.md")

if not os.path.exists(dag_path):
    st.warning("Showcase DAG not found.")
    st.stop()

with open(dag_path, "r") as f:
    flow = json.load(f)

trace_log = []
memory = ""

st.markdown("## 🔁 Simulated Chain Execution")

for step in flow:
    st.markdown(f"### 🧠 Step {step['step']}: {step['title']}")
    user_input = st.text_input(f"Input for {step['title']}", key=step['title'])
    output = f"Processed output of '{step['title']}' using: {user_input or '[empty]'}"
    st.success(f"💬 Output: {output}")
    memory += f"
[{step['title']} Output]: {output}"
    trace_log.append({"step": step['step'], "title": step['title'], "input": user_input, "output": output})

if st.button("💾 Save Trace Log"):
    with open(trace_log_path, "w") as f:
        f.write("# 🧠 Assistant Chain Execution Log

")
        f.write(f"📅 {datetime.now()}

")
        for entry in trace_log:
            f.write(f"## Step {entry['step']}: {entry['title']}
")
            f.write(f"- Input: `{entry['input']}`
")
            f.write(f"- Output: `{entry['output']}`

")
    st.success(f"✅ Saved to {trace_log_path}")
