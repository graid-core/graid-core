def execute(action_type, user_input):
    if action_type == "DOWNLOAD_ACTION":
        return "📥 გადმოწერა წარმატებით დასრულდა"
    elif action_type == "SEND_MESSAGE":
        return "📤 შეტყობინება გაიგზავნა"
    else:
        return "🤖 GPT პასუხი: " + user_input
