from flask import Flask, render_template
import os

app = Flask(__name__)

todos = [ {"ID": 1, "TEXT": "Goto Work" }, 
{"ID": 2, "TEXT": "Watch Netflix" },
{"ID": 3, "TEXT": "Complete my flask app" },
{"ID": 4, "TEXT": "Meditate" }
]
port = int(os.getenv('PORT', 8000))

@app.route("/")
def home():
    return "Hello World"

@app.route("/html")
def html():
    return render_template("home.html")

@app.route("/todo")
def todo():
    return render_template("todo.html", todos=todos)

app.run(host="0.0.0.0", port=port)