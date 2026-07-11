from langgraph.graph import END


def validation_router(state):
    """
    Decide whether to continue the workflow
    or retry data collection.
    """

    validation = state.get("validation", {})

    if validation.get("passed", False):
        return "PASS"

    return "FAIL"


def reviewer_router(state):
    """
    Decide whether the report is approved
    or needs rewriting.
    """

    review = state.get("review", "")

    if "APPROVED" in review.upper():
        return "END"

    return "REWRITE"
