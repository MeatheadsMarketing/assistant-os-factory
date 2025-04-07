"""Score agents in a run based on output quality."""

def score_agent(output: str, expected_keywords=None):
    expected_keywords = expected_keywords or []
    score = sum(1 for kw in expected_keywords if kw.lower() in output.lower())
    return round(score / len(expected_keywords) * 100, 2) if expected_keywords else 0
