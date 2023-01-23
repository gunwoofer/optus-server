import json
from datetime import date, timedelta


with open("fares.json") as f:
    fares = json.load(f)


reponses = {}


def entree_optimize(dateArrivee, dateDepart, categorieAge):
    for nbTrajetsMoyen in range (1,9):
        reponses.update({nbTrajetsMoyen: optimize(dateArrivee, dateDepart, categorieAge, nbTrajetsMoyen)}) 
    return reponses


def optimize(dateArrivee, dateDepart, categorieAge, nbTrajets):
    return "monthly"


def divide_date_by_month(arrival_date, departure_date):
    arrival_date = date(*map(int, arrival_date.split("-")))
    departure_date = date(*map(int, departure_date.split("-"))) + timedelta(days=1)
    current_month = arrival_date.month
    current_day = arrival_date
    result = []
    current_list_month = []
    while current_day <= departure_date:
        if current_day.month != current_month or current_day == departure_date:
            result.append(current_list_month)
            current_list_month = []
            current_month = current_day.month
        current_list_month.append(current_day.strftime('%Y-%m-%d'))
        current_day += timedelta(days=1)
    return result

def divide_date_by_week(arrival_date, departure_date):
    arrival_date = date(*map(int, arrival_date.split("-")))
    departure_date = date(*map(int, departure_date.split("-"))) + timedelta(days=1)
    current_week = arrival_date.isocalendar()[1]
    current_day = arrival_date
    result = []
    current_list_week = []
    while current_day <= departure_date:
        if current_day.isocalendar()[1] != current_week or current_day == departure_date:
            result.append(current_list_week)
            current_list_week = []
            current_week = current_day.isocalendar()[1]
        current_list_week.append(current_day.strftime('%Y-%m-%d'))
        current_day += timedelta(days=1)
    return result

