"""Отчёт для кликбейтных видео."""
from typing import List, Dict, Any

from models import Video


class ClickbaitReporter:

    """
    Формирует отчёт о кликбейтных видео.
    Условия: ctr > 15 И retention_rate < 40
    Сортировка: по убыванию CTR
    """
    @property
    def name(self) -> str:
        """Название отчёта (совпадает с параметром --report)."""
        return "clickbait"

    def generate(self, videos: List[Video]) -> List[Dict[str, Any]]:
        """
        Генерирует отчёт из списка видео.
        Args:
            videos: Список всех видео
        Returns:
            Список словарей с полями title, ctr, retention_rate
        """
        # Фильтрация
        filtered = [
            video for video in videos
            if video.ctr > 15 and video.retention_rate < 40
        ]

        # Сортировка по убыванию CTR
        filtered.sort(key=lambda v: v.ctr, reverse=True)

        # Преобразование в формат для таблицы
        return [
            {
                "title": v.title,
                "ctr": v.ctr,
                "retention_rate": v.retention_rate
            }
            for v in filtered
        ]
