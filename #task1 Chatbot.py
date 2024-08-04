#task1 Chatbot with rule based responses

import datetime

# Get today's date and current time
today = datetime.date.today()
time = datetime.datetime.now().time()
name = input("Chatbot: What's your name? ")
# Function for replies with rules
def replies(user_input):
   
    # Convert everything to lower case to avoid mismatch errors
    user_input = user_input.lower()

    # Rule-based responses
    if 'hello' in user_input or 'hi' in user_input or 'namaste' in user_input or 'salut' in user_input or 'goodevening' in user_input or 'goodmorning' in user_input or 'goodafternoon' in user_input:
        return f"Hello, {name}! How can I assist you today?"
    elif 'how are you' in user_input or 'are you fine' in user_input or 'how have you been' in user_input:
        return 'I am just a chatbot, as much as I would love to share my emotional state (which, by the way, is a solid mix of ones and zeros), let us focus on you! How can I assist you today? Any more questions or topics you would like to explore?'
    elif 'what is your name' in user_input or 'what shall i call you' in user_input:
        return 'I am your personal assistant, you can call me whatever you like.'
    elif 'whats the date' in user_input or 'whats the date today' in user_input:
        return f"Today's date is {today}"
    elif 'whats the time right now' in user_input or 'what time is it' in user_input:
        return f"The time right now is {time}"
    elif 'bye' in user_input or 'goodbye' in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "I'm sorry, I am afraid that would be beyond my boundaries to reply... do you have something else to talk about?"

print(f"Chatbot: Hi {name}! I'm your assistant.How can I assist you?( Type 'bye' to exit.)")

def main():
    while True:
        user_input = input("You: ")
        response = replies(user_input)
        print("Chatbot:", response)
        if 'bye' in user_input.lower() or 'goodbye' in user_input.lower():
            print("Have a nice day!")
            break

if __name__ == "__main__":
    main()
