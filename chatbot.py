import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ["hi|hello", ["Hello!", "Hi there!"]],
    ["what is your name?", ["I'm a chatbot created by you."]],
    ["how are you?", ["I'm doing well, thanks!", "All good!"]],
    ["quit", ["Bye! Take care."]]
]

def chatbot():
    print("Hi! I'm your AI chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()


chatbot()

    

