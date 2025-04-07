import streamlit as st
from streamlit_dag import Dag, Task
import openai
import os

st.set_page_config(page_title="🧠 GPT DAG Builder", layout="wide")
st.title("🧠 DAG Flow Builder – Phase 2: GPT Enhancements")

# --- SETUP ---
openai.api_key = os.getenv("OPENAI_API_KEY", "sk-REPLACE_ME")  # Use your actual key or load from env

CATEGORY_STYLES = {
    "Data Cleaning": {"color": "#4BA3C7", "icon": "🧹"},
    "Data Structuring": {"color": "#FFD166", "icon": "🧱"},
    "Data Enrichment": {"color": "#EF476F", "icon": "✨"},
    "Validation & QA": {"color": "#06D6A0", "icon": "✅"},
    "Export": {"color": "#118AB2", "icon": "📤"},
    "Uncategorized": {"color": "#CCCCCC", "icon": "❓"},
}

# --- SIDEBAR: GPT GOAL FLOW ---
st.sidebar.title("🪄 GPT Auto-Builder")
goal = st.sidebar.text_input("Describe your pipeline goal:")
if st.sidebar.button("⚡ Generate DAG from Goal"):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{
                "role": "user",
                "content": f"Given the goal '{goal}', suggest a 3-5 step assistant pipeline with titles and categories."
            }],
            temperature=0.4
        )
        st.session_state['gpt_dag_result'] = response.choices[0].message.content.strip()
    except Exception as e:
        st.sidebar.error(f"GPT error: {e}")

if 'gpt_dag_result' in st.session_state:
    st.sidebar.markdown("### 🧠 Suggested Flow:")
    st.sidebar.code(st.session_state['gpt_dag_result'])

# --- MOCKED DATA (later replaced by dynamic flow)
assistants = [
    {"id": "clean_nulls", "title": "Clean Nulls", "category": "Data Cleaning"},
    {"id": "normalize_columns", "title": "Normalize Columns", "category": "Data Structuring"},
    {"id": "detect_outliers", "title": "Detect Outliers", "category": "Validation & QA"},
    {"id": "merge_datasets", "title": "Merge Datasets", "category": "Data Structuring"},
    {"id": "export_to_api", "title": "Export to API", "category": "Export"},
]

def style_node(node):
    cat = node.get("category", "Uncategorized")
    style = CATEGORY_STYLES.get(cat, CATEGORY_STYLES["Uncategorized"])
    return Task(
        id=node["id"],
        label=f"{style['icon']} {node['title']}",
        style={"backgroundColor": style["color"], "borderRadius": "10px", "boxShadow": "2px 2px 5px rgba(0,0,0,0.2)"}
    )

nodes = [style_node(a) for a in assistants]
edges = [("clean_nulls", "normalize_columns"), ("normalize_columns", "detect_outliers")]

# --- MAIN DAG DISPLAY ---
st.subheader("🎨 Styled DAG with GPT Support")
with Dag(nodes, edges, direction="LR", node_spacing=60, layer_spacing=80) as result:
    st.write("📦 Current flow:", result)

# --- GPT Assistant Suggestion (per node) ---
st.markdown("### 🔮 Suggest Next Assistant")
selected_node = st.selectbox("Select current node", [a['title'] for a in assistants])
if st.button("💡 GPT: What comes next?"):
    try:
        prompt = f"I'm building a data pipeline. After the step '{selected_node}', what assistant should come next?"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )
        st.success(response.choices[0].message.content.strip())
    except Exception as e:
        st.error(f"GPT error: {e}")

# --- PIPELINE SUMMARY ---
if st.button("🧠 Summarize Pipeline"):
    try:
        steps = ", then ".join([a["title"] for a in assistants])
        prompt = f"Summarize the purpose of this pipeline: {steps}."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        st.info(response.choices[0].message.content.strip())
    except Exception as e:
        st.error(f"GPT error: {e}")
