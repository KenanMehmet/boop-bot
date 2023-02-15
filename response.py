def handle_response(message):
    p_message = message.content.lower()
    print(p_message)
    
    if p_message == "!avatar":
        return f"{message.author.avatar}"

    #if p_message[0] == "!":
    #    return handle_command(message)

    if p_message == "beep":
        return f"@{message.author} boop"

    if p_message == "roll":
        return "4"

    if p_message == '!help':
        return "``` I cant help you Dan ```"

"""
def handle_command(message) -> str:
    print("Hello")
    print(message.author.avatar)
    
"""