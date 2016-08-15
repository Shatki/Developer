from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Alenka!"

if __name__ == "__main__":
    app.run(host='192.168.0.218', port=80, debug=True)
