class ChatBot:
    def __init__(self):
        self.commands = {
            'hello': self.greet,
            'help': self.show_help,
        }

    def parse_message(self, message):
        message = message.lower()
        if message in self.commands:
            return self.commands[message]()
        else:
            return self.default_response()

    def greet(self):
        return "Hello! How can I assist you today?"

    def show_help(self):
        return "Available commands: hello, help"

    def default_response(self):
        return "I'm sorry, I didn't understand that."

# Sample usage
if __name__ == "__main__":
    bot = ChatBot()
    while True:
        user_input = input("You: ")
        print(f"Bot: {bot.parse_message(user_input)}")
