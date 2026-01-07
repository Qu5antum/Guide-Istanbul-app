from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.messages import SystemMessage
from langchain.agents import create_agent
from backend.src.core.config.config import settings


llm = ChatGoogleGenerativeAI(
    model=settings.MODEL,
    temperature=0.4,
    api_key=settings.AI_API_KEY
)

system_message = SystemMessage(
    content=settings.SYSTEM_PROMPT
)

tools = []

agent = create_agent(
    model=llm,
    system_prompt=system_message,
    tools=tools,
)














