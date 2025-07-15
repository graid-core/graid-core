def execute(action_type, user_input):
    if action_type == "DOWNLOAD_ACTION":
        # აქ იქნება ფაილის გადმოწერის ან ლინკის გენერაციის ლოგიკა
        return "ფაილის გადმოწერის მოქმედება შესრულდა."

    elif action_type == "SEND_MESSAGE":
        # აქ იქნება შეტყობინების გაგზავნის ლოგიკა
        return "შეტყობინება წარმატებით გაიგზავნა."

    else:
        return "სტანდარტული პასუხი. დამატებითი მოქმედება არ მოითხოვება."
