from config.llm import llm


def report_writer(state):

    prompt = f"""
Prepare a professional investment report.

User Query

{state["query"]}

Company

{state["company"]}

Stock

{state["stock_price"]}

Financial Analysis

{state["financial_analysis"]}

Sentiment

{state["sentiment"]}

Risk Analysis

{state["risks"]}

Generate

1 Executive Summary

2 Company Overview

3 Financial Analysis

4 News Summary

5 Sentiment

6 Risks

7 Recommendation

8 BUY / HOLD / SELL

9 Confidence Score
"""

    response = llm.invoke(prompt)

    state["report"] = response.content

    return state
