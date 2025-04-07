# 🔁 Flow Engine Module

This folder contains modular utilities to run assistant DAGs:

- `runner.py` – DAG runner that executes each node
- `logger.py` – Saves markdown trace of the run
- `wrapper.py` – Converts an assistant into a tool schema
- `__init__.py` – Makes it importable from Colab or CLI
