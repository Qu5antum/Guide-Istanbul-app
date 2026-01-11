from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.messages import SystemMessage
from langchain.agents import create_agent
from backend.src.core.config.config import settings
from backend.src.core.tools.user_searching_tool import user_search_request_by_locationtype_and_distance



llm = ChatGoogleGenerativeAI(
    model=settings.MODEL,
    temperature=0.3,
    api_key=settings.AI_API_KEY
)


system_message = SystemMessage(
    content=settings.SYSTEM_PROMPT
)

tools = [user_search_request_by_locationtype_and_distance]

agent = create_agent(
    model=llm,
    system_prompt=system_message,
    tools=tools,
)
















