from config.llm import llm


def risk(state):

    prompt = f"""
You are an Investment Risk Expert.

Company

{state["company"]}

Financial Analysis

{state["financial_analysis"]}

News

{state["news"]}

NSE Filings

{state["filings"]}

Identify

Business Risks

Financial Risks

Sector Risks

Regulatory Risks

Promoter Risks

Overall Investment Risk
"""

    response = llm.invoke(prompt)

    state["risks"] = {

        "analysis": response.content

    }

    return state
