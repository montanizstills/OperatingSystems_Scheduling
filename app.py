from flask import Flask, render_template, request, jsonify

from algorithms import spn, str, rr, hrrn, customAlg

app = Flask(__name__)


@app.route("/spn", methods=["POST"])
def do_spn():
    # print(request.get_json())
    spn.run(request.get_json())
    return ""


@app.route("/str", methods=["POST"])
def do_str():
    # print(request.get_json())
    str.run(request.get_json())
    return ""

@app.route("/rr", methods=["POST"])
def do_rr():
    # print(request.get_json())
    rr.run(request.get_json())
    return ""

@app.route("/hrrn", methods=["POST"])
def do_hrrn():
    # print(request.get_json())
    hrrn.run(request.get_json())
    return ""

@app.route("/own", methods=["POST"])
def do_own():
    # print(request.get_json())
    customAlg.run(request.get_json())
    return ""


# if __name__ == '__main__':
#     app.run()
