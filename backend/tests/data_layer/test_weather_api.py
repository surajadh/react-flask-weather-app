from api.data_layer.weather_api_impl import WeatherApiImpl
from api.data_layer.weather_api import WeatherApi
import pytest

# def test_generate_final_url():
#     weather_api: WeatherApi = WeatherApiImpl(api_url='http://someurl.com/test', api_key='somekey')
#     weather_api.generate_final_url({
#         'test1': 1,
#         'test2': 2
#     })
#     assert weather_api.final_url == "http://someurl.com/test?test1=1&test2=2&key=somekey"
# {'city_name': 'Williamson', 'country_code': 'US',
# 'data': [{'app_max_temp': 33.3, 'app_min_temp': 20.9, 'clouds': 10, 'clouds_hi': 0, 'clouds_low': 10, 'clouds_mid': 0, 'datetime': '2022-10-12', 'dewpt': 16, 'high_temp': 33.5, 'low_temp': 18.3, 'max_dhi': None, 'max_temp': 33.5, 'min_temp': 20.4, 'moon_phase': 0.85105, 'moon_phase_lunation': 0.58, 'moonrise_ts': 1665624045, 'moonset_ts': 1665591324, 'ozone': 269.1, 'pop': 0, 'precip': 0, 'pres': 977.7, 'rh': 59, 'slp': 1012.6, 'snow': 0, 'snow_depth': 0, 'sunrise_ts': 1665577927, 'sunset_ts': 1665619457, 'temp': 26.3, 'ts': 1665558060, 'uv': 6.5, 'valid_date': '2022-10-12', 'vis': 14.844, 'weather': {'code': 801, 'icon': 'c02d', 'description': 'Few clouds'}, 'wind_cdir': 'SW', 'wind_cdir_full': 'southwest', 'wind_dir': 226, 'wind_gust_spd': 6.9, 'wind_spd': 3.8}, {'app_max_temp': 27.6, 'app_min_temp': 17.3, 'clouds': 4, 'clouds_hi': 16, 'clouds_low': 0, 'clouds_mid': 0, 'datetime': '2022-10-13', 'dewpt': 5.8, 'high_temp': 29.2, 'low_temp': 15.8, 'max_dhi': None, 'max_temp': 29.2, 'min_temp': 17.9, 'moon_phase': 0.771411, 'moon_phase_lunation': 0.61, 'moonrise_ts': 1665712581, 'moonset_ts': 1665681255, 'ozone': 276.7, 'pop': 0, 'precip': 0, 'pres': 980.6, 'rh': 35, 'slp': 1014.8, 'snow': 0, 'snow_depth': 0, 'sunrise_ts': 1665664366, 'sunset_ts': 1665705789, 'temp': 23.1, 'ts': 1665637260, 'uv': 6.8, 'valid_date': '2022-10-13', 'vis': 11.469, 'weather': {'code': 801, 'icon': 'c02d', 'description': 'Few clouds'}, 'wind_cdir': 'ENE', 'wind_cdir_full': 'east-northeast', 'wind_dir': 60, 'wind_gust_spd': 8.3, 'wind_spd': 4.9}, {'app_max_temp': 29.4, 'app_min_temp': 15.8, 'clouds': 24, 'clouds_hi': 30, 'clouds_low': 11, 'clouds_mid': 11, 'datetime': '2022-10-14', 'dewpt': 8.7, 'high_temp': 30.3, 'low_temp': 21.6, 'max_dhi': None, 'max_temp': 30.3, 'min_temp': 15.8, 'moon_phase': 0.682569, 'moon_phase_lunation': 0.65, 'moonrise_ts': 1665801355, 'moonset_ts': 1665771002, 'ozone': 276.2, 'pop': 20, 'precip': 0.009994507, 'pres': 981.6, 'rh': 40, 'slp': 1015, 'snow': 0, 'snow_depth': 0, 'sunrise_ts': 1665750805, 'sunset_ts': 1665792122, 'temp': 23.3, 'ts': 1665723660, 'uv': 6.7, 'valid_date': '2022-10-14', 'vis': 16.26, 'weather': {'code': 802, 'icon': 'c02d', 'description': 'Scattered clouds'}, 'wind_cdir': 'ESE', 'wind_cdir_full': 'east-southeast', 'wind_dir': 102, 'wind_gust_spd': 6.2, 'wind_spd': 3.9}, {'app_max_temp': 31.8, 'app_min_temp': 22.3, 'clouds': 35, 'clouds_hi': 50, 'clouds_low': 9, 'clouds_mid': 30, 'datetime': '2022-10-15', 'dewpt': 17.2, 'high_temp': 32.6, 'low_temp': 21.4, 'max_dhi': None, 'max_temp': 32.6, 'min_temp': 21.5, 'moon_phase': 0.588087, 'moon_phase_lunation': 0.68, 'moonrise_ts': 1665890408, 'moonset_ts': 1665860482, 'ozone': 270.2, 'pop': 0, 'precip': 0, 'pres': 982.8, 'rh': 60, 'slp': 1012.4, 'snow': 0, 'snow_depth': 0, 'sunrise_ts': 1665837245, 'sunset_ts': 1665878455, 'temp': 26.5, 'ts': 1665810060, 'uv': 5.3, 'valid_date': '2022-10-15', 'vis': 24.128, 'weather': {'code': 802, 'icon': 'c02d', 'description': 'Scattered clouds'}, 'wind_cdir': 'S', 'wind_cdir_full': 'south', 'wind_dir': 173, 'wind_gust_spd': 9, 'wind_spd': 5.3}, {'app_max_temp': 32.7, 'app_min_temp': 22.1, 'clouds': 57, 'clouds_hi': 39, 'clouds_low': 43, 'clouds_mid': 27, 'datetime': '2022-10-16', 'dewpt': 18.4, 'high_temp': 33.7, 'low_temp': 20.9, 'max_dhi': None, 'max_temp': 33.7, 'min_temp': 21.4, 'moon_phase': 0.491102, 'moon_phase_lunation': 0.71, 'moonrise_ts': 1665979742, 'moonset_ts': 1665949648, 'ozone': 264.7, 'pop': 20, 'precip': 0.125, 'pres': 982.5, 'rh': 64, 'slp': 1012.1, 'snow': 0, 'snow_depth': 0, 'sunrise_ts': 1665923685, 'sunset_ts': 1665964724, 'temp': 26.8, 'ts': 1665896460, 'uv': 5.2, 'valid_date': '2022-10-16', 'vis': 24.128, 'weather': {'code': 803, 'icon': 'c03d', 'description': 'Broken clouds'}, 'wind_cdir': 'SSE', 'wind_cdir_full': 'south-southeast', 'wind_dir': 165, 'wind_gust_spd': 7.6, 'wind_spd': 4.4}], 'lat': '30.5052', 'lon': '-97.8203', 'state_code': 'TX', 'timezone': 'America/Chicago'}

