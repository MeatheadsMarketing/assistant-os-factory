import streamlit as st
from streamlit_dag import streamlit_dag, DagNode
import json
import os
import uuid

st.set_page_config(page_title="🖱️ Drag-and-Drop DAG Builder", layout="wide")
st.title("🖱️ Drag-and-Drop Assistant Flow Builder")

manifest_path = os.path.join(os.path.dirname(__file__), "zip_manifest.json")
dag_flow_dir = os.path.join(os.path.dirname(__file__), "..", "dag_flows")
os.makedirs(dag_flow_dir, exist_ok=True)

# Load assistant manifest
if not os.path.exists(manifest_path):
    st.warning("zip_manifest.json not found.")
    st.stop()

with open(manifest_path, "r") as f:
    manifest = json.load(f)

# Build node list
nodes = []
for item in manifest:
    node = DagNode(
        id=str(uuid.uuid4()),
        label=item["title"],
        description=item.get("category", "Uncategorized"),
        inputs=[],
        outputs=[]
    )
    nodes.append(node)

# Drag-and-drop UI
result = streamlit_dag(nodes)

# Preview and export
if result["nodes"]:
    st.success(f"{len(result['nodes'])} nodes used in this DAG.")

    if st.button("💾 Save DAG Flow"):
        flow_name = st.text_input("Flow Name", "dag_flow_v1", key="save_input")
        dag_json = json.dumps(result, indent=2)
        json_path = os.path.join(dag_flow_dir, f"{flow_name}.json")
        with open(json_path, "w") as f:
            f.write(dag_json)
        st.success(f"✅ Flow saved to `{json_path}`")

    # Export formats
    st.markdown("### 📤 Export Flow")
    dag_data = json.dumps(result, indent=2)
    st.download_button("📥 Download JSON", data=dag_data, file_name="dag_flow.json")

    import pandas as pd
    flat_rows = [{"id": n["id"], "title": n["label"], "category": n.get("description", "")} for n in result["nodes"]]
    df = pd.DataFrame(flat_rows)

    st.download_button("📥 Download CSV", data=df.to_csv(index=False), file_name="dag_flow.csv")
    st.download_button("📥 Download Markdown", data=df.to_markdown(index=False), file_name="dag_flow.md")
else:
    st.info("👆 Drag assistants into a DAG to start.")
