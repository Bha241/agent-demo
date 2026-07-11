from langchain_core.tools import tool
from duckduckgo_search import DDGS


@tool
def search_web(query: str):
    """
    Search the web for general information.
    """

    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=5))

    return results
