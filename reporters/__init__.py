"""Регистрация всех доступных отчётов."""
from typing import Dict, Type
from reporters.base import BaseReporter

from reporters.clickbait import ClickbaitReporter


# Словарь доступных отчётов: имя -> класс
REPORTERS: Dict[str, Type[BaseReporter]] = {
    ClickbaitReporter.name: ClickbaitReporter,
}


def get_reporter(report_name: str):
    """Возвращает экземпляр репортера по имени."""
    reporter_class = REPORTERS.get(report_name)

    if not reporter_class:
        raise ValueError(
            f"Неизвестный отчёт: {report_name}. "
            f"Доступны: {list(REPORTERS.keys())}"
        )

    return reporter_class()
