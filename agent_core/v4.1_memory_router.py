"""Route memory/output selectively to future agents."""

def route_memory(memory: dict, route_table: dict):
    routed = {}
    for agent, targets in route_table.items():
        if agent in memory:
            for t in targets:
                routed[t] = memory[agent]
    return routed
