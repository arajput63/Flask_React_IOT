from flask import Flask,  render_template, request
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/echo')
def echo_socket(ws):
    print("ws")
    while True:
        message = ws.receive()
        ws.send(message[::-1])
        print(message)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/echo_test", methods=['GET'])
def echo_test():
    return render_template('echo_test.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
