#!/bin/env python3

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Bill, you SysAdmin genius you. They should hire you at HPC."

if __name__ == "__main__":
    app.run(port=5000)