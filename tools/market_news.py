from langchain_core.tools import tool
from duckduckgo_search import DDGS


def latest_news(company: str):
    """
    Helper function to get the latest news for a company.
    """
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(f"{company} latest business news", max_results=5))
        return results
    except Exception as e:
        return [{"title": f"News search failed", "body": str(e)}]


@tool
def latest_market_news(company: str):
    """
    Returns latest market news.
    """
    return latest_news(company)
