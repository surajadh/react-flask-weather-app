from abc import abstractmethod
from typing import Any, Dict, Protocol, Union


class WeatherApi(Protocol):
    api_key: Union[str, None] = None
    api_url: Union[str, None] = None
    # final_url: Union[str, None] = None

    @abstractmethod
    def api_get(self, params: Dict[str, str]) -> Dict[Any, Any]:
        """
        This method makes a GET request to the API
        """
        raise NotImplementedError

    # @abstractmethod
    # def generate_final_url(self, params: Dict[str, str]) -> None:
    #     """
    #     This method generates a final url given query parameters.
    #     Query parameters will be passed has to be passed in from service layer
    #     """
    #     raise NotImplementedError
