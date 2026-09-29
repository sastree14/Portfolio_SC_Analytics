from typing import TypedDict
from langgraph.graph import StateGraph, END

class State(TypedDict):
    request: str
    plan: str
    review: str
    approved: bool

def planner(state: State):
    return {"plan": f"Plan for: {state['request']}"}

def reviewer(state: State):
    return {"review": "reviewed", "approved": True}

graph=StateGraph(State)
graph.add_node("planner",planner)
graph.add_node("reviewer",reviewer)
graph.set_entry_point("planner")
graph.add_edge("planner","reviewer")
graph.add_edge("reviewer",END)
workflow=graph.compile()
