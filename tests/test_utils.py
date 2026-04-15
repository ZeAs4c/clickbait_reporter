"""Тесты для утилит."""
import pytest
import tempfile
import csv

from pathlib import Path
from utils import read_csv_files


def test_read_csv_files_single():
    """Тест чтения одного CSV файла."""
    # Создаём временный CSV файл
    with tempfile.NamedTemporaryFile(
        mode='w',
        suffix='.csv',
        delete=False,
        encoding='utf-8'
    ) as f:
        writer = csv.DictWriter(
            f,
            fieldnames=['title', 'ctr', 'retention_rate', 'views']
        )

        writer.writeheader()

        writer.writerow({
            'title': 'Test Video',
            'ctr': '25.5',
            'retention_rate': '30',
            'views': '1000'
        })

        temp_path = f.name

    try:
        videos = read_csv_files([temp_path])
        assert len(videos) == 1
        assert videos[0].title == 'Test Video'
        assert videos[0].ctr == 25.5
        assert videos[0].retention_rate == 30.0
    finally:
        Path(temp_path).unlink()


def test_read_csv_files_multiple():
    """Тест чтения нескольких CSV файлов."""
    paths = []

    try:
        for i in range(2):
            with tempfile.NamedTemporaryFile(
                mode='w', suffix='.csv', delete=False, encoding='utf-8'
            ) as f:
                writer = csv.DictWriter(
                    f, fieldnames=['title', 'ctr', 'retention_rate']
                )

                writer.writeheader()

                writer.writerow({
                    'title': f'Video{i}',
                    'ctr': '10',
                    'retention_rate': '50'
                })

                paths.append(f.name)

        videos = read_csv_files(paths)

        assert len(videos) == 2
    finally:
        for path in paths:
            Path(path).unlink()


def test_read_csv_files_not_exists():
    """Тест ошибки при несуществующем файле."""
    with pytest.raises(FileNotFoundError):
        read_csv_files(['nonexistent.csv'])


def test_read_csv_files_missing_columns():
    """Тест ошибки при отсутствии нужных колонок."""
    with tempfile.NamedTemporaryFile(
        mode='w', suffix='.csv', delete=False, encoding='utf-8'
    ) as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'views'])
        writer.writeheader()
        writer.writerow({'title': 'Test', 'views': '100'})
        temp_path = f.name
    try:
        with pytest.raises(ValueError):
            read_csv_files([temp_path])
    finally:
        Path(temp_path).unlink()
