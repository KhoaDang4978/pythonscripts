from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import os

llm = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

messages = [
    SystemMessage(content="You are a helpful travel assistant for a Vietnamese travel company."),
    HumanMessage(content="What are the best beaches near Ho Chi Minh City?")
]

response = llm.invoke(messages)
print(response.content)
