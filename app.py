from flask import Flask, request, render_template, send_file, abort
import os

app = Flask(__name__)
FLAG_FILE = "admin.txt"

# Write the flag to disk once (hidden from main website)
if not os.path.exists(FLAG_FILE):
    with open(FLAG_FILE, "w") as f:
        f.write("flag{http_methods_mastered}")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/admin.txt", methods=["GET", "OPTIONS", "PUT"])
def admin_file():
    if request.method == "OPTIONS":
        return "", 200, {
            "Allow": "GET, PUT, OPTIONS"
        }

    if request.method == "PUT":
        return "Sorry, you can't overwrite this file.", 403

    if request.method == "GET":
        return send_file(FLAG_FILE)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
