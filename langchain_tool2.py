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

@tool
def get_travel_time(route: str, pickup: str) -> str:
    """Get the travel time for a Vie Limo route and pickup point."""
    times = {
        ("vung tau", "district 1"): "2 hours 15 minutes",
        ("vung tau", "airport"): "3 hours",
        ("mui ne", "district 1"): "4-5 hours",
        ("mui ne", "airport"): "5 hours",
        ("ho tram", "district 1"): "2 hours 30-45 minutes",
        ("ho tram", "airport"): "3 hours 15 minutes",
    }
    key = (route.lower(), pickup.lower())
    return times.get(key, "Travel time not available for this route.")


llm = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

agent = create_agent(
    model=llm,
    tools=[get_ticket_price, get_travel_time],
    system_prompt="You are a helpful Vie Limo travel assistant."
)

response = agent.invoke({
    "messages": [("user", "I want to go to Vung Tau from District 1, what's the price for seat A and how long will it take?"
)]
})
print(response["messages"][-1].content)
