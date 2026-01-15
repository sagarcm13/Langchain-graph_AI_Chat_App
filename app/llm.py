import os
from dotenv import load_dotenv
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage
from langchain_core.outputs import ChatResult, ChatGeneration
from google import genai
from langchain_core.messages import HumanMessage


load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiChat(BaseChatModel):
    model: str = "gemini-2.5-flash"

    def _generate(self, messages, **kwargs):
        prompt = "\n".join([m.content for m in messages])
        response = client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        ai_message = AIMessage(content=response.text)
        generation = ChatGeneration(message=ai_message)
        return ChatResult(generations=[generation])

    @property
    def _llm_type(self) -> str:
        return "gemini"
