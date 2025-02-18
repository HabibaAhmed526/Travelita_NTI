from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import time

# Define the time agent details
class BestTimeAgent(BaseModel):
    start_time: time = Field(..., title="Start Time of the Event", description="The starting time of the event/activity.")
    end_time: time = Field(..., title="End Time of the Event", description="The ending time of the event/activity.")
    duration: str = Field(..., title="Duration", description="The duration of the event/activity.")
    notes: Optional[str] = Field(None, title="Additional Notes", description="Additional notes about the time, such as peak hours or recommendations.")
    day: Optional[str] = Field(None, title="Day", description="The day of the week or specific date of the event.")
    
# Define a model for structured output that includes multiple time slots for different events or activities
class BestTimeList(BaseModel):
    best_times: List[BestTimeAgent] = Field(..., title="List of Best Times", min_items=1)

# # Example data using the BestTimeAgent model
# best_time_data = BestTimeList(
#     best_times=[
#         BestTimeAgent(
#             start_time=time(9, 0),  # 9:00 AM
#             end_time=time(10, 30),  # 10:30 AM
#             duration="1.5 hours",
#             notes="Best time for meetings or quick discussions.",
#             day="Monday"
#         ),
#         BestTimeAgent(
#             start_time=time(14, 0),  # 2:00 PM
#             end_time=time(16, 0),  # 4:00 PM
#             duration="2 hours",
#             notes="Recommended time for brainstorming sessions.",
#             day="Wednesday"
#         ),
#         BestTimeAgent(
#             start_time=time(18, 30),  # 6:30 PM
#             end_time=time(20, 0),  # 8:00 PM
#             duration="1.5 hours",
#             notes="Ideal for team wrap-up meetings or debriefs.",
#             day="Friday"
#         )
#     ]
# )

