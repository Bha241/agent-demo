from langgraph.graph import StateGraph, END
from graph.routers import validation_router, reviewer_router
from memory.memory import memory

from graph.state import InvestmentState

from agents.planner import planner
from agents.researcher import researcher
from agents.financial import financial
from agents.sentiment import sentiment
from agents.validation import validation
from agents.risk import risk
from agents.report_writer import report_writer
from agents.reviewer import reviewer


builder = StateGraph(InvestmentState)

# -------------------------
# Nodes
# -------------------------

builder.add_node("planner", planner)
builder.add_node("researcher", researcher)
builder.add_node("financial", financial)
builder.add_node("sentiment", sentiment)
builder.add_node("validation", validation)
builder.add_node("risk", risk)
builder.add_node("report_writer", report_writer)
builder.add_node("reviewer", reviewer)

# -------------------------
# Entry
# -------------------------

builder.set_entry_point("planner")

# -------------------------
# Edges
# -------------------------

builder.add_edge("planner", "researcher")

builder.add_edge("researcher", "financial")

builder.add_edge("financial", "sentiment")

builder.add_edge("sentiment", "validation")

builder.add_conditional_edges(
    "validation",
    validation_router,
    {
        "PASS": "risk",
        "FAIL": "researcher"
    }
)

builder.add_edge("risk", "report_writer")

builder.add_edge("report_writer", "reviewer")

builder.add_conditional_edges(
    "reviewer",
    reviewer_router,
    {
        "END": END,
        "REWRITE": "report_writer",
    },
)



graph = builder.compile(
    checkpointer=memory
)
