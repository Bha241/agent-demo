from langchain_core.tools import tool


@tool
def percentage_change(old: float, new: float):

    """
    Calculate percentage change.
    """

    return round(((new-old)/old)*100,2)


@tool
def cagr(beginning: float, ending: float, years: int):

    """
    CAGR calculator.
    """

    return (((ending/beginning)**(1/years))-1)*100