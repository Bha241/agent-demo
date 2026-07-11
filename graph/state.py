from typing import TypedDict, List, Dict, Any, Optional
from typing import Annotated
from langgraph.graph.message import add_messages


class InvestmentState(TypedDict):

    query: str

    messages: Annotated[list, add_messages]

    company: Optional[Dict[str, Any]]

    stock_price: Optional[Dict[str, Any]]

    financials: Optional[Dict[str, Any]]

    news: Optional[List]

    filings: Optional[List]

    sentiment: Optional[Dict[str, Any]]

    risks: Optional[Dict[str, Any]]

    report: Optional[str]

    review: Optional[str]

    validation: Optional[Dict[str, Any]]

    financial_analysis: Optional[str]