# Chatbot testing repository

Welcome to the Chatbot Testing Repository! This repository contains tools and scripts to test chatbots written in Python. Below are instructions on how to test a simple terminal-based chatbot, a chatbot with a UI.

## Table of Contents

- [Getting Started](#getting-started)
- [Testing a Simple Chatbot](#testing-a-simple-chatbot)
- [Testing a Chatbot with UI](#testing-a-chatbot-with-ui)
- [Contributing](#contributing)
- [License](#license)

## Getting started

Macbook: 

To get started, ensure you have Python 3 installed on your machine. You can check your Python version by running:

```bash
python3 --version
```

## Testing a simple Chatbot

To test a simple chatbot that operates in the terminal, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Tesena-smart-testing/chat_bots.git
   cd chatbot-testing-repo
   ```
2. Run the test script using Python 3:

   ```bash
   python3 test_chat_bot.py
   ```

This will execute the tests for the terminal-based chatbot.

## Testing a Chatbot with UI

To test a chatbot with a graphical user interface (UI), follow these steps:

1. Ensure you have Flask installed. If not, install it using pip:

   ```bash
   pip install flask
   ```
2. Start the Flask app:

   ```bash
   python3 app.py
   ```
3. Open your web browser and navigate to `http://localhost:5000` to interact with the chatbot UI.
