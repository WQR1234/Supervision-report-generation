from flask import Flask, request, jsonify

from File_Generation import *

from Online_mode.Yclzbj import yclzbj

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "GET":
        print(request.args)
    elif request.method == "POST":
        data = request.json
        generate_file('The_group/交流监造联系单.docx', 'The_group/交流监造联系单-0.docx', data)
        return jsonify(data)
    return jsonify(request.args)


@app.route('/yclzbj', methods=['POST'])
def origin_material():
    if request.method == "POST":
        data = request.json
        yclzbj(data)
    
    return ''


if __name__ == "__main__":
    app.run(debug=True)