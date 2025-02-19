from nltk.chat.util import Chat, reflections

class ChatBot:
    def __init__(self):
        self.pairs = [
            [r"(.*)my name is (.*)", ["Hello %2, how are you today?"]],
            [r"(.*)help(.*)", ["I can help you! How can I assist you?"]],
            [r"(.*) your name ?", ["My name is ChatBot, but you can call me Bot!"]],
            [r"how are you (.*) ?", ["I'm doing great! How about you?", "I'm just a chatbot, but I'm good!"]],
            [r"(hi|hey|hello|hola|holla)(.*)", ["Hello!", "Hey there!", "Hi!"]],
            [r"quit", ["Goodbye! Have a nice day!", "See you soon!"]],
            [r"(.*)", ["That's interesting!", "Tell me more!"]]
        ]

        # Initialize chatbot
        self.chat = Chat(self.pairs, reflections)

    def start_chat(self):
        """Start chatbot conversation."""
        self.chat.converse()
