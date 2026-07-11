from config.llm import llm


def reviewer(state):

    prompt = f"""
Review this investment report.

{state["report"]}

Check

- Accuracy

- Missing Sections

- Hallucinations

- Grammar

- Investment Logic

If acceptable return APPROVED.

Otherwise provide corrections.
"""

    response = llm.invoke(prompt)

    state["review"] = response.content

    return state
