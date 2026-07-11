from langchain_core.tools import tool
from ddgs import DDGS


def get_nse_announcements(company: str):
    """
    Get latest NSE announcements for a company.
    """
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(f"{company} NSE corporate announcements filings", max_results=3))
        return results
    except Exception as e:
        return [{"title": f"NSE search failed", "body": str(e)}]


def get_bse_announcements(company: str):
    """
    Get latest BSE announcements for a company.
    """
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(f"{company} BSE corporate announcements filings", max_results=3))
        return results
    except Exception as e:
        return [{"title": f"BSE search failed", "body": str(e)}]


@tool
def nse_filings(company: str):
    """
    Latest NSE announcements.
    """
    return get_nse_announcements(company)


@tool
def bse_filings(company: str):
    """
    Latest BSE announcements.
    """
    return get_bse_announcements(company)