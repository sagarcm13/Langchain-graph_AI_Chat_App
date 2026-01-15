# ChatBotAppWithWeatherAPI

A conversational AI chatbot powered by Google Gemini and LangChain, with integrated weather information via OpenWeatherMap API.

## Features
- Natural language chat using Gemini LLM (Google GenAI)
- Weather queries for any city (current temperature, humidity, etc.)
- Intent detection (weather/general chat)
- Modular, extendable graph-based architecture (LangGraph)

## Project Structure
```
main.py                # Entry point for the chatbot
app/
  llm.py               # Gemini LLM integration
  intent.py            # Intent detection logic
  weather.py           # Weather API integration
  nodes.py             # Graph nodes for intent, weather, chat
  graph.py             # Graph construction and routing
  state.py             # Agent state definition
requirements.txt       # Python dependencies
.env                   # API keys (not committed)
AIenv/                 # Python virtual environment (optional)
```

## Setup Instructions

### 1. Clone the repository
```
git clone https://github.com/sagarcm13/Langchain-graph_AI_Chat_App.git
cd Langchain-graph_AI_Chat_App
```

### 2. Create and activate a virtual environment (recommended)
```
python3 -m venv AIenv
source AIenv/bin/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Set up API keys
Create a `.env` file in the project root with the following content:
```
GEMINI_API_KEY=your_gemini_api_key_here
WEATHER_API_KEY=your_openweathermap_api_key_here
```
- [Get a Gemini API key](https://ai.google.dev/)
- [Get an OpenWeatherMap API key](https://openweathermap.org/api)

### 5. Run the chatbot
```
python main.py
```

## Usage
- Type any message to chat with the AI.
- Ask about the weather in any city (e.g., "What's the weather in Paris?").
- Type `exit` to quit.

## Example
```
🤖 Gemini AI Agent (type 'exit' to quit)

You: What's the weather in London?
AI: 🌦️ Weather in London
Temperature: 12°C
Feels like: 10°C
Humidity: 80%
Condition: Light Rain

You: Tell me a joke
AI: Why did the scarecrow win an award? Because he was outstanding in his field!
```

## Notes
- The `.env` file and `AIenv/` are excluded from version control.
- The chatbot uses Google Gemini for both intent detection and general chat.
- Weather data is fetched live from OpenWeatherMap.

## Requirements
See `requirements.txt` for all dependencies.
