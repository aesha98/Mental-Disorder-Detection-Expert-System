from flask import Flask, render_template, request, flash

import DisorderCheck

app = Flask(__name__)
app.config['SECRET_KEY'] = '73a4b6ca8cb647a20b71423e31492452'


@app.route("/")
@app.route("/home")
def Homepage():
    # cases, cured, death = CurrentStats.currentStatus()
    return render_template("TestHomepage.html", feedback="False")


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template("PageNotFound.html")


@app.route("/about")
def About():
    return render_template("About.html")


@app.route("/infected")
def Infected():
    return render_template("Infected.htm", disease="Nothing")


@app.route("/noninfected")
def NonInfected():
    return render_template("NonInfected.htm")


@app.route("/disorder/<prediction>", methods=["GET"])
def disorder(prediction):
    illness = prediction
    if illness == "Dimorphic_hemmorhoids":  # Dimorphic_hemmorhoids

        return render_template("Depression.html")
    else:
        return render_template(f"{illness}.html")


@app.route("/disorderprediction", methods=["POST", "GET"])
def Disease():
    symptoms = []
    if request.method == "POST":
        rf = request.form
        # print(rf)
        for key, value in rf.items():
            # print(key)
            if value == "0":
                pass
            else:
                symptoms.append(value)

        prediction = DisorderCheck.predicts(symptoms)
        if prediction:
            sick = prediction
            disorder(sick)
            return render_template("Infected.htm", disease=prediction)

        else:
            return render_template("NonInfected.htm")
    return render_template("checksymptom.html")


if __name__ == '__main__':
    app.run(debug=True)
