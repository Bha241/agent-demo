from fastapi import FastAPI

from graph.workflow import graph

app = FastAPI()


@app.post("/research")
@app.get("/research")
def research(company: str):

    state = {

        "query": company

    }

    config = {
        "configurable": {
            "thread_id": f"api_thread_{company}"
        }
    }

    result = graph.invoke(state, config=config)

    return result
