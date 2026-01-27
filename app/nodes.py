from langchain_core.messages import HumanMessage
from app.llm import GeminiChat
from app.state import AgentState
from app.intent import detect_intent
from app.weather import get_weather
from app.rag.retriever import get_relevant_context

llm = GeminiChat()

# -------------------------
# Intent Node
# -------------------------
def intent_node(state):
    query = state["user_input"]
    print("🧭 Detecting intent...")

    result = detect_intent(query)

    state["intent"] = result.get("intent")
    state["city"] = result.get("city")

    print("🎯 Intent:", state["intent"], "| City:", state["city"])
    return state


# -------------------------
# Weather Node
# -------------------------
def weather_node(state: AgentState) -> AgentState:
    city = state["city"]

    if not city:
        return {"response": "Please tell me the city name 🌍"}

    try:
        data = get_weather(city)

        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"].title()

        return {
            "response": (
                f"🌦️ Weather in {city}\n"
                f"Temperature: {temp}°C\n"
                f"Feels like: {feels}°C\n"
                f"Humidity: {humidity}%\n"
                f"Condition: {desc}"
            )
        }

    except Exception as e:
        return {"response": f"❌ Could not fetch weather for {city}"}

# -------------------------
# Chat Node
# -------------------------
# -------------------------
# Chat Node
# -------------------------
def chat_node(state: AgentState) -> AgentState:
    user_text = state["user_input"]
    context = state.get("rag_context")

    # If RAG context exists, inject it
    if context:
        prompt = f"""
You are an assistant answering based on the user's personal profile.

Context:
{context}

User Question:
{user_text}
"""
        result = llm.invoke([
            HumanMessage(content=prompt)
        ])
    else:
        result = llm.invoke([
            HumanMessage(content=user_text)
        ])

    return {"response": result.content}

def rag_node(state):
    print("🧠 Fetching personal context from RAG...")
    query = state["user_input"]

    context = get_relevant_context(query)

    state["rag_context"] = context
    return state
