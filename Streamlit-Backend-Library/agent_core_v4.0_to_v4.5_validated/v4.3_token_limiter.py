"""Enforce token budgets across chained agents."""

def enforce_token_limit(text: str, max_tokens: int = 1000):
    tokens = text.split()
    if len(tokens) > max_tokens:
        return " ".join(tokens[:max_tokens])
    return text
