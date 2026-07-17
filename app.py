from flask import Flask, render_template, request, jsonify
from chatbox import chatbot  # Assuming your chatbot file is named `chatbox.py`

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")
    print("User message:", user_message)  # Debugging line
    if user_message:
        response = chatbot.respond(user_message)
        print("Chatbot response:", response)  # Debugging line
        return jsonify({"response": response})
    return jsonify({"response": "Sorry, I didn't understand that."})

if __name__ == "__main__":
    app.run(debug=True)
