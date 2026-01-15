from langchain_core.messages import HumanMessage
from app.llm import GeminiChat
import json

llm = GeminiChat()

PROMPT = """
You are an intent classifier.

User message: "{text}"

Return ONLY valid JSON in this format:

{{
  "intent": "weather" or "general",
  "city": "<correct city name or null>"
}}

Rules:
- If user asks about weather, temperature, climate → intent = weather.
- Fix spelling mistakes in city names.
- If no city mentioned → city = null.
- Do not add explanation or markdown.
"""

def detect_intent(text: str) -> dict:
    response = llm.invoke([
        HumanMessage(content=PROMPT.format(text=text))
    ])

    try:
        return json.loads(response.content)
    except Exception:
        return {"intent": "general", "city": None}
