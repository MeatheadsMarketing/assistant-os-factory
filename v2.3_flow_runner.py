import argparse
import json
import os
from datetime import datetime

def run_dag_from_file(dag_path: str, inputs: dict = None):
    if not os.path.exists(dag_path):
        raise FileNotFoundError(f"DAG not found at: {dag_path}")

    with open(dag_path) as f:
        flow = json.load(f)

    print(f"📋 Running DAG: {os.path.basename(dag_path)}")
    log = []
    memory = ""

    for step in flow:
        title = step["title"]
        print(f"🔁 Step {step['step']}: {title}")
        step_input = inputs.get(title, "[default input]") if inputs else "[default input]"
        step_output = f"Output from {title} with input: {step_input}"
        memory += f"
[{title}]: {step_output}"
        print(f"✅ Output: {step_output}")
        log.append({
            "step": step["step"],
            "title": title,
            "input": step_input,
            "output": step_output
        })

    return log

def save_trace(log, output_path="trace_log.md"):
    with open(output_path, "w") as f:
        f.write(f"# 🔗 DAG Execution Log\n📅 {datetime.now()}\n\n")
        for entry in log:
            f.write(f"## Step {entry['step']}: {entry['title']}\n")
            f.write(f"- Input: `{entry['input']}`\n")
            f.write(f"- Output: `{entry['output']}`\n\n")
    print(f"🧾 Log saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dag", type=str, required=True, help="Path to DAG .json file")
    parser.add_argument("--log", type=str, default="trace_log.md", help="Path to save output log")
    args = parser.parse_args()

    result = run_dag_from_file(args.dag)
    save_trace(result, args.log)
