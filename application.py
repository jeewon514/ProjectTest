from flask import url_for, session, Flask, render_template, request, redirect

application = Flask(__name__)
application.secret_key = "abcdef1234##"

ID = "JeewonKoo"
PW = "JeewonKoo"

@application.route("/")
def home():
    if "userID" in session:
        return render_template("home.html",username = session.get("userID"), login = True)
    else:
        return render_template("home.html", login = False)

@application.route("/login", methods = ["get"])
def login():
    global ID, PW
    _id_ = request.args.get("loginId")
    _password_ = request.args.get("loginPw")

    if ID == _id_ and PW == _password_:
        session["userID"] = _id_
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))

@application.route("/logout")
def logout():
    session.pop("userID")
    return redirect(url_for("home"))

application.run(host = "0.0.0.0")