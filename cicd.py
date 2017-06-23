# -*- coding: utf-8 -*-
import math
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

SBWorldDate = datetime(2017,7,20)
SEC_TO_DAY = 60 * 60 * 24  # 60 seconds / min * 60 min / hour * 24 hour

@app.route("/")
def index():
    return render_template("index.html",
                           time = get_minutes_left(datetime.now(), SBWorldDate),
                           unit = u"分",
                           today = datetime.now().strftime('%Y.%m.%d'))

def get_minutes_left(now, target):
    return int(math.ceil((target - now).total_seconds() / 60))

def get_day_left(now, target):
    return int(math.ceil((target - now).total_seconds() / SEC_TO_DAY))

if __name__ == "__main__":
    app.run()
