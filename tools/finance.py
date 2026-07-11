import numpy as np


def pe_ratio(price, eps):

    if eps == 0:
        return None

    return round(price / eps, 2)


def earnings_growth(current, previous):

    return round(((current - previous) / previous) * 100, 2)


def debt_to_equity(total_debt, equity):

    return round(total_debt / equity, 2)


def profit_margin(net_income, revenue):

    return round((net_income / revenue) * 100, 2)


def roe(net_income, equity):

    return round((net_income / equity) * 100, 2)


def cagr(beginning, ending, years):

    return round((((ending / beginning) ** (1 / years)) - 1) * 100, 2)
