from langchain.messages import HumanMessage
from backend.src.core.ai_config.ai_assistant_config import agent


# ai responce by user prompt
async def ai_response(prompt: str):
    result = await agent.ainvoke({
        "messages": [
            HumanMessage(content=prompt)
        ]   
    })

    for message in reversed(result["messages"]):
        if message.type == "ai" and message.content:
            return message.content

    return "Sorry, I couldn't find any places for your request."




