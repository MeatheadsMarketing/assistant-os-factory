"""Replay past agent chains for debugging or training."""

def replay_log(file_path):
    if not file_path.endswith(".md"):
        raise ValueError("Log must be a markdown file.")
    with open(file_path) as f:
        return f.read().split("\n\n")
