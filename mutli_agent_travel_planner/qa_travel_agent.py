from phi.model.groq import Groq  # Assuming this is how you import Groq Llama
from phi.agent import Agent

travel_agent = Agent(
    name="Travel Planner",
    model=Groq(id="llama-3.3-70b-versatile"),  # Adjust if necessary based on actual import
    instructions=[
        "You are a travel planning assistant using Groq Llama.",
        "Help users plan their trips by researching destinations, finding attractions, suggesting accommodations, and providing transportation options.",
        "Give me relevant live Links of each places and hotels you provide by searching on internet (It's important)",
        "Always verify information is current before making recommendations."
    ],
    show_tool_calls=True,
    markdown=True
)