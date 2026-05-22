from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
import os

@tool
def get_ticket_price(route: str, seat_type: str) -> str:
    """Get the ticket price for a Vie Limo route and seat type."""
    prices = {
        ("vung tau", "b"): "230,000 VND",
        ("vung tau", "a"): "270,000 VND",
        ("mui ne", "b"): "360,000 VND",
        ("mui ne", "a"): "420,000 VND",
        ("ho tram", "b"): "360,000 VND",
        ("ho tram", "a"): "400,000 VND",
    }
    key = (route.lower(), seat_type.lower())
    return prices.get(key, "Price not found.")

llm = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

agent = create_agent(
    model=llm,
    tools=[get_ticket_price],
    system_prompt="You are a helpful Vie Limo travel assistant."
)

response = agent.invoke({
    "messages": [("user", "What's the ticket price to Vung Tau for seat type A?")]
})
print(response["messages"][-1].content)