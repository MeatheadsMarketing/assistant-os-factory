import json
import os

def run_dag_from_file(dag_path: str, inputs: dict = None):
    if not os.path.exists(dag_path):
        raise FileNotFoundError(f"DAG not found: {dag_path}")

    with open(dag_path) as f:
        flow = json.load(f)

    memory = ""
    log = []

    for step in flow:
        title = step["title"]
        step_input = inputs.get(title, "[default input]") if inputs else "[default input]"
        output = f"Output from {title} with input: {step_input}"
        memory += f"\n[{title}]: {output}"
        log.append({
            "step": step["step"],
            "title": title,
            "input": step_input,
            "output": output
        })

    return log, memory
