from flask import Flask, jsonify
from flask.globals import request
app = Flask(__name__)
tasks = [
    {
        "id":1,
        "title":"Buy Groceries",
        "description":"Milk, Margerita, chesse, pizza, fruit",
        "done": False,
    },
    {"id":2, "title":"Learn python", "description":"come to RST", "done":True},
]
@app.route("/tasks", methods=["GET"])
def get_task():
    return jsonify({"tasks" : tasks})
@app.route("/homepage", methods=["GET"])
def homepage():
    return "<HTML> <body bgcolor=Blue><h1><marquee>Welcome to RST Forum</maruee>"
@app.route("/mail")
def get_mail():
    return "<html><body><marquee><h1>Welcome to Gmail</h1></marquee></body></html>"
@app.route("/pythonhome")
def  pythonhome():
    myfile = open("C:\\Users\\Dell\\OneDrive\\Desktop\\Python RST Forum\\Automation\\API\\Piyush.html")
    data = myfile.read()
    return data
@app.route("/uber", methods=["GET"])
def fb():
    return {
        "Driver" : "Piyush Bhavsar",
        "OTP" : "6969",
        "ETA" : "10 Mins",
        "Vehicle" : "MH01 9999"
    }
@app.route("/login", methods=["POST"])
def login():
    user = request.form.get("user","bhavsarp456")
    pwd = request.form.get("pwd","Piyush@7523")
    if user == "bhavsarp456" and pwd == "Piyush@7523":
        return "You have successfully Login"
    else:
        return "Chal ja Hava Ane De"
if __name__ == "__main__":
    app.run(debug=True, port = 8080)