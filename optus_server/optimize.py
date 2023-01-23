import json
from datetime import date, timedelta

from optus_server.day import Day

with open("fares.json") as f:
    fares = json.load(f)["fares"]


reponses = {}

FARES_MONTH = -1
FARES_WEEKLY = -3
FARES_DAY = 5
FARES_1_TICKET = 0
FARES_2_TICKET = 1
FARES_10_TICKET = 4

def entree_optimize(dateArrivee, dateDepart, categorieAge):
    date_by_month = divide_date_by_month(dateArrivee, dateDepart)
    date_by_week = divide_date_by_week(dateArrivee, dateDepart)
    date_by_day = sum(date_by_week, []) # Magie noire pour flatten
    for nbTrajetsMoyen in range (1,9):
        reponses.update({
            nbTrajetsMoyen: optimize(
                [[Day(date, nbTrajetsMoyen) for date in dates] for dates in date_by_month],
                [[Day(date, nbTrajetsMoyen) for date in dates] for dates in date_by_week],
                [Day(date, nbTrajetsMoyen) for date in date_by_day],
                categorieAge,
                nbTrajetsMoyen
            )
        }) 
    return reponses

list()
def optimize(date_by_month, date_by_week, date_by_day, categorieAge, nbTrajets, solution=None):
    if solution is None:
        solution = []
    prices_by_travel = get_price_by_travel(date_by_month, date_by_week, date_by_day, categorieAge, nbTrajets)
    
    best_price = 999
    best_index = None
    index_week_or_month = None
    for type_ticket, prices in prices_by_travel.items():
        if type_ticket == FARES_MONTH or type_ticket == FARES_WEEKLY:
            for number_week_or_month, price in enumerate(prices):
                if price < best_price:
                    best_price = price
                    index_week_or_month = number_week_or_month
                    best_index = type_ticket
        else:
            if prices < best_price:
                best_price = prices
                index_week_or_month = None
                best_index = type_ticket
    
    # On connait maintenant le meilleur ticket, il faut update les differents calendrier
    #TODO: Update les differents calendrier et reappeler la fonction. Ne pas oublier de mettre a jour le nombre de voyage pas day si necessaire
    test = 5
    

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

def get_price_by_travel(date_by_month, date_by_week, date_by_day, categorieAge, nbTrajets, ticket_restant=0):
    prices_by_month = [fares[FARES_MONTH]["price"][categorieAge] / (len(dates) * nbTrajets) for dates in date_by_month]
    prices_by_week = [fares[FARES_WEEKLY]["price"][categorieAge] / (len(dates) * nbTrajets) for dates in date_by_week]

    price_by_24h = fares[FARES_DAY]["price"][categorieAge] / nbTrajets

    nb_trajets_restant = sum([date.nb_trajet for date in date_by_day])

    price_by_1_ticket = fares[FARES_1_TICKET]["price"][categorieAge]
    price_by_2_ticket = fares[FARES_2_TICKET]["price"][categorieAge] / (len(date_by_day) if nb_trajets_restant < 2 else 2)
    price_by_10_ticket = fares[FARES_10_TICKET]["price"][categorieAge] / (len(date_by_day) if nb_trajets_restant < 10 else 10)

    prices = {
        FARES_MONTH: prices_by_month, 
        FARES_WEEKLY: prices_by_week, 
        FARES_DAY: price_by_24h, 
        FARES_1_TICKET: price_by_1_ticket, 
        FARES_2_TICKET: price_by_2_ticket, 
        FARES_10_TICKET: price_by_10_ticket, 
    }

    return prices