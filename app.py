from flask import Flask, render_template, request, jsonify

from algorithms import spn, srt, rr, hrrn, customAlg, fcfs

app = Flask(__name__)
app.config["CORS_HEADERS"] = ['Access-Control-Allow-Origin']
app.config["CORS_ORIGINS"] = ["*"]

@app.route("/fcfs", methods=["POST"])
def do_fcfs():
    # print(request.get_json())
    return fcfs.run(request.get_json())

@app.route("/spn", methods=["POST"])
def do_spn():
    # print(request.get_json())
    return spn.run(request.get_json())


@app.route("/srt", methods=["POST"])
def do_str():
    # print(request.get_json())
    return srt.run(request.get_json())

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


if __name__ == '__main__':
    app.run()
