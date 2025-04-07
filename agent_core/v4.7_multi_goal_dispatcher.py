"""Assign different agents to solve sub-goals in parallel."""

from concurrent.futures import ThreadPoolExecutor

def dispatch_subgoals(agent_fn_map, goals):
    results = {}
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(agent_fn_map[g["agent"]], g["goal"]): g["agent"] for g in goals}
        for future in futures:
            agent = futures[future]
            try:
                results[agent] = future.result()
            except Exception as e:
                results[agent] = f"❌ Error: {e}"
    return results
