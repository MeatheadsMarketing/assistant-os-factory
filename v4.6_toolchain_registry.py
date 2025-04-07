"""Register agents + toolchains from YAML or LangChain specs."""

import yaml
import os

def load_toolchain_config(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Toolchain file not found: {path}")
    with open(path, "r") as f:
        return yaml.safe_load(f)

def list_available_agents(config):
    return list(config.get("agents", {}).keys())
