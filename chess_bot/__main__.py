from flask import Flask, render_template, request, session

app = Flask(__name__)

USERS = {}

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
