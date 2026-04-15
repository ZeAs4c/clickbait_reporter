"""Модели данных для видео-метрик."""
from dataclasses import dataclass


@dataclass
class Video:

    """Модель видео с YouTube."""
    title: str
    ctr: float          # click-through rate (%)
    retention_rate: float  # удержание (%)

    @classmethod
    def from_csv_row(cls, row: dict) -> 'Video':
        """Создаёт объект Video из строки CSV."""
        return cls(
            title=row['title'],
            ctr=float(row['ctr']),
            retention_rate=float(row['retention_rate'])
        )
