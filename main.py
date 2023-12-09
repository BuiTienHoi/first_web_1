from flask import Flask,render_template,url_for,request,redirect
app = Flask(__name__)

@app.route("/")
def base_file():
    return render_template("home.html")
@app.route("/mini", methods = ["POST","GET"])
def minigame():
        first_name = ''
        secound_name = ''
        sex = ''
        if request.method == "POST":
            first_name = request.form['Name']
            secound_name = request.form['Surename']
            sex = request.form.get('Gender')
            if first_name =='' or secound_name =='' or sex is None:
                    return render_template('mini.html')
        return render_template('mini.html',var_1 = first_name,var_2 = secound_name ,var_3 = sex)
@app.route("/<name>")
def button_file(name):
    pages = ["lives","tourism","infor"]
    if name in pages:
        return render_template(name +".html")
    else:
        return render_template('base.html')
if __name__ == "__main__":
    app.run()