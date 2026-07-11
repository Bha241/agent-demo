from tools.yahoo_finance import (
    get_company_info,
    get_stock_price,
    get_income_statement,
    get_balance_sheet,
    get_cashflow
)

from tools.market_news import latest_news
from tools.indian_filings import get_nse_announcements


def researcher(state):

    company = state["query"]

    state["company"] = get_company_info(company)

    state["stock_price"] = get_stock_price(company)

    state["news"] = latest_news(company)

    state["filings"] = get_nse_announcements(company)

    state["financials"] = {

        "income_statement": get_income_statement(company),

        "balance_sheet": get_balance_sheet(company),

        "cashflow": get_cashflow(company)
    }

    return state
