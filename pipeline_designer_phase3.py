import streamlit as st
from streamlit_dag import Dag, Task
import os
import json
from datetime import datetime

st.set_page_config(page_title="💾 DAG Builder – Phase 3", layout="wide")
st.title("💾 DAG Builder – Phase 3: Save, Load, Export")

# --- Path setup ---
FLOW_DIR = "/content/drive/MyDrive/assistant_markdown/dag_flows/"
os.makedirs(FLOW_DIR, exist_ok=True)

# --- Assistant templates ---
CATEGORY_STYLES = {
    "Data Cleaning": {"color": "#4BA3C7", "icon": "🧹"},
    "Data Structuring": {"color": "#FFD166", "icon": "🧱"},
    "Data Enrichment": {"color": "#EF476F", "icon": "✨"},
    "Validation & QA": {"color": "#06D6A0", "icon": "✅"},
    "Export": {"color": "#118AB2", "icon": "📤"},
    "Uncategorized": {"color": "#CCCCCC", "icon": "❓"},
}

# Default mock flow
default_assistants = [
    {"id": "clean_nulls", "title": "Clean Nulls", "category": "Data Cleaning"},
    {"id": "normalize_columns", "title": "Normalize Columns", "category": "Data Structuring"},
    {"id": "detect_outliers", "title": "Detect Outliers", "category": "Validation & QA"},
    {"id": "merge_datasets", "title": "Merge Datasets", "category": "Data Structuring"},
    {"id": "export_to_api", "title": "Export to API", "category": "Export"},
]
default_edges = [("clean_nulls", "normalize_columns"), ("normalize_columns", "detect_outliers")]

# Session state
if "nodes" not in st.session_state:
    st.session_state.nodes = default_assistants
if "edges" not in st.session_state:
    st.session_state.edges = default_edges

# Build styled DAG nodes
def style_node(node):
    cat = node.get("category", "Uncategorized")
    style = CATEGORY_STYLES.get(cat, CATEGORY_STYLES["Uncategorized"])
    return Task(
        id=node["id"],
        label=f"{style['icon']} {node['title']}",
        style={"backgroundColor": style["color"], "borderRadius": "10px", "boxShadow": "2px 2px 5px rgba(0,0,0,0.2)"}
    )

styled_nodes = [style_node(n) for n in st.session_state.nodes]

# UI: DAG Display
st.subheader("🧱 DAG Canvas")
with Dag(styled_nodes, st.session_state.edges, direction="LR", node_spacing=60, layer_spacing=80) as result:
    st.write("🔗 Flow result:", result)

# 💾 SAVE FLOW
if st.button("💾 Save Flow as JSON"):
    flow_data = {
        "nodes": st.session_state.nodes,
        "edges": st.session_state.edges
    }
    filename = f"dag_flow_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(os.path.join(FLOW_DIR, filename), "w") as f:
        json.dump(flow_data, f, indent=2)
    st.success(f"Saved to {filename}")

# 📂 LOAD FLOW
flow_files = [f for f in os.listdir(FLOW_DIR) if f.endswith(".json")]
selected_flow = st.selectbox("📂 Load existing flow", ["-- Select --"] + flow_files)

if selected_flow != "-- Select --":
    with open(os.path.join(FLOW_DIR, selected_flow)) as f:
        loaded = json.load(f)
        st.session_state.nodes = loaded["nodes"]
        st.session_state.edges = loaded["edges"]
    st.success(f"Loaded flow: {selected_flow}")

# 📝 EXPORT AS MARKDOWN
if st.button("📄 Export Flow as Markdown"):
    lines = ["# DAG Flow Summary
"]
    for n in st.session_state.nodes:
        lines.append(f"## {n['title']}")
        lines.append(f"- ID: `{n['id']}`")
        lines.append(f"- Category: `{n.get('category', 'N/A')}`
")
    st.download_button("📥 Download Markdown", data="
".join(lines), file_name="dag_flow_summary.md")
