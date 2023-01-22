from datetime import datetime, timedelta
import calendar

def faire_calendrier(dateArrivee, dateDepart, navetteArrivee, navetteDepart):
    dateArrivee = datetime.strptime(dateArrivee, '%Y-%m-%d')
    dateDepart = datetime.strptime(dateDepart, '%Y-%m-%d')
    date_range = []
    current_date = dateArrivee
    while current_date <= dateDepart:
        date_range.append({
            "date": current_date.strftime('%Y-%m-%d'),
            "day": calendar.day_name[current_date.weekday()],
            "weekend": current_date.weekday() >= 5,
            "airportDay": (current_date == dateArrivee and navetteArrivee) or (current_date == dateDepart and navetteDepart),
            "fare_used": ""
        })
        current_date += timedelta(days=1)
    return date_range