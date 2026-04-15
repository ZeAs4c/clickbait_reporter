"""Утилиты для чтения файлов."""
import csv
import logging

from pathlib import Path
from typing import List

from models import Video


def read_csv_files(file_paths: List[str]) -> List[Video]:
    """
    Читает один или несколько CSV-файлов и возвращает список Video.
    Args:
        file_paths: Список путей к CSV-файлам
    Returns:
        Список объектов Video из всех файлов
    """
    videos = []
    for file_path in file_paths:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Файл не найден: {file_path}")
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            # Проверяем наличие обязательных колонок для расчёта отчётов
            required_columns = {'title', 'ctr', 'retention_rate'}
            if not required_columns.issubset(reader.fieldnames):
                raise ValueError(
                    f"Файл {file_path} не содержит нужные колонки: "
                    f"{required_columns}"
                )
            for row in reader:
                try:
                    video = Video.from_csv_row(row)
                    videos.append(video)
                except (ValueError, KeyError) as e:
                    # Пропускаем строки с некорректными данными
                    # (например, невалидные числа)
                    msg = f"Ошибка в строке {file_path}: {e}"
                    logging.warning(msg)
                    continue
    return videos
