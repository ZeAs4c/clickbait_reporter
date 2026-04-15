"""Отчёт для кликбейтных видео."""
from typing import List, Dict, Any
from models import Video
from reporters.base import BaseReporter


class ClickbaitReporter(BaseReporter):

    """
    Формирует отчёт о кликбейтных видео.
    Условия: ctr > 15 И retention_rate < 40
    Сортировка: по убыванию CTR
    """
    name = "clickbait"

    def generate(self, videos: List[Video]) -> List[Dict[str, Any]]:
        """
        Генерирует отчёт из списка видео.
        Args:
            videos: Список всех видео
        Returns:
            Список словарей с полями title, ctr, retention_rate
        """
        # Условие кликбейта: высокий CTR и низкое удержание
        filtered = [
            video for video in videos
            if video.ctr > 15 and video.retention_rate < 40
        ]

        # Сортируем, чтобы самые кликбейтные (с высоким CTR) были сверху
        filtered.sort(key=lambda v: v.ctr, reverse=True)

        # Приводим к формату, подходящему для tabulate (список словарей)
        return [
            {
                "title": v.title,
                "ctr": v.ctr,
                "retention_rate": v.retention_rate
            }
            for v in filtered
        ]
