import streamlit as st
from streamlit_dag import Dag, Task
import json
import os

st.set_page_config(page_title="🧱 DAG Flow Builder", layout="wide")
st.title("🧱 DAG Flow Builder – Phase 1: Visual Enhancements")

# === CONFIGURATION ===
CATEGORY_STYLES = {
    "Data Cleaning": {"color": "#4BA3C7", "icon": "🧹"},
    "Data Structuring": {"color": "#FFD166", "icon": "🧱"},
    "Data Enrichment": {"color": "#EF476F", "icon": "✨"},
    "Validation & QA": {"color": "#06D6A0", "icon": "✅"},
    "Export": {"color": "#118AB2", "icon": "📤"},
    "Uncategorized": {"color": "#CCCCCC", "icon": "❓"},
}

# === MOCKED ASSISTANTS (can be loaded dynamically later) ===
assistants = [
    {"id": "clean_nulls", "title": "Clean Nulls", "category": "Data Cleaning"},
    {"id": "normalize_columns", "title": "Normalize Columns", "category": "Data Structuring"},
    {"id": "detect_outliers", "title": "Detect Outliers", "category": "Validation & QA"},
    {"id": "merge_datasets", "title": "Merge Datasets", "category": "Data Structuring"},
    {"id": "export_to_api", "title": "Export to API", "category": "Export"},
]

# === BUILD TASKS WITH STYLES ===
def style_node(node):
    cat = node.get("category", "Uncategorized")
    style = CATEGORY_STYLES.get(cat, CATEGORY_STYLES["Uncategorized"])
    return Task(
        id=node["id"],
        label=f"{style['icon']} {node['title']}",
        style={"backgroundColor": style["color"], "borderRadius": "10px", "boxShadow": "2px 2px 5px rgba(0,0,0,0.2)"},
    )

nodes = [style_node(a) for a in assistants]
edges = [("clean_nulls", "normalize_columns"), ("normalize_columns", "detect_outliers")]

# === LAYOUT ===
st.subheader("🎨 Styled Assistant Graph")
with Dag(nodes, edges, direction="LR", node_spacing=60, layer_spacing=80) as result:
    st.write("📦 Current flow:", result)

# === HOVER TOOLTIP MOCKUP ===
st.markdown("ℹ️ Hover over each node to view assistant category and color.")
