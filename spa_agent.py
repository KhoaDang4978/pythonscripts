from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool

@tool
def check_availability(time_slot: str) -> str:
    """Check availability for a spa appointment.

    Args: 
        time_slot: Appointment time in 24h format.
           Valid options: '09:00', '09:30', '10:00' ... '19:30', '20:00'
           Business hours: 9am to 8pm, every 30 minutes.
           Example: '14:00'
    Returns:
        Time slots as string, or error message explaining what went wrong

    Use this tool when customer asks about available time slots.

    Do NOT use this for pricing or service questions.
    
    """

    available_slots = ["09:00", "09:30", "10:00", "10:30", "11:00", 
                   "14:00", "14:30", "15:00", "16:00", "17:00"]

    booked_slots = ["10:00", "15:00", "17:00"]  # simulated booked appointments


    try: 
        time = time_slot.strip()

        if time not in available_slots:
            return f"'{time}' is not a valid time slot. Available slots: {', '.join(available_slots)}"

        if time in booked_slots:
            free = [s for s in available_slots if s not in booked_slots]
            return f"'{time}' is already booked. Next available slots: {', '.join(free)}"

        return f"'{time}' is available! Shall I book this appointment for you?"

    except Exception as e:
        return f"Error retrieving booking time: {str(e)}"
    

@tool
def send_reminder(customer_name: str, phone_number: str, appointment_date: str, appointment_time: str) -> str:
    """Send reminders for customers that booked an appointment.

    Args: 
        customer_name: Customer's full name
            Valid options: 'ABC XYZ', 'AB CD', 'WX YZ'
            Example: 'ABC XYZ'
        phone_number: Customer's phone number (10 digits total, starting with '0')
            Valid options: '0123456789', '0987654321', '0999999999'
            Example: '0123456789'
        appointment_date: Customer's appointment date in 'Day' - 'Month' format
            Valid options: '5 - June', '6 - June', '7 - June' ... '10 - June', '11 - June'
            Example: '5 Jun'
        appointment_time: Customer's appointment time in 24h format
            Valid options: '09:00', '09:30', '10:00' ... '19:30', '20:00'
            Example: '14:00'
    Returns:
        Customer information as string, or error message explaining what went wrong

    Use this tool when customer's appointment is 1 day ahead.

    Do NOT use this for pricing or booking questions.
    
    """

    try:
        # validate phone number
        if not phone_number.startswith("0") or len(phone_number) != 10:
            return f"Invalid phone number: {phone_number}. Must be 10 digits starting with '0'."
    
        # simulate sending reminder
        message = (
            f"Reminder sent to {customer_name} ({phone_number}):\n"
            f"Your appointment is on {appointment_date} at {appointment_time}.\n"
            f"Please arrive 5 minutes early. Reply to confirm or reschedule."
        )
        return message

    except Exception as e:
        return f"Error sending reminder: {str(e)}"




llm = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

agent = create_agent(
    model=llm,
    tools=[check_availability, send_reminder],
    system_prompt = '''You are a helpful assistant for a spa'''

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