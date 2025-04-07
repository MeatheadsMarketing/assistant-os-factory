# 🧠 Assistant OS Factory

A modular, versioned AI assistant framework built with GPT, Streamlit, Colab, and GitHub.

---

## 🔧 Architecture Overview

```
assistant_markdown/
├── agent_core/               # v4.x agent runtime system
├── flow_engine/              # v2.x–v3.x DAG and orchestration tools
├── tools/                    # v5.x backend + utility modules
├── streamlit_ready/          # UI-ready assistants and builder tabs
├── raw/                      # Unprocessed assistant markdowns
├── processed/                # GPT-enhanced .md files
├── dag_flows/                # JSON-based DAG execution chains
├── CHANGELOG.md              # Combined v1–v5 release history
```

---

## 📦 Versioned Milestones

| Version | Layer | Summary |
|---------|-------|---------|
| v1.x    | Assistant Factory | GPT-enhanced markdown → .py generation, validation, and launcher UI |
| v2.x    | DAG Runtime       | DAG execution, CLI runner, webhook, trace logger |
| v3.x    | Agent Runtime     | Modular agent flows, memory injection, orchestration, toolchain logic |
| v4.x    | `agent_core/`     | Core agent execution: scoring, retry, token limits, message passing |
| v5.x    | `tools/` backend  | Sheet ingestors, file scanners, launcher tools, UI components |

---

## 🚀 Deploy Options

- **Streamlit Cloud**: [streamlit.io/cloud](https://streamlit.io/cloud)
- **Replit Export**: Use `v1.9_cloud_bundle_exporter.py`
- **GitHub Sync**: via `push_to_github.py`
- **DAG Execution**: via `v2.0_run_from_dag.py` or `flow_engine.runner`

---

## 🧠 Agents and Execution

- 🧠 Each assistant folder has:
  - `run_ui()` Streamlit frontend
  - `manifest.json` metadata
  - `.md` + `README.md`
- 🔗 Agents can chain via DAG
- 🤖 All agents can export to `tool.json` (LangChain-style)

---

## 📈 Validation + Testing

Use:
- `zip_manifest.json` for tracking assistant health
- `manifest_dashboard.py` for visual filter/export
- `agent_evaluator.py` to score outputs

---

## 🌍 Connect

- GitHub: [MeatheadsMarketing/assistant-os-factory](https://github.com/MeatheadsMarketing/assistant-os-factory)