# {
#     'app_max_temp': 33.3,
#     'app_min_temp': 20.9,
#     'clouds': 10,
#     'clouds_hi': 0,
#     'clouds_low': 10,
#     'clouds_mid': 0,
#     'datetime': '2022-10-12',
#     'dewpt': 16,
#     'high_temp': 33.5,
#     'low_temp': 18.3,
#     'max_dhi': None,
#     'max_temp': 33.5,
#     'min_temp': 20.4,
#     'moon_phase': 0.85105,
#     'moon_phase_lunation': 0.58,
#     'moonrise_ts': 1665624045,
#     'moonset_ts': 1665591324,
#     'ozone': 269.1,
#     'pop': 0,
#     'precip': 0,
#     'pres': 977.7,
#     'rh': 59,
#     'slp': 1012.6,
#     'snow': 0,
#     'snow_depth': 0,
#     'sunrise_ts': 1665577927,
#     'sunset_ts': 1665619457,
#     'temp': 26.3,
#     'ts': 1665558060,
#     'uv': 6.5,
#     'valid_date': '2022-10-12',
#     'vis': 14.844,
#     'weather': {'code': 801, 'icon': 'c02d', 'description': 'Few clouds'},
#     'wind_cdir': 'SW',
#     'wind_cdir_full': 'southwest',
#     'wind_dir': 226,
#     'wind_gust_spd': 6.9,
#     'wind_spd': 3.8
# }
@pytest.mark.skip("Unskip to make actual call to the service and validate the result")
def test_api_get():
    weather_api: WeatherApi = WeatherApiImpl()
    response = weather_api.api_get({"postal_code": "78613", "days": 5})
    print(response)
    valid_keys = ["city_name", "country_code", "data"]
    valid_data_keys = ["app_max_temp", "app_min_temp"]
    for key in valid_keys:
        assert key in response.keys()
    assert len(response["data"]) == 5
    for key in valid_data_keys:
        assert key in response["data"][0].keys()
