# Simple Rule-Based Chatbot

print("🤖 Hello! I am ChatBot. Type 'exit' to end the chat.")

while True:
    user_input = input("You: ").lower()  # convert input to lowercase

    if user_input == "exit":
        print("ChatBot: Bye! Have a nice day! 👋")
        break

    # Greeting
    elif user_input in ["hi", "hello", "hey"]:
        print("ChatBot: Hello! How can I help you today?")

    # Asking about well-being
    elif user_input in ["how are you", "how are you?"]:
        print("ChatBot: I am a bot, but I'm doing great! 😄 How about you?")

    # Asking about bot’s name
    elif user_input in ["what is your name", "who are you"]:
        print("ChatBot: I am a simple chatbot created by Rajesh.")

    # Asking for help
    elif user_input in ["help", "i need help"]:
        print("ChatBot: Sure! I can answer simple questions like greetings, your name, and well-being.")

    # Default response
    else:
        print("ChatBot: Sorry, I didn't understand that. Can you rephrase?")
