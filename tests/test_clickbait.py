"""Тесты для отчёта clickbait."""
import pytest

from reporters.clickbait import ClickbaitReporter
from models import Video


@pytest.fixture
def reporter():
    """Фикстура: экземпляр репортера."""
    return ClickbaitReporter()


def test_clickbait_name(reporter):
    """Тест имени отчёта."""
    assert reporter.name == "clickbait"


def test_clickbait_filtering(reporter):
    """Тест фильтрации: только ctr>15 и retention<40."""
    videos = [
        Video("Video1", 20.0, 30.0),   # ✅ подходит
        Video("Video2", 10.0, 30.0),   # ❌ ctr низкий
        Video("Video3", 20.0, 50.0),   # ❌ retention высокий
        Video("Video4", 30.0, 35.0),   # ✅ подходит
        Video("Video5", 15.0, 39.0),   # ❌ ctr = 15 (не >)
        Video("Video6", 16.0, 40.0),   # ❌ retention = 40 (не <)
    ]

    result = reporter.generate(videos)

    assert len(result) == 2
    assert result[0]["title"] == "Video4"  # 30 > 20, должна быть первой
    assert result[1]["title"] == "Video1"


def test_clickbait_sorting(reporter):
    """Тест сортировки по убыванию CTR."""
    videos = [
        Video("Low", 18.0, 35.0),
        Video("High", 30.0, 38.0),
        Video("Medium", 25.0, 32.0),
    ]

    result = reporter.generate(videos)

    assert result[0]["ctr"] == 30.0  # High
    assert result[1]["ctr"] == 25.0  # Medium
    assert result[2]["ctr"] == 18.0  # Low


def test_clickbait_empty(reporter):
    """Тест когда нет подходящих видео."""
    videos = [
        Video("Bad1", 10.0, 30.0),
        Video("Bad2", 20.0, 50.0),
    ]

    result = reporter.generate(videos)
    assert result == []


def test_clickbait_data_format(reporter):
    """Тест формата выходных данных."""
    videos = [Video("Test", 22.5, 28.0)]
    result = reporter.generate(videos)

    assert len(result) == 1

    item = result[0]

    assert "title" in item
    assert "ctr" in item
    assert "retention_rate" in item
    assert item["title"] == "Test"
    assert item["ctr"] == 22.5
    assert item["retention_rate"] == 28.0
