from config.llm import llm


def summarize_financials(financials):
    if not financials:
        return "No financials available."
    
    compact_text = []
    for statement_name, statement_dict in financials.items():
        compact_text.append(f"--- {statement_name.upper()} ---")
        if not isinstance(statement_dict, dict):
            compact_text.append(str(statement_dict))
            continue
        
        # statement_dict has dates as keys and row-value dicts as values
        # Take only the first 2 dates to limit token usage
        dates = list(statement_dict.keys())[:2]
        for date in dates:
            row_data = statement_dict[date]
            date_str = str(date).split()[0]
            compact_text.append(f"Date: {date_str}")
            
            # Key rows filter to reduce size drastically
            for row, val in row_data.items():
                if val == "":
                    continue
                row_lower = row.lower()
                is_key = any(k in row_lower for k in [
                    "revenue", "gross profit", "operating income", "net income", 
                    "total assets", "total liabilities", "equity", "total debt",
                    "operating activities", "capital expenditure", "free cash flow"
                ])
                if is_key:
                    compact_text.append(f"  {row}: {val}")
    return "\n".join(compact_text)


def financial(state):
    summarized = summarize_financials(state.get("financials"))

    prompt = f"""
You are a CFA Level III Financial Analyst.

Analyze these financial statements.

{summarized}

Provide

- Revenue Trend

- Profit Trend

- Margin Analysis

- Debt Analysis

- Cashflow Analysis

- Growth Analysis

- Overall Financial Health
"""

    response = llm.invoke(prompt)

    state["financial_analysis"] = response.content

    return state
