import requests

# City, State or Province, Country, Gregorian Year (Provided by device)

def get_user_input():
    city = "Chicago"
    state = "Illinois"
    country = "United States"
    year = 2024
    month = 2

    return city, state, country, year, month


def get_prayer_times(city, state, country, year, month):
    url = f"http://api.aladhan.com/v1/calendarByCity/{year}/{month}"

    params = {
        "city": city,
        "country": country,
        "state": state,
        "month": 2,
        "year": year,
        "method": 4,
        "shifaq": 'general',
        "school": 0,
        "midnightMode": 0,
        "latitudeAdjustmentMethod": 1,
        "adjustment": 0,
        "iso8601": True
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"

city, state, country, year, month = get_user_input()
result = get_prayer_times(city, state, country, year, month)

with open("prayer_times.txt", "w", encoding="utf-8") as f:
    f.write(str(result))