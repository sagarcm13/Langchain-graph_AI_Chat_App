from langchain_core.messages import HumanMessage
from app.llm import GeminiChat
from app.state import AgentState
from app.intent import detect_intent
from app.weather import get_weather

llm = GeminiChat()

# -------------------------
# Intent Node
# -------------------------
def intent_node(state: AgentState) -> AgentState:
    result = detect_intent(state["user_input"])
    print("🧠 Detected:", result)

    return {
        "intent": result["intent"],
        "city": result["city"]
    }

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
def chat_node(state: AgentState) -> AgentState:
    result = llm.invoke([
        HumanMessage(content=state["user_input"])
    ])
    return {"response": result.content}
