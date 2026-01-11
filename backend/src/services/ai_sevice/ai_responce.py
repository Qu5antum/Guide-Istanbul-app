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
        if message.type != "ai":
            continue

        content = message.content

        if isinstance(content, str) and content.strip():
            return content

        if isinstance(content, list):
            texts = [
                part.get("text")
                for part in content
                if isinstance(part, dict) and part.get("type") == "text"
            ]
            if texts:
                return "\n".join(texts)

    return "Sorry, I couldn't generate a response."
        





