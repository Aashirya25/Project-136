from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)
@app.route("/")
def displaydata():
    return jsonify({
        "data":data,
        "status":"success"
    })

@app.route("/star")
def planet():
    name = request.args.get("name")
    star_name_data = next(i for i in data if i["name"]==name)
    return jsonify({
        "data":star_name_data,
        "status":"success"
    })

if __name__ == "__main__":
    app.run(debug = True) 

