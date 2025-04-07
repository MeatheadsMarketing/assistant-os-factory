import streamlit as st
import os
from datetime import datetime

st.set_page_config(page_title="🕒 Flow Scheduler", layout="wide")
st.title("🕒 Schedule a DAG to Run Later")

dag = st.selectbox("Choose DAG", ["showcase_ai_data_pipeline.json"])
run_at = st.time_input("Select Time")

if st.button("📅 Schedule DAG"):
    with open("/content/drive/MyDrive/assistant_markdown/dag_flows/scheduled_jobs.txt", "a") as f:
        f.write(f"{dag} scheduled for {run_at} at {datetime.now()}\n")
    st.success(f"Scheduled {dag} for {run_at}")
