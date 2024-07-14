from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "GET":
        print(request.args)
    elif request.method == "POST":
        data = request.json
        if 'abc' in data:
            data['abc'] += 100
        return jsonify(data)
    return jsonify(request.args)


if __name__ == "__main__":
    app.run(debug=True)