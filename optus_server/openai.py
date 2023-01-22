import json
from itertools import combinations_with_replacement
from datetime import datetime, timedelta

def generate_fare_combinations_for_duration(arrival_date, departure_date, category):
    with open('fares.json') as json_file:
        fares = json.load(json_file)['fares']

    arrival_datetime = datetime.strptime(arrival_date, "%Y-%m-%d")
    departure_datetime = datetime.strptime(departure_date, "%Y-%m-%d")
    duration = (departure_datetime - arrival_datetime).days
    fare_combinations = []
    for i in range(1, len(fares)+1):
        fare_combinations += list(combinations_with_replacement(fares, i))
    fare_combinations = [comb for comb in fare_combinations if all(fare['include747'] for fare in comb)]
    fare_combinations = [comb for comb in fare_combinations if not any("YUL Aeroport 747" in fare["name"] for fare in comb)]
    fare_combinations = [comb for comb in fare_combinations if not any("747" in fare["name"] for fare in comb)]
    fare_combinations = [comb for comb in fare_combinations if sum(fare['price'][category]*(duration//30) if fare["name"] == "Monthly" else fare['price'][category]*(duration//7) if fare["name"] == "Weekly" else fare['price'][category]*(duration//3) if fare["name"] == "3 days" else fare['price'][category]*(duration//1) if fare["name"] == "24h" else fare['price'][category]*(duration//10) if fare["name"] == "10 trips" else fare['price'][category]*(duration//7) if fare["name"] == "Unlimited weekend" else fare['price'][category]*(duration//7) if fare["name"] == "Unlimited evening" else fare['price'][category]*(duration//2) if fare["name"] == "2 trip" else fare['price'][category]*duration if fare["name"] == "1 trip"  else fare['price'][category] for fare in comb) <= duration]
    return fare_combinations
