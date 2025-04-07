import streamlit as st
import requests
import json

st.set_page_config(page_title="🌐 Trigger External Webhook", layout="wide")
st.title("🌐 Webhook Trigger on Flow Completion")

webhook_url = st.text_input("Webhook URL")
payload = {
    "event": "dag_complete",
    "status": "success",
    "pipeline": "showcase_ai_data_pipeline"
}

if st.button("🚀 Send Webhook"):
    try:
        r = requests.post(webhook_url, json=payload)
        st.success(f"Sent! Status code: {r.status_code}")
    except Exception as e:
        st.error(str(e))
