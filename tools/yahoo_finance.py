import yfinance as yf
from tools.company_resolver import resolve_company


def _get_ticker(company: str):
    """
    Resolve company name and return yfinance Ticker object.
    """

    company_info = resolve_company(company)

    if company_info is None:
        raise ValueError(f"Company '{company}' not found.")

    ticker = company_info["ticker"]

    return yf.Ticker(ticker)


# -------------------------------------------------------
# Company Profile
# -------------------------------------------------------

def get_company_info(company: str):

    stock = _get_ticker(company)

    info = stock.info

    return {
        "Company": info.get("longName"),
        "Sector": info.get("sector"),
        "Industry": info.get("industry"),
        "CEO": info.get("companyOfficers"),
        "Website": info.get("website"),
        "Summary": info.get("longBusinessSummary"),
        "Employees": info.get("fullTimeEmployees"),
        "Country": info.get("country"),
    }


# -------------------------------------------------------
# Current Stock Price
# -------------------------------------------------------

def get_stock_price(company: str):

    stock = _get_ticker(company)

    info = stock.info

    return {
        "Company": info.get("longName"),
        "Symbol": info.get("symbol"),
        "Current Price": info.get("currentPrice"),
        "Previous Close": info.get("previousClose"),
        "Open": info.get("open"),
        "Day High": info.get("dayHigh"),
        "Day Low": info.get("dayLow"),
        "Currency": info.get("currency"),
    }


# -------------------------------------------------------
# Historical Data
# -------------------------------------------------------

def get_history(company: str, period="1y"):

    stock = _get_ticker(company)

    history = stock.history(period=period)

    return history.reset_index().to_dict(orient="records")


# -------------------------------------------------------
# Financial Statements
# -------------------------------------------------------

def _stringify_keys(d):
    if not isinstance(d, dict):
        return d
    return {str(k): _stringify_keys(v) if isinstance(v, dict) else v for k, v in d.items()}


def get_balance_sheet(company: str):

    stock = _get_ticker(company)

    return _stringify_keys(stock.balance_sheet.fillna("").to_dict())


def get_income_statement(company: str):

    stock = _get_ticker(company)

    return _stringify_keys(stock.financials.fillna("").to_dict())


def get_cashflow(company: str):

    stock = _get_ticker(company)

    return _stringify_keys(stock.cashflow.fillna("").to_dict())


# -------------------------------------------------------
# Earnings
# -------------------------------------------------------

def get_earnings(company: str):

    stock = _get_ticker(company)

    try:
        return stock.earnings.to_dict()
    except Exception:
        return {}


# -------------------------------------------------------
# Dividends
# -------------------------------------------------------

def get_dividends(company: str):

    stock = _get_ticker(company)

    return stock.dividends.to_dict()


# -------------------------------------------------------
# Analyst Recommendations
# -------------------------------------------------------

def get_recommendations(company: str):

    stock = _get_ticker(company)

    recommendations = stock.recommendations

    if recommendations is None:
        return []

    return recommendations.tail(20).fillna("").to_dict(
        orient="records"
    )


# -------------------------------------------------------
# Major Holders
# -------------------------------------------------------

def get_major_holders(company: str):

    stock = _get_ticker(company)

    holders = stock.major_holders

    if holders is None:
        return []

    return holders.fillna("").to_dict(orient="records")


# -------------------------------------------------------
# Institutional Holders
# -------------------------------------------------------

def get_institutional_holders(company: str):

    stock = _get_ticker(company)

    holders = stock.institutional_holders

    if holders is None:
        return []

    return holders.fillna("").to_dict(orient="records")


from langchain_core.tools import tool


@tool
def stock_price(company: str):

    """
    Return latest stock price.
    """

    return get_stock_price(company)


@tool
def company_profile(company: str):

    """
    Company information.
    """

    return get_company_info(company)