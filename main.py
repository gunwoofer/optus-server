from flask import Flask
from flask_cors import CORS
from flask import request, jsonify
from optus_server import entree_optimize
from optus_server import generate_fare_combinations_for_duration

app = Flask(__name__)
CORS(app)


def main():
    # Valeurs MOCK pour tester sans client
    navetteArrivee = True
    navetteDepart = True
    dateArrivee = "2023-01-21"
    dateDepart = "2023-02-5"
    categorieAge = "none"

    solution = entree_optimize(dateArrivee, dateDepart, categorieAge, navetteArrivee, navetteDepart)



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

    # Valeurs MOCK en attendant que le client l'envoie
    navetteArrivee = True
    navetteDepart = True

    solution = entree_optimize(dateArrivee, dateDepart, categorieAge, navetteArrivee, navetteDepart)

    return jsonify(
        test='Reponse du backend, params recus :',
        dateArrivee=dateArrivee,
        dateDepart=dateDepart,
        categorieAge=categorieAge
    )


if __name__ == '__main__':
    main()