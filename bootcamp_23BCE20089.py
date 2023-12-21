def chatbot(message):
    if "hi" in message or "hey" in message or "hello" in message:
        return "Hello! How can I assist you today?"
    elif "what is your name" in message:
        return "My name is ChatBot. Nice to meet you!"
    elif "how are you" in message:
        return "I'm doing well, thank you! How about you?"
    elif "sorry" in message:
        return "No problem, it happens."
    elif "quit" in message:
        return "Goodbye! It was nice chatting with you. Have a great day!"
    elif "cool" in message:
        return "Thanks! I'm glad you think it's cool."
    elif "nice " in message:
        return "I'm glad you think it's nice!"
    elif "bye" in message:
        return " Aw, bye! It was nice chatting with you. If you ever want to ask more silly questions or just have a chat, feel free to come back anytime. Take care"
    else:
        return "I'm sorry, I didn't quite catch that. Can you please rephrase?"

while True:
    user_input = input("User: ")
    response = chatbot(user_input)
    print("ChatBot:", response)
