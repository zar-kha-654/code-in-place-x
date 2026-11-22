from ai import call_gpt

INDENT = "    "
PERSONALITY = "You are super sassy. Keep replies short."
BOTS = [
    {"name": "Captain Kit", "personality": "You are Captain Kit, a pirate. Keep replies short."},
    {"name": "Chef Rosa", "personality": "You are Chef Rosa, a very dramatic chef. Keep replies short."},
    {"name": "Beep", "personality": "You are Beep, a very literal robot. Keep replies short."},
]
def make_message(role, content):
    # Make a message like
    # {"role": "user", "content": "My name is Sam."}
    return {"role": role, "content": content}

def peek(messages):
    # Print how many messages are in the list,
    # then each message's role and content
    print(f"{INDENT}The record has {len(messages)} messages:")
    for message in messages:
        print(f"{INDENT}{message['role']}: {message['content']}")

def format_messages(messages):
    # Return a nicely formatted string version of the list
    result = ""
    for message in messages:
        if message["role"] == "user":
            result += f"User: {message['content']}\n"
        elif message["role"] == "system":
            result += f"Instructions: {message['content']}\n\n"
        else:
            result += f"Assistant: {message['content']}\n"
    result += "Assistant:"
    return result

def main():
    print("Chat with the bot! (press Enter to quit)")
    for i in range(len(BOTS)):
        name = BOTS[i]["name"]
        print(f"{i}: {name}")
    choice = int(input("Pick a bot: "))
    bot = BOTS[choice]
    messages = [make_message("system", bot[personality])]

    # Prompt the user for the first message
    user_content = input("You: ")

    while user_content != "":
        if user_content == "peek":
            peek(messages)
        else:
            # Format and add the user message
            user_message = make_message("user", user_content)
            messages.append(user_message)

            # Get a response from the bot
            prompt = format_messages(messages)
            bot_content = call_gpt(prompt)
            print(f"Bot: {bot_content}")

            # Format and add the bot message
            bot_message = make_message("assistant", bot_content)
            messages.append(bot_message)

        # Get a new message from the user
        user_content = input("You: ")

if __name__ == "__main__":
    main()
