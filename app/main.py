from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Anderson flask app porta 8080!!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
