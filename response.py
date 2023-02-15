def handle_response(message):
    p_message = message.lower()
    print(p_message)
    if p_message == "beep":
        return "boop"

    if p_message == "roll":
        return "4"

    if p_message == '!help':
        return "``` I cant help you Dan ```"