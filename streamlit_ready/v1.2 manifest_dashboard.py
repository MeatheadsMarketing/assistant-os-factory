import streamlit as st
import json
import os
import pandas as pd

st.set_page_config(page_title="📊 Assistant Dashboard", layout="wide")
st.title("📊 Assistant Validation Dashboard")

manifest_path = os.path.join(os.path.dirname(__file__), "zip_manifest.json")

if not os.path.exists(manifest_path):
    st.warning("⚠️ zip_manifest.json not found.")
else:
    with open(manifest_path, "r") as f:
        manifest = json.load(f)

    df = pd.DataFrame(manifest)

    # Sidebar filters
    st.sidebar.header("🔍 Filters")
    score_range = st.sidebar.slider("Score Range", 0, 5, (3, 5))
    status_filter = st.sidebar.multiselect("Status", options=df["status"].unique(), default=list(df["status"].unique()))
    category_filter = st.sidebar.multiselect("Category", options=df["category"].unique(), default=list(df["category"].unique()))
    gpt_filter = st.sidebar.selectbox("Uses GPT?", options=["All", True, False])

    # Apply filters
    filtered_df = df[
        (df["score"] >= score_range[0]) &
        (df["score"] <= score_range[1]) &
        (df["status"].isin(status_filter)) &
        (df["category"].isin(category_filter))
    ]
    if gpt_filter != "All":
        filtered_df = filtered_df[filtered_df["uses_gpt"] == gpt_filter]

    st.success(f"Showing {len(filtered_df)} of {len(df)} assistants")
    st.dataframe(filtered_df)

    # Export options
    st.markdown("### 📥 Export Filtered Data")
    st.download_button("Download CSV", filtered_df.to_csv(index=False), file_name="filtered_manifest.csv")
    st.download_button("Download JSON", data=filtered_df.to_json(orient="records", indent=2), file_name="filtered_manifest.json")
