import streamlit as st
from streamlit_dag import Dag, Task
import openai
import json
import os
from copy import deepcopy

st.set_page_config(page_title="🛠️ DAG Builder – Phase 4", layout="wide")
st.title("🛠️ DAG Builder – Phase 4: Full UX + GPT Simulation")

# GPT Setup
openai.api_key = os.getenv("OPENAI_API_KEY", "sk-REPLACE_ME")

# State
if "nodes" not in st.session_state:
    st.session_state.nodes = []
if "edges" not in st.session_state:
    st.session_state.edges = []
if "history" not in st.session_state:
    st.session_state.history = []

CATEGORY_STYLES = {
    "Data Cleaning": {"color": "#4BA3C7", "icon": "🧹"},
    "Data Structuring": {"color": "#FFD166", "icon": "🧱"},
    "Data Enrichment": {"color": "#EF476F", "icon": "✨"},
    "Validation & QA": {"color": "#06D6A0", "icon": "✅"},
    "Export": {"color": "#118AB2", "icon": "📤"},
    "Uncategorized": {"color": "#CCCCCC", "icon": "❓"},
}

# Node Library (static for now)
node_library = [
    {"title": "Clean Nulls", "category": "Data Cleaning"},
    {"title": "Normalize Columns", "category": "Data Structuring"},
    {"title": "Detect Outliers", "category": "Validation & QA"},
    {"title": "Merge Datasets", "category": "Data Structuring"},
    {"title": "Export to API", "category": "Export"},
]

def generate_node_id(title):
    return title.lower().replace(" ", "_") + "_" + str(len(st.session_state.nodes))

# Sidebar: Node Library
st.sidebar.title("📚 Node Library")
search = st.sidebar.text_input("Search Assistants")
filtered = [n for n in node_library if search.lower() in n["title"].lower()]

for item in filtered:
    if st.sidebar.button(f"➕ Add: {item['title']}"):
        new_id = generate_node_id(item["title"])
        st.session_state.history.append((deepcopy(st.session_state.nodes), deepcopy(st.session_state.edges)))
        st.session_state.nodes.append({
            "id": new_id,
            "title": item["title"],
            "category": item["category"]
        })

# Sidebar: Undo/Redo
st.sidebar.markdown("---")
if st.sidebar.button("↩️ Undo"):
    if st.session_state.history:
        last_nodes, last_edges = st.session_state.history.pop()
        st.session_state.nodes = last_nodes
        st.session_state.edges = last_edges

# Build Task objects
def style_node(node):
    cat = node.get("category", "Uncategorized")
    style = CATEGORY_STYLES.get(cat, CATEGORY_STYLES["Uncategorized"])
    return Task(
        id=node["id"],
        label=f"{style['icon']} {node['title']}",
        style={"backgroundColor": style["color"], "borderRadius": "10px", "boxShadow": "2px 2px 5px rgba(0,0,0,0.2)"}
    )

tasks = [style_node(n) for n in st.session_state.nodes]

st.subheader("🎯 DAG Canvas")
with Dag(tasks, st.session_state.edges, direction="LR", node_spacing=60, layer_spacing=80) as result:
    st.write("🧩 Flow result:", result)
    # Allow edge creation through canvas
    if result["added_edges"]:
        st.session_state.edges += result["added_edges"]

# GPT Simulation
if st.button("🧪 Run Simulation"):
    if not st.session_state.nodes:
        st.warning("No nodes to simulate.")
    else:
        try:
            steps = ", then ".join([n["title"] for n in st.session_state.nodes])
            prompt = f"Simulate what this assistant pipeline will do: {steps}."
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4
            )
            st.info(response.choices[0].message.content.strip())
        except Exception as e:
            st.error(f"GPT error: {e}")
