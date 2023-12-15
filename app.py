from flask import Flask, render_template, request, jsonify

from algorithms import spn, str, rr, hrrn, customAlg

app = Flask(__name__)


@app.route("/spn", methods=["POST"])
def do_spn():
    # print(request.get_json())
    return spn.run(request.get_json())


@app.route("/str", methods=["POST"])
def do_str():
    # print(request.get_json())
    return str.run(request.get_json())

@app.route("/rr", methods=["POST"])
def do_rr():
    # print(request.get_json())
    return rr.run(request.get_json())

@app.route("/hrrn", methods=["POST"])
def do_hrrn():
    # print(request.get_json())
    return hrrn.run(request.get_json())

@app.route("/own", methods=["POST"])
def do_own():
    # print(request.get_json())
    return customAlg.run(request.get_json())


# if __name__ == '__main__':
#     app.run()
