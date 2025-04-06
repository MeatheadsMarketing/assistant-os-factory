# 🧱 Assistant OS Factory – Project Folder Structure

This is a complete map of all project folders and files used across versions `v1.0 → v1.9`.

---

## 📁 Folder Tree

```
assistant_markdown/
├── raw/                            # Raw assistant .md drafts (from GPT or Sheets)
├── processed/                      # GPT-enhanced markdowns
├── streamlit_ready/               # Launchable assistants + UI tabs
│   ├── multi_tab_launcher.py      # Streamlit launcher (v1.0+)
│   ├── manifest_dashboard.py      # Streamlit tab: assistant score table (v1.2)
│   ├── pipeline_designer_phaseX.py# DAG builder UIs (v1.4–v1.5)
│   ├── zip_manifest.json          # Assistant metadata (v1.1+)
├── dag_flows/                     # Saved DAG configurations (v1.4+)
├── tools/                         # Reusable utility modules
│   ├── visual_validator.py        # Validation + scoring (v1.1, v1.2)
│   ├── push_to_github.py          # GitHub deploy (Step 11)
│   ├── langchain_export.py        # LangChain converter (v1.3)
│   ├── __init__.py                # Package marker
├── releases/                      # Versioned .zip exports (v1.8+)
├── v1.1_manifest_builder.py       # Script to generate zip_manifest.json (v1.1)
├── assistant_bundle.zip           # Packaged bundle (from v1.0)
```

---

## 🧠 How It All Fits Together

| File/Folder                        | Purpose                                | Versions |
|-----------------------------------|----------------------------------------|----------|
| `raw/`                            | Markdown inputs from GPT or Sheets     | v1.0+    |
| `processed/`                      | Enhanced markdowns                     | v1.0     |
| `streamlit_ready/`                | Assistant folders + launcher UI        | v1.0+    |
| `zip_manifest.json`               | Assistant metadata summary             | v1.1+    |
| `manifest_dashboard.py`           | Score/validate dashboard tab           | v1.2     |
| `tools/visual_validator.py`       | Audit + rebuild incomplete assistants  | v1.1+    |
| `tools/langchain_export.py`       | Create LangChain tool JSONs            | v1.3     |
| `dag_flows/`                      | Store assistant chain JSON configs     | v1.4+    |
| `pipeline_designer_phaseX.py`     | Visual DAG building UIs                | v1.4–v1.5|
| `releases/`                       | Archived versioned bundles             | v1.8+    |
```

Place this in your `/assistant_markdown/` folder for reference.
