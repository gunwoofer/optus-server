from flask import Flask
from flask_cors import CORS
from flask import request, jsonify
from optus_server import entree_optimize


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return "Hello, cross-origin-world!"


@app.route('/optimize', methods=["POST"])
def optimize():
    data = request.get_json()
    print('ARRIVEE : ' + data['dateArrivee'])
    print('DEPART : ' + data['dateDepart'])
    print('AGE : ' + data['categorieAge'])

    dateArrivee = data['dateArrivee']
    dateDepart = data['dateDepart']
    categorieAge = data['categorieAge']

    solution = entree_optimize(dateArrivee, dateDepart, categorieAge)

    return jsonify(
        test='Reponse du backend, params recus :',
        dateArrivee=dateArrivee,
        dateDepart=dateDepart,
        categorieAge=categorieAge
    )
