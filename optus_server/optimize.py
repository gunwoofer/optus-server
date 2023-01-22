import json
from optus_server.utilities import faire_calendrier

with open("fares.json") as f:
    fares = json.load(f)

reponses = {}
calendrier = []

def entree_optimize(dateArrivee, dateDepart, categorieAge, navetteArrivee, navetteDepart):
    for nbTrajetsMoyen in range (1,9):
        reponses.update({nbTrajetsMoyen: optimize(dateArrivee, dateDepart, categorieAge, nbTrajetsMoyen, navetteArrivee, navetteDepart)}) 
    return reponses


def optimize(dateArrivee, dateDepart, categorieAge, nbTrajets, navetteArrivee, navetteDepart):
    calendrier = faire_calendrier(dateArrivee, dateDepart, navetteArrivee, navetteDepart)
    return "monthly"
