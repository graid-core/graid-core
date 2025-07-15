def route_action(user_input):
    if "გადმოწერე" in user_input or "download" in user_input:
        return "DOWNLOAD_ACTION"
    elif "გაგზავნე" in user_input or "send" in user_input:
        return "SEND_MESSAGE"
    else:
        return "GPT_REPLY"
