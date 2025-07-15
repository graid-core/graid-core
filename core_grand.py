from memory_engine import remember
from executor import execute
import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

def process(user_input):
    if "გადმოწერე" in user_input:
        action_type = "DOWNLOAD_ACTION"
    elif "გაგზავნე" in user_input:
        action_type = "SEND_MESSAGE"
    else:
        action_type = "DEFAULT"

    action_response = execute(action_type, user_input)
    response = f"🤖GRAID ბოტის პასუხი და შესრულებული მოქმედება: {action_response}"
    remember(user_input, response)
    return response
