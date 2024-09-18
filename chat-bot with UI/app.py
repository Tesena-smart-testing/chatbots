
from flask import Flask, render_template, request, jsonify
from chat_bot_api import ChatBot

app = Flask(__name__)
bot = ChatBot()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = bot.parse_message(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
