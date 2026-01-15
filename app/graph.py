from langgraph.graph import StateGraph, END
from app.state import AgentState
from app.nodes import intent_node, weather_node, chat_node

def route(state: AgentState):
    if state["intent"] == "weather":
        return "weather"
    return "chat"

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("intent", intent_node)
    graph.add_node("weather", weather_node)
    graph.add_node("chat", chat_node)

    graph.set_entry_point("intent")

    graph.add_conditional_edges(
        "intent",
        route,
        {
            "weather": "weather",
            "chat": "chat"
        }
    )

    graph.add_edge("weather", END)
    graph.add_edge("chat", END)

    return graph.compile()
