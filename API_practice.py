# %%
# Import the requests library.
import requests

# %%
# Import the API key.
from config import weather_api_key

# %%
# Starting URL for Weather Map API Call.
url = "https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22" + weather_api_key
print(url)

# %%
# Create an endpoint URL for a city.
city_url = url + "&q=" + "Boston"
print(city_url)

# %%
