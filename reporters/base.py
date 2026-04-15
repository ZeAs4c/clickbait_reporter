from typing import List, Dict, Any
from models import Video


class BaseReporter:
    """Базовый класс для всех отчетов."""

    name: str

    def generate(self, videos: List[Video]) -> List[Dict[str, Any]]:
        raise NotImplementedError("Метод generate должен быть реализован")
