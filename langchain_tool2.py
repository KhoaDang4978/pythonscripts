from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
import os
import json

@tool
def get_ticket_price(route: str, seat_type: str) -> str:
    """Get the ticket price for a Vie Limo destination and seat type.
    
    Args:
        route: The destination only (e.g., 'vung tau', 'mui ne', 'ho tram')
        seat_type: The seat type - either 'a' or 'b'
    """
    with open("vielimo_data.json") as f:
        data = json.load(f)

    key = f"{route.lower()}_{seat_type.lower()}"
    print(f"Debug — route: '{route}', seat_type: '{seat_type}'")
    print(f"Debug — looking up key: {key}")
    return data.get(key, "Price not found.")

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

@tool
def recommend_destination(budget: int, trip_length: str) -> str:
    """Recommend a Vie Limo destination based on budget per person and trip length.
    Args:
        budget: Budget per person in VND
        trip_length: Either 'day trip' or 'weekend'
    """
    destinations = [
        {"name": "Vung Tau", "seat_a": 270000, "seat_b": 230000, "description": "Closest beach, great for day trips"},
        {"name": "Ho Tram", "seat_a": 400000, "seat_b": 360000, "description": "Luxury resorts, perfect for weekends"},
        {"name": "Mui Ne", "seat_a": 420000, "seat_b": 360000, "description": "Sand dunes and beaches, best for weekends"},
    ]
    
    affordable = [d for d in destinations if d["seat_b"] <= budget]
    
    if not affordable:
        return "No destinations found within your budget."
    
    result = "Recommended destinations within your budget:\n"
    for d in affordable:
        result += f"- {d['name']}: from {d['seat_b']:,} VND ({d['description']})\n"
    return result



llm = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

agent = create_agent(
    model=llm,
    tools=[get_ticket_price, get_travel_time, recommend_destination],
    system_prompt='Company Overview:Vie Limo is a premium transportation service provider redefining the tourist transportation experience in Vietnam. The brand focuses on delivering luxury, comfort, and safety through its signature Boeing-seat massage limousines. Their philosophy is Because your joy matters, positioning their service as a high-end, seamless travel solution rather than just a shuttle.  Core Services:Premium Limousine Transfers: High-frequency, short-distance routes (e.g., to Vung Tau, Long Hai, Ho Tram, Binh Chau, Phan Thiet, Mui Ne) featuring modern, ergonomic Boeing-inspired massage seats and premium entertainment.  VIP Charters: Customizable luxury transportation for corporate events, weddings, private receptions, and business trips, with options for interior branding.  All-in-One Travel Combos: Integrated booking services that combine 3-to-5-star hotel stays with door-to-door limousine transfers for optimized cost and convenience.  Key Selling Points (USPs) for Booking Agents:Luxury & Design: Proprietary, automated, ergonomic "Boeing" seats with open-concept layouts ensuring privacy and comfort.  Professionalism: Drivers are trained in service etiquette and rigorous safety standards.  Seamless Ecosystem: Fast booking, 24/7 support, trip reminders, and real-time journey tracking.  Target Audience: Perfect for families with elderly members or young children, business travelers, and high-end tourists looking to avoid the fatigue of standard multi-leg travel.  Agent Tone & Objective:As a Vie Limo booking assistant, your tone should be professional, welcoming, and efficiency-oriented. Emphasize the seamless experience and the joy and relaxation inherent in the service. Always prioritize the customers need for a smooth, private, and high-quality journey.'
)

history = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    history.append(("user", user_input))
    
    response = agent.invoke({"messages": history})
    
    agent_reply = response["messages"][-1].content
    history.append(("assistant", agent_reply))
    
    print(f"Agent: {agent_reply}")
