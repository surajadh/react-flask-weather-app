from typing import Dict, Protocol


class Service(Protocol):
    def get_min_max(zip: str, days: int) -> Dict[str, str]:
        raise NotImplementedError