def validation(state):

    errors = []

    if not state.get("company"):
        errors.append("Company information missing")

    if not state.get("stock_price"):
        errors.append("Stock price missing")

    if not state.get("financials"):
        errors.append("Financial statements missing")

    if not state.get("news"):
        state["news"] = [
            {
                "title": "Recent news unavailable",
                "body": "No recent news articles were found or retrieved for the company at this time."
            }
        ]

    if not state.get("filings"):
        state["filings"] = [
            {
                "title": "Corporate filings unavailable",
                "body": "No recent NSE/BSE corporate announcements or filings were found for the company at this time."
            }
        ]

    state["validation"] = {

        "passed": len(errors) == 0,

        "errors": errors

    }

    return state
