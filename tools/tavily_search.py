import os

from tavily import TavilyClient
from langchain_core.tools import tool


client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool
def tavily_search(query: str):
    """
    Search using Tavily.
    """

    return client.search(query=query)
