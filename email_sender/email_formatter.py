# from crewai import Crew, Process

# from dotenv import load_dotenv
# import os
# from email_sender import send_email_gmail  # Import the email utility
# import markdown  # Optional: For converting Markdown to HTML


# # # Format the results for email
# def format_results_for_email(result):
#     email_content = "<h2>Your Travel Itinerary</h2>"

#     # Access the tasks_output attribute
#     print(result.tasks_output)
#     output_data = result.tasks_output  # Use the tasks_output attribute

#     # Check if output_data is a list or a dictionary
#     if isinstance(output_data, list):
#         for task_output in output_data:
#             # Assuming each task_output is a TaskOutput object
#             task_name = task_output.description  # Use the description for the task name
#             task_result = task_output.raw  # Get the raw output
            
#             email_content += f"<h3>{task_name.replace('_', ' ').title()}</h3>"
#             if isinstance(task_result, str):
#                 # Convert Markdown to HTML if necessary
#                 html_content = markdown.markdown(task_result)
#                 email_content += f"<div>{html_content}</div>"
#             else:
#                 email_content += f"<div>{str(task_result)}</div>"
#     else:
#         print("Expected a list but got:", type(output_data))
#         email_content += "<h3>Error: Unexpected result format.</h3>"

#     return email_content


# result = {
#     "tasks_output": [
#         {
#             "description": "best_time_to_visit",
#             "raw": "The best time to visit London is during the summer months when the weather is warm and sunny. The peak tourist season is from June to August, so expect higher prices and larger crowds during this time. For a more budget-friendly and less crowded experience, consider visiting in the shoulder seasons of spring (March to May) or autumn (September to November). Winter (December to February) can be cold and rainy, but you'll find lower prices and fewer tourists."
#         },
#         {
#             "description": "accommodation_recommendations",
#             "raw": "# Hotel Recommendations\n\n1. **Hotel A**\n   - *Description*: A lovely hotel with great amenities.\n   - *Price"
#     }]
# }
# formatted_email = format_results_for_email(result)

# # Prompt the user for the receiver's email address
# receiver_email = input("Enter the recipient's email address: ")

# # Send the email
# sender_email = os.getenv("GMAIL_USER")
# sender_password = os.getenv("GMAIL_PASSWORD")

# send_email_gmail(sender_email, sender_password, receiver_email, formatted_email)

import re

def format_email_content(text):
    # Remove ##
    text = text.replace("## ", "").strip()

    # Convert bold markers (**text**) to <strong>text</strong>
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)

    # Convert italic markers (_text_) to <em>text</em>
    text = re.sub(r"_(.*?)_", r"<em>\1</em>", text)

    # Convert new lines to HTML <br> tags for spacing
    text = text.replace("\n\n", "<br><br>")

    # Convert bullet points (* text) to proper HTML list items
    lines = text.split("\n")
    formatted_lines = []
    in_list = False

    for line in lines:
        if line.startswith("* "):  # If it's a bullet point
            if not in_list:
                formatted_lines.append("<ul>")
                in_list = True
            formatted_lines.append(f"<li>{line[2:]}</li>")
        else:
            if in_list:
                formatted_lines.append("</ul>")
                in_list = False
            formatted_lines.append(f"<p>{line}</p>")

    if in_list:
        formatted_lines.append("</ul>")

    formatted_content = "\n".join(formatted_lines)

    # Final HTML Template
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            h2 {{ color: #333; }}
            p {{ font-size: 14px; }}
            ul {{ padding-left: 20px; }}
            li {{ margin-bottom: 10px; }}
            a {{ color: #1a73e8; text-decoration: none; }}
        </style>
    </head>
    <body>
        {formatted_content}
    </body>
    </html>
    """
    
    return html_template
