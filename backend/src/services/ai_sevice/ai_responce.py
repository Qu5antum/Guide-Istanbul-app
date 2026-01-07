from langchain.messages import HumanMessage
from backend.src.core.ai_config.ai_assistant_config import agent


async def ai_response(user_prompt: str):
    result = agent.invoke({
        "messages": [
            HumanMessage(content=user_prompt)
        ]
    })
    return result["messages"][-1].content




