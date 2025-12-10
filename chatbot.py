import random

def process_input(user_input):
    """
    Processes the user's input and prints a predefined response
    using rule-based matching with if-elif-else.
    """
    user_input = user_input.lower()

    # 1. Greetings
    if user_input in ["hello", "hi", "hey", "hola"]:
        print("Chatbot: Hello! How can I help you today?")

    # 2. Status check
    elif "how are you" in user_input or "how are you doing" in user_input:
        print("Chatbot: I'm fine, thanks! I'm a simple rule-based bot.")

    # 3. Farewells
    elif user_input in ["bye", "goodbye", "see you"]:
        print("Chatbot: Goodbye! Have a great day.")

    # 4. Asking name
    elif "your name" in user_input or "who are you" in user_input:
        print("Chatbot: I'm a basic chatbot built with Python.")

    # 5. Help or options
    elif "help" in user_input or "options" in user_input:
        print("Chatbot: You can greet me, ask how I am, or say goodbye.")

    # 6. Default fallback
    else:
        fallback_responses = [
            "Chatbot: Hmm, I didn’t get that. Try 'hello' or 'how are you'.",
            "Chatbot: Sorry, I’m still learning. Can you rephrase?",
            "Chatbot: I don’t understand yet, but I’m improving!"
        ]
        print(random.choice(fallback_responses))


def start_chatbot():
    """
    Initializes and runs the main chatbot loop.
    """
    print("🤖 Chatbot initialized. Type 'quit' to exit the conversation.")
    print("-" * 40)

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "quit":
            print("Chatbot: Thanks for chatting!")
            break
        else:
            process_input(user_input)

# Run the chatbot
if __name__ == "__main__":
    start_chatbot()