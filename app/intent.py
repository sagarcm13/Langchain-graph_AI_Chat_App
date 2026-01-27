from langchain_core.messages import HumanMessage
from app.llm import GeminiChat
import json

llm = GeminiChat()

PROMPT = """
You are an intent classifier for an AI assistant.

User message: "{text}"

Return ONLY valid JSON in this format:

{{
  "intent": "weather" | "personal" | "github" | "portfolio" | "general",
  "city": "<correct city name or null>"
}}

Intent Rules:
- If user asks about weather, temperature, climate, rain → intent = weather.
- If user asks about Sagar or Sagar CM, his life, personal things, profile, hobbies, education, GitHub link, portfolio link → intent = personal.
- If user asks about latest repositories, commits, contributions, README, stars → intent = github.
- If user asks to open, analyze, summarize portfolio website or recent work → intent = portfolio.
- Otherwise → intent = general.

City Rules:
- Fix spelling mistakes in city names (example: banglore → Bangalore).
- If no city is mentioned → city = null.
- Only extract city if intent = weather.

Strict Rules:
- Return ONLY valid JSON.
- Do NOT add explanations.
- Do NOT use markdown.
"""

def detect_intent(text: str) -> dict:
    response = llm.invoke([
        HumanMessage(content=PROMPT.format(text=text))
    ])

    try:
        return json.loads(response.content)
    except Exception as e:
        print("⚠️ Intent parsing failed:", e)
        return {
            "intent": "general",
            "city": None
        }
