import streamlit as st
import os
import zipfile

st.set_page_config(page_title="☁️ Cloud Bundle Exporter", layout="wide")
st.title("☁️ Replit + Streamlit Cloud Bundle Generator")

src_dir = "/content/drive/MyDrive/assistant_markdown/streamlit_ready/"
bundle_name = "assistant_factory_cloud_bundle.zip"
output_path = f"/content/drive/MyDrive/assistant_markdown/{bundle_name}"

if st.button("📦 Build Cloud Export ZIP"):
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(src_dir):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, src_dir)
                zipf.write(full_path, arcname)
    st.success(f"✅ Cloud bundle created at: {output_path}")
    st.download_button("Download ZIP", open(output_path, "rb"), file_name=bundle_name)

st.markdown("This ZIP can be uploaded directly to Replit or linked to Streamlit Cloud.")
st.markdown("It includes `.py`, `.md`, `manifest.json`, and launcher files.")
