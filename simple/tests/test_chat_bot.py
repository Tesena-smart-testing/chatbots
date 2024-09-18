import unittest
from ..chat_bot import ChatBot

class TestChatBot(unittest.TestCase):

    def setUp(self):
        self.bot = ChatBot()

    def test_greet_command(self):
        response = self.bot.parse_message("hello")
        self.assertEqual(response, "Hello! How can I assist you today?")

    def test_help_command(self):
        response = self.bot.parse_message("help")
        self.assertEqual(response, "Available commands: hello, help")

    def test_default_response(self):
        response = self.bot.parse_message("unknown command")
        self.assertEqual(response, "I'm sorry, I didn't understand that.")

    def test_case_insensitivity(self):
        response = self.bot.parse_message("HeLLo")
        self.assertEqual(response, "Hello! How can I assist you today?")

    def test_empty_message(self):
        response = self.bot.parse_message("")
        self.assertEqual(response, "I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    unittest.main()
