from typing import Union, Dict, Any
from .weather_api import WeatherApi
from dotenv import load_dotenv
import os
import requests

load_dotenv()
# ?postal_code=78613&days=5&key=
class WeatherApiImpl(WeatherApi):
    def __init__(
        self,
        api_key: Union[str, None] = os.getenv("API_KEY"),
        api_url: Union[str, None] = f"https://api.weatherbit.io/v2.0/forecast/daily",
    ) -> None:
        self.api_url = api_url
        self.api_key = api_key

    # def generate_final_url(self, params: Dict[str, str]) -> None:
    #     if not self.api_key:
    #         raise ValueError('api_key is not set')

    #     if not self.api_url:
    #         raise ValueError('api_url is not set')
    #     params['key'] = self.api_key
    #     req = PreparedRequest()
    #     req.prepare_url(self.api_url, params)
    #     self.final_url = req.url

    def api_get(self, params: Dict[str, str]) -> Dict[Any, Any]:
        params["key"] = self.api_key
        r = requests.get(self.api_url, params=params)
        return r.json()
