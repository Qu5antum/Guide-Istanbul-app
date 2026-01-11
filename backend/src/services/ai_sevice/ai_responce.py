from langchain.messages import HumanMessage
from backend.src.core.ai_config.ai_assistant_config import agent


# ai responce by user prompt
async def ai_response(prompt: str, lat: float, lon: float):
    full_prompt = (
        f"{prompt}\n"
        f"My location: latitude {lat}, longitude {lon}."
    )

    result = await agent.ainvoke({
        "messages": [HumanMessage(content=full_prompt)],
    })

    for message in reversed(result["messages"]):
        if message.type in ("ai", "tool") and message.content:
            return message.content
        





