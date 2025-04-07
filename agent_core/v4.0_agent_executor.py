"""Execute assistant agents from a config file, DAG, or single call."""

def run_agent_from_config(config: dict):
    agent_name = config.get("name", "default_agent")
    input_data = config.get("input", "")
    print(f"Running agent {agent_name} with input: {input_data}")
    return f"[{agent_name} output]: processed '{input_data}'"
