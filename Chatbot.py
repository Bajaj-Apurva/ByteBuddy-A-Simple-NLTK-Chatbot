import nltk
from nltk.chat.util import Chat, reflections
import datetime

patterns = [
    (r'hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']),
    (r'how are you', ['I am good, thank you!', 'I am doing well, how about you?']),
    (r'(.*) your name', ['I am a chatbot created with NLTK.', 'You can call me ByteBuddy.']),
    (r'(.*) help (.*)', ['Sure, I can help you. What do you need assistance with?', 'How can I assist you today?']),
    (r'(.*) thank you|thanks', ['You\'re welcome!', 'No problem.']),
    (r'what is your purpose|why are you here', ['I am here to assist you!']),
    (r'your age', ['I don\'t have an age. I\'m just a computer program.']),
    (r'(.*) your creator', ['I was created by an OpenAI.']),
    (r'(.*) name (.*)', ['I\'m more interested in your name. What is your name?']),
    (r'my name is (.*)', ['Nice to meet you, {}!', 'Hello, {}!']),
    (r'current date', [f'Today is {datetime.date.today()}']),
    (r'current time', [f'The current time is {datetime.datetime.now().strftime("%H:%M:%S")}']),
    (r'quit', ['Goodbye!', 'Bye!', 'Take care.']),
    (r'(.*)', ['I\'m sorry, I didn\'t understand that. Can you please rephrase?', 'I\'m still learning.']),
]

chatbot = Chat(patterns, reflections)

def chat():
    print("Hello! I am your ByteBuddy. Type 'quit' to exit.")
    while True:
        user_input = input("User: ")
        if user_input.lower() == 'quit':
            print("ByteBuddy: Goodbye! See you next time!")
            break
        response = chatbot.respond(user_input)
        print("ByteBuddy", response.format(chatbot.respond(user_input).split(" ")[-1]))

if __name__ == "__main__":
    chat()

