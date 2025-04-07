"""Let agents message each other with state updates."""

def broadcast_message(agents, message):
    for agent in agents:
        agent["inbox"].append(message)
    return agents

def retrieve_inbox(agent):
    return agent.get("inbox", [])
