from backend.api.data_layer.weather_api_impl import WeatherApiImpl
from backend.api.data_layer.weather_api import WeatherApi
from typing import Dict
from .service import Service

class ServiceImpl(Service):
    def __init__(self, weather_api: WeatherApi = WeatherApiImpl()) -> None:
        self.weather_api = weather_api
        
    
    def get_min_max(self, zip: str, days: int = 5) -> Dict[str, str]:
        if not zip:
            raise ValueError('zip can not be empty')
        
        params = {
            'postal_code': zip,
            'days': days
        }
        response = self.weather_api.api_get(params)
        result = []
        for day_data in response['data']:
            result_item = {}
            # datetime is deprecated (https://www.weatherbit.io/api/weather-forecast-16-day)
            result_item['date'] = day_data['valid_date']
            result_item['high'] = day_data['high_temp']
            result_item['low'] = day_data['low_temp']
            result.append(result_item)
        return result
