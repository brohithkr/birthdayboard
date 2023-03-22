from flask import Flask, render_template
from birthdayreminder import *
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

@app.route("/")
def getbirthdaylist():
    bdlist = getBDlist()
    is_bd = (len(bdlist) != 0)
    datetoday = datetime.now(timezone('Asia/Kolkata')).strftime("%d-%m-%Y %H:%M:%S")
    return render_template("index.html",is_bd=is_bd,bdlist=bdlist,datetoday=datetoday)

if __name__=="__main__":
    app.run(True)
