import json
from flask import Flask,  request, g, jsonify
app = Flask(__name__)

cachedData = []

@app.route("/", methods=["GET"])
def getData():
    return jsonify(cachedData)

@app.route("/", methods=["POST"])
def appendData():
    cachedData.append(request.json)
    return "appended stuff"
    


if __name__ == "__main__":
    app.run()