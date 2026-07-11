import sys
from graph.workflow import graph


if len(sys.argv) > 1:
    query = sys.argv[1]
else:
    query = input("Enter Company Name:\n")

state = {

    "query": query

}

config = {
    "configurable": {
        "thread_id": "investment_research_thread"
    }
}

result = graph.invoke(state, config=config)

print()

print("="*80)

print(result.get("report", "No report generated."))