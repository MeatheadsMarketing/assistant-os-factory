import streamlit as st
st.set_page_config(page_title="🧠 Reflective DAG Optimizer", layout="wide")
st.title("🧠 Reflective DAG Optimizer (GPT-powered)")

import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")
dag_path = os.path.join(os.path.dirname(__file__), "..", "dag_flows", "showcase_ai_data_pipeline.json")

if not os.path.exists(dag_path):
    st.warning("Showcase DAG not found.")
    st.stop()

with open(dag_path) as f:
    flow = json.load(f)

flow_text = "\n".join([f"{s['step']}. {s['title']}" for s in flow])

st.markdown("## 📋 Original Flow")
st.code(flow_text)

if st.button("🔮 Ask GPT to Optimize Flow"):
    prompt = f"""Given this assistant DAG:

{flow_text}

Suggest a more efficient version. Add/remove/reorder steps if needed, and explain your reasoning."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )
        st.markdown("### 🔁 Optimized Flow")
        st.markdown(response.choices[0].message.content.strip())
    except Exception as e:
        st.error(str(e))
