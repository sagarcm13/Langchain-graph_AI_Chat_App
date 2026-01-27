from typing import TypedDict, Optional

class AgentState(TypedDict):
    user_input: str
    intent: Optional[str]
    city: Optional[str]
    response: Optional[str]
    rag_context: Optional[str]
