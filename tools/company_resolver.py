import yfinance as yf


def resolve_company(query: str):
    """
    Resolve an Indian company name into its
    NSE symbol and Yahoo Finance ticker.
    """

    company_map = {
        "reliance": {
            "name": "Reliance Industries Ltd",
            "symbol": "RELIANCE",
            "ticker": "RELIANCE.NS",
            "bse": "500325"
        },

        "tcs": {
            "name": "Tata Consultancy Services Ltd",
            "symbol": "TCS",
            "ticker": "TCS.NS",
            "bse": "532540"
        },

        "infosys": {
            "name": "Infosys Ltd",
            "symbol": "INFY",
            "ticker": "INFY.NS",
            "bse": "500209"
        },

        "hdfc bank": {
            "name": "HDFC Bank Ltd",
            "symbol": "HDFCBANK",
            "ticker": "HDFCBANK.NS",
            "bse": "500180"
        },

        "icici bank": {
            "name": "ICICI Bank Ltd",
            "symbol": "ICICIBANK",
            "ticker": "ICICIBANK.NS",
            "bse": "532174"
        },

        "wipro": {
            "name": "Wipro Ltd",
            "symbol": "WIPRO",
            "ticker": "WIPRO.NS",
            "bse": "507685"
        },

        "sbi": {
            "name": "State Bank of India",
            "symbol": "SBIN",
            "ticker": "SBIN.NS",
            "bse": "500112"
        }
    }

    query = query.lower().strip()

    for key, value in company_map.items():

        if key in query:

            return value

    return None