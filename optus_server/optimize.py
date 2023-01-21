import json


with open("fares.json") as f:
    fares = json.load(f)


reponses = {}


def entree_optimize(dateArrivee, dateDepart, categorieAge):
    for nbTrajetsMoyen in range (1,9):
        reponses.update({nbTrajetsMoyen: optimize(dateArrivee, dateDepart, categorieAge, nbTrajetsMoyen)}) 
    return reponses


def optimize(dateArrivee, dateDepart, categorieAge, nbTrajets):
    return "monthly"
