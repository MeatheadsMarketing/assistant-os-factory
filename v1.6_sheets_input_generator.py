import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="📥 Sheet → Assistant Generator", layout="wide")
st.title("📥 Google Sheets Batch to Assistant Markdown")

st.markdown("Upload a CSV exported from Google Sheets. Each row will be converted into a `.md` assistant draft.")

csv_file = st.file_uploader("Upload Assistant Sheet (.csv)", type="csv")

if csv_file:
    df = pd.read_csv(csv_file)
    st.success(f"Loaded {len(df)} rows from file")

    required_cols = ["title", "description", "category", "inputs", "outputs"]
    if not all(col in df.columns for col in required_cols):
        st.error("Missing one or more required columns: title, description, category, inputs, outputs")
        st.stop()

    output_dir = "/content/drive/MyDrive/assistant_markdown/raw/"
    os.makedirs(output_dir, exist_ok=True)

    for _, row in df.iterrows():
        slug = row["title"].lower().replace(" ", "_")
        md_path = os.path.join(output_dir, f"{slug}.md")
        with open(md_path, "w") as f:
            f.write(f"# {row['title']}

")
            f.write("## Description
")
            f.write(f"{row['description']}

")
            f.write(f"Category: {row['category']}

")
            f.write("### Inputs
")
            for item in str(row["inputs"]).split(";"):
                f.write(f"- Input: {item.strip()}
")
            f.write("### Outputs
")
            for item in str(row["outputs"]).split(";"):
                f.write(f"- Output: {item.strip()}
")

    st.success(f"✅ {len(df)} assistants saved to `/raw/`")
