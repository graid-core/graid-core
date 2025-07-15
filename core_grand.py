from memory_engine import remember
from executor import execute

def process(user_input):
    if "ფაილი" in user_input:
        action_type = "DOWNLOAD_ACTION"
    elif "მესიჯი" in user_input:
        action_type = "SEND_MESSAGE"
    else:
        action_type = "DEFAULT"

    action_response = execute(action_type, user_input)
    response = f"🤖GRAND ბოტის პასუხი და შესრულებული მოქმედება: {action_response}"
    remember(user_input, response)
    return response
