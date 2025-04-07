# 🔁 Assistant OS Factory – CHANGELOG v2.x

## v2.0 – Run DAGs from JSON
- Load saved DAG files
- Simulate assistant execution order
- Foundation for runtime orchestration

## v2.1 – Assistant → Tool schema wrapper
- Exports assistant manifest as OpenAI-style tool schema
- Used for LangChain, function-calling, and GPT agents

## v2.2 – Chain memory trace logger
- Logs each assistant step’s input/output
- Simulates memory chaining across the flow

## v2.3 – CLI + API DAG runner
- Enables `python run_from_dag.py --dag xyz.json`
- Supports batch running of DAGs outside Streamlit

## v2.4 – Flow integration staging (optional if skipped)
- Reserved version slot for future integrations

## v2.5 – GPT-powered DAG optimizer
- Ask GPT to analyze and revise a DAG flow
- Suggests reordering or assistant replacement

## v2.6 – Agent-style chain simulator
- Simulates assistants acting like connected agents
- Mock interface with user input + output generation

## v2.7 – Webhook on DAG completion
- Triggers external webhook after flow finishes
- Sends success payload with flow metadata

## v2.8 – DAG scheduler / job queuer
- Save a DAG run to a scheduled timestamp
- Queue up future auto-runs (future cron-ready)

## v2.9 – Drive snapshot / zip exporter
- Exports full `/assistant_markdown/` as versioned ZIP
- Useful for backup, handoff, or Replit packaging
