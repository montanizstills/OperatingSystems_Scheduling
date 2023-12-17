from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("./webpage.html")
    # return "Hello World, Operating Systems Projects"


if __name__ == '__main__':
    app.run()
