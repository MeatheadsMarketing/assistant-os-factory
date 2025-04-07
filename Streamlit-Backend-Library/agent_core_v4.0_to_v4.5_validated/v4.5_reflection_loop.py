"""Run agent → reflect → retry loop (like ReAct)."""

def reflection_loop(agent_fn, input_data, max_attempts=3):
    for attempt in range(max_attempts):
        output = agent_fn(input_data)
        if "error" not in output.lower():
            return output
        input_data += " [reflected]"
    return "[Failed after retries]"
