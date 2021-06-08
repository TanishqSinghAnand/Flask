from flask import Flask, jsonify, request

app = Flask(__name__)

persons = [
    {
        'id': 1,
        'Name': u'Raju',
        'Contact': u'9987644456',
        'done': False
    },
    {
        'id': 2,
        'Name': u'Rahul',
        'Contact': u'9876543222',
        'done': False
    }
]


@app.route("/")
def helloWorld():
    return "Hello World"


@app.route("/add-person", methods=["POST"])
def add_person():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": 'Please provide the data'
        }, 400)
    person = {
        'id': persons[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    persons.append(person)
    return jsonify({
        'status': "success",
        'message': "person added succesfully"
    })


@app.route("/get-person")
def getPerson():
    return jsonify({'data': persons})


if(__name__ == "__main__"):
    app.run(debug=True)
