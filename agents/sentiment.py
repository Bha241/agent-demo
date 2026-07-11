from config.llm import llm


def sentiment(state):

    prompt = f"""
Analyze sentiment from these news articles.

{state["news"]}

Return

Overall Sentiment

Positive %

Negative %

Neutral %

Top Reasons
"""

    response = llm.invoke(prompt)

    state["sentiment"] = {

        "analysis": response.content

    }

    return state
