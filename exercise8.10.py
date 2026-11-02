def send_messages(messages, sent_messages):
    """Print each message and move it to the sent_messages list."""
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

messages = ["Hello!", "How are you?", "Nice to meet you."]
sent_messages = []

send_messages(messages, sent_messages)

print("\nmessages:", messages)
print("sent_messages:", sent_messages)