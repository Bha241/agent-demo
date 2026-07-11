from tools.search_tool import search_web
from tools.tavily_search import tavily_search
from tools.yahoo_finance import (
    stock_price,
    company_profile
)
from tools.market_news import latest_market_news
from tools.indian_filings import (
    nse_filings,
    bse_filings
)
from tools.calculator import (
    percentage_change,
    cagr
)


TOOLS = [

    search_web,

    tavily_search,

    stock_price,

    company_profile,

    latest_market_news,

    nse_filings,

    bse_filings,

    percentage_change,

    cagr,
]
