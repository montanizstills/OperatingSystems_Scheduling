from flask import Flask, render_template, request, jsonify, redirect, url_for

from algorithms import spn, srt, rr, hrrn, customAlg, fcfs, mlf

app = Flask(__name__)

# app.config["CORS_HEADERS"] = ['Access-Control-Allow-Origin']
# app.config["CORS_ORIGINS"] = ["*"]

@app.route('/',  methods=["GET", "POST"])
def home():
    return render_template("webpage.html")

@app.route('/process', methods=["GET", "POST"])
def process():
    # Get the selected radio button value
    selected_option = request.form.get('algorithm')

    # Process dynamic form inputs
    form_data = {}
    if request.method == "POST":
        numProcesses = int(request.form.get("numProcesses"))
        arrivalString = "arrivalTime"
        serviceString = "serviceTime"
        for i in range(numProcesses):
            form_data[str(i)] = str((int(request.form.get(arrivalString+str(i))), int(request.form.get(serviceString+str(i)))))

        # For demonstration purposes, just print the form data
        print("Form Data:", form_data)

        # Determine the redirection URL based on the selected option
        result = ""
        if selected_option == 'fcfs':
            result =  fcfs.run(form_data)
        elif selected_option == 'rr':
            result = rr.run(form_data)
        elif selected_option == 'hrrn':
            result = hrrn.run(form_data)
        elif selected_option == 'mlf':
            result = mlf.run(form_data)
        elif selected_option == 'spn':
            result = spn.run(form_data)
        elif selected_option == 'srt':
            result = srt.run(form_data)

         # Format the data for display in the template
        if selected_option != 'mlf':
            formatted_data = {
                "turnaroundtimes": [
                    f"Process {process}: {val}"
                    for process, val in result["turnaroundtimes"].items()
                ],
                "averageTurnAroundTime": f"Average Turnaround Time: {result['averageTurnAroundTime']}"
            }
            print("formatted data: ")
            print(formatted_data)
            return render_template("webpage.html", entries=formatted_data)

        else:
            return render_template("mlfOutput.html", entries = result)





if __name__ == '__main__':
    app.run()