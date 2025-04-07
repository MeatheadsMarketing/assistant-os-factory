import streamlit as st
import os
import json
import pandas as pd

st.set_page_config(page_title="📊 Assistant Manifest Dashboard", layout="wide")
st.title("📊 Assistant Validation Dashboard")

MANIFEST_PATH = os.path.join(os.path.dirname(__file__), "zip_manifest.json")

if not os.path.exists(MANIFEST_PATH):
    st.warning("No manifest file found. Please run validation first.")
else:
    with open(MANIFEST_PATH) as f:
        manifest = json.load(f)

    df = pd.DataFrame(manifest)

    # Filters
    st.sidebar.header("🔍 Filters")
    score_filter = st.sidebar.slider("Score Range", 0, 5, (3, 5))
    category_filter = st.sidebar.multiselect("Categories", options=df["category"].unique(), default=list(df["category"].unique()))
    status_filter = st.sidebar.multiselect("Status", options=df["status"].unique(), default=list(df["status"].unique()))

    filtered_df = df[
        (df["score"] >= score_filter[0]) &
        (df["score"] <= score_filter[1]) &
        (df["category"].isin(category_filter)) &
        (df["status"].isin(status_filter))
    ]

    st.success(f"Showing {len(filtered_df)} of {len(df)} assistants")

    st.dataframe(filtered_df)

    # Download options
    st.markdown("### 📥 Download Filtered Manifest")
    st.download_button("Download JSON", data=json.dumps(filtered_df.to_dict(orient="records"), indent=2), file_name="filtered_manifest.json")
    st.download_button("Download CSV", data=filtered_df.to_csv(index=False), file_name="filtered_manifest.csv")
