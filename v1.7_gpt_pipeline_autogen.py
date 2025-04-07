import streamlit as st
import openai
import os
import json

st.set_page_config(page_title="🤖 GPT Auto-Chain Generator", layout="wide")
st.title("🤖 GPT-Powered Assistant Flow Generator")

# Load API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")

st.markdown("Describe your goal, and GPT will suggest a full assistant sequence.")
goal_prompt = st.text_area("🧠 What do you want to accomplish?", placeholder="e.g., Clean, validate, and export a messy CSV...")

if st.button("🔮 Generate Flow") and goal_prompt:
    prompt = f"""
You are an AI pipeline assistant. Given the user goal:
"""
{goal_prompt}
"""

Suggest a sequence of assistant steps that would achieve this. 
Output as a list of assistant titles with 1-line descriptions, like:

1. Assistant Title — Description
2. Assistant Title — Description
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )
        output = response.choices[0].message.content.strip()
        st.markdown("### 🧠 Suggested Pipeline")
        st.code(output)

        if st.button("💾 Save to `/dag_flows/`"):
            flow_name = st.text_input("Flow File Name", "gpt_pipeline", key="save_name")
            save_path = f"/content/drive/MyDrive/assistant_markdown/dag_flows/{flow_name}.md"
            with open(save_path, "w") as f:
                f.write(output)
            st.success(f"Flow saved to {save_path}")

    except Exception as e:
        st.error(f"❌ Error from OpenAI: {e}")
