from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
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
    return prices.get(key, "Price not found for this route and seat type.")

llm = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

tools = [get_ticket_price]

agent = create_agent(
    model=llm,
    tools=tools,
    prompt="You are a helpful assistant that uses ReAct patterns."
)

response = agent.invoke({"messages": [("user", "What's the ticket price to Vung Tau?")]})
print(response["messages"][-1].content)

if response.tool_calls:
    print(f"Model wants to call: {response.tool_calls[0]['name']}")