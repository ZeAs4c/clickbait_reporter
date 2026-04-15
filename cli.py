"""Обработка аргументов командной строки."""
import argparse

from typing import List


def parse_args(args: List[str] = None):
    """
    Парсит аргументы командной строки.
    Args:
        args: Список аргументов (для тестов можно подставить свои)
    Returns:
        Объект с атрибутами files и report
    """
    parser = argparse.ArgumentParser(
        description="Генерация отчётов по метрикам YouTube видео"
    )

    parser.add_argument(
        "--files",
        nargs="+",  # принимает один или несколько файлов
        required=True,
        help="Пути к CSV-файлам с данными (можно указать несколько)"
    )

    parser.add_argument(
        "--report",
        type=str,
        required=True,
        help="Название отчёта (например: clickbait)"
    )

    return parser.parse_args(args)
