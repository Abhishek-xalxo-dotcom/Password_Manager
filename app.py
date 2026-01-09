from flask import Flask, render_template, request, jsonify
from password_manager import create_account, login

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username", "").strip()
    password = data.get("password", "")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    success, message = create_account(username, password)
    return jsonify({"success": success, "message": message})

@app.route("/login", methods=["POST"])
def login_user():
    data = request.json
    username = data.get("username", "").strip()
    password = data.get("password", "")

    success, message = login(username, password)
    return jsonify({"success": success, "message": message})

if __name__ == "__main__":
    app.run(debug=True)
