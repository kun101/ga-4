import requests
from urllib.parse import urlencode

API_KEY = 'AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv'
LOCATOR_API = 'https://locator-service.api.bbci.co.uk/locations'
WEATHER_API_BASE = 'https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated'

def get_location_id(city: str) -> str:
    city = city.lower()
    params = {
        'api_key': API_KEY,
        's': city,
        'stack': 'aws',
        'locale': 'en',
        'filter': 'international',
        'place-types': 'settlement,airport,district',
        'order': 'importance',
        'a': 'true',
        'format': 'json'
    }
    url = f"{LOCATOR_API}?{urlencode(params)}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    try:
        loc_id = data['response']['results']['results'][0]['id']
    except (KeyError, IndexError) as e:
        raise ValueError(f"Could not find location ID for city '{city}'") from e

    return str(loc_id)

def get_weather_forecast(location_id: str) -> dict:
    url = f"{WEATHER_API_BASE}/{location_id}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    forecasts = data.get('forecasts')
    if not forecasts:
        raise ValueError(f"No forecasts found for location ID {location_id}")

    daily_descriptions = {}
    for day in forecasts:
        summary = day.get('summary', {})
        report = summary.get('report', {})
        local_date = report.get('localDate')
        description = report.get('enhancedWeatherDescription')

        if local_date and description:
            daily_descriptions[local_date] = description

    return daily_descriptions

if __name__ == "__main__":
    city_name = "Jakarta"
    try:
        loc_id = get_location_id(city_name)
        print(f"Location ID for {city_name}: {loc_id}")

        forecast = get_weather_forecast(loc_id)

        print(f"\nWeather forecast for {city_name}:")
        print("{")
        for i, (date, desc) in enumerate(forecast.items()):
            comma = "," if i < len(forecast) - 1 else ""
            print(f'  "{date}": "{desc}"{comma}')
        print("}")

    except Exception as e:
        print(f"Error: {e}")
