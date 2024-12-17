from flask import Flask as fl

app = fl(__name__)

@app.route('/')
def hello_world():
    return "Website for testing"

if __name__ == '__main__':
    app.run(debug=True)
