from datetime import datetime

def save_trace_log(trace_log: list, output_path: str = "trace_log.md"):
    with open(output_path, "w") as f:
        f.write(f"# 🧠 Assistant DAG Execution Log\n📅 {datetime.now()}\n\n")
        for entry in trace_log:
            f.write(f"## Step {entry['step']}: {entry['title']}\n")
            f.write(f"- Input: `{entry['input']}`\n")
            f.write(f"- Output: `{entry['output']}`\n\n")
    return output_path
