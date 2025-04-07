# 📦 Assistant Factory – Full CHANGELOG

---

## v1.x: Foundation + Launch

### 🚀 v1.0 – Assistant Factory Core
- Generate `.md` → `.py` assistants
- GPT-enhancement + preview
- Streamlit-ready with `run_ui()`
- ZIP export to bundle assistants

### 🧾 v1.1 – Manifest Generator
- Validates all assistant folders
- Outputs `zip_manifest.json` with assistant health & metadata

### 📊 v1.2 – Streamlit Dashboard Tab
- View assistants with filters: score, category, GPT
- Export filtered view as CSV/JSON

### 🔌 v1.3 – LangChain Tool Export
- Export assistants to tool schema format
- Compatible with OpenAI Function Calling

### 🧱 v1.4 – Assistant DAG Builder
- Select assistants sequentially to build a flow
- Save chain into `dag_flows/`

### 🖱 v1.5 – Drag-and-Drop DAG UI
- Assistant nodes in Streamlit-DAG
- Export as JSON, CSV, Markdown

### 📥 v1.6 – Sheets Input Generator
- Upload Google Sheets CSV
- Generate `.md` drafts row-by-row

### 🤖 v1.7 – GPT Pipeline Generator
- Describe a goal → get assistant chain
- Export flow as Markdown

### 🏷 v1.8 – GitHub Tag + Changelog Tool
- Create GitHub tags from Streamlit
- Generate changelog from `zip_manifest.json`

### 📦 v1.9 – Cloud Bundle Exporter
- Create deployable `.zip` for Replit/Streamlit
- Includes launcher, assistants, and manifest
---

## v2.x: Agent Logic + DAG Execution

### v2.0 – Run DAGs from JSON
- Load saved DAG files
- Simulate assistant execution order
- Foundation for runtime orchestration

### v2.1 – Assistant → Tool schema wrapper
- Exports assistant manifest as OpenAI-style tool schema
- Used for LangChain, function-calling, and GPT agents

### v2.2 – Chain memory trace logger
- Logs each assistant step’s input/output
- Simulates memory chaining across the flow

### v2.3 – CLI + API DAG runner
- Enables `python run_from_dag.py --dag xyz.json`
- Supports batch running of DAGs outside Streamlit

### v2.4 – Flow integration staging (optional if skipped)
- Reserved version slot for future integrations

### v2.5 – GPT-powered DAG optimizer
- Ask GPT to analyze and revise a DAG flow
- Suggests reordering or assistant replacement

### v2.6 – Agent-style chain simulator
- Simulates assistants acting like connected agents
- Mock interface with user input + output generation

### v2.7 – Webhook on DAG completion
- Triggers external webhook after flow finishes
- Sends success payload with flow metadata

### v2.8 – DAG scheduler / job queuer
- Save a DAG run to a scheduled timestamp
- Queue up future auto-runs (future cron-ready)

### v2.9 – Drive snapshot / zip exporter
- Exports full `/assistant_markdown/` as versioned ZIP
- Useful for backup, handoff, or Replit packaging
