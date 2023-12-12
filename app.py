from flask import Flask, render_template, request, jsonify

from algorithms.spn import run

app = Flask(__name__)


@app.route("/spn", methods=["POST"])
def do_spn():
    # print(request.get_json())
    run(request.get_json())
    return ""


# if __name__ == '__main__':
#     app.run()
