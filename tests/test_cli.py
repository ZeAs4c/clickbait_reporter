"""Тесты для CLI парсера."""
import pytest

from cli import parse_args


def test_parse_args_valid():
    """Тест корректных аргументов."""
    args = parse_args([
        "--files", "file1.csv",
        "file2.csv", "--report", "clickbait"
    ])

    assert args.files == ["file1.csv", "file2.csv"]
    assert args.report == "clickbait"


def test_parse_args_single_file():
    """Тест с одним файлом."""
    args = parse_args(["--files", "stats.csv", "--report", "clickbait"])
    assert args.files == ["stats.csv"]


def test_parse_args_missing_files():
    """Тест ошибки при отсутствии --files."""
    with pytest.raises(SystemExit):
        parse_args(["--report", "clickbait"])


def test_parse_args_missing_report():
    """Тест ошибки при отсутствии --report."""
    with pytest.raises(SystemExit):
        parse_args(["--files", "stats.csv"])
