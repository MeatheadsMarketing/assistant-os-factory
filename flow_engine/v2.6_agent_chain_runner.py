import streamlit as st
import json
import os

st.set_page_config(page_title="🧠 Agent Chain Launcher", layout="wide")
st.title("🧠 Run Assistants as an Agent Chain")

dag_file = os.path.join(os.path.dirname(__file__), "..", "dag_flows", "showcase_ai_data_pipeline.json")

if not os.path.exists(dag_file):
    st.warning("DAG file not found.")
    st.stop()

with open(dag_file) as f:
    flow = json.load(f)

st.markdown("## 🔗 Agent Chain Simulation")
for step in flow:
    title = step["title"]
    user_input = st.text_input(f"🔹 Input for `{title}`", key=title)
    response = f"[Simulated output from {title}] using input: {user_input or '[none]'}"
    st.success(response)
