from config.llm import llm


SYSTEM_PROMPT = """
You are the Planner Agent.

Your job is NOT to answer.

Your job is to determine what information
is needed before making an investment decision.

Always require:

- Company Information
- Stock Price
- Latest News
- NSE/BSE Filings
- Financial Analysis

Return only:

PLAN READY
"""


def planner(state):

    history = state.get("messages", []) or []

    history_items = []
    for msg in history:
        if isinstance(msg, dict):
            role = msg.get("role", "user")
            content = msg.get("content", "")
        else:
            role = getattr(msg, "type", "user")
            content = getattr(msg, "content", "")
        history_items.append(f"{role.capitalize()}: {content}")
    history_text = "\n".join(history_items)

    prompt = f"""
Conversation History

{history_text}

Current Question

{state['query']}

{SYSTEM_PROMPT}
"""

    response = llm.invoke(prompt)

    if "messages" not in state or state["messages"] is None:
        state["messages"] = []

    state["messages"].append(
        {
            "role": "user",
            "content": state["query"]
        }
    )

    state["messages"].append(
        {
            "role": "assistant",
            "content": response.content
        }
    )

    return state
