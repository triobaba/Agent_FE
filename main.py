from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def chatbot():
    return render_template("chat.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
