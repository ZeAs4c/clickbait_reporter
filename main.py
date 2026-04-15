"""Основной модуль CLI приложения."""
import sys

from cli import parse_args
from reporters import get_reporter
from utils import read_csv_files
from tabulate import tabulate


def main():
    """Основной pipeline:
    CLI → чтение данных → выбор отчёта → генерация → вывод"""
    try:

        args = parse_args()
        videos = read_csv_files(args.files)

        if not videos:
            print("Предупреждение: не найдено валидных видео в файлах")
            return

        reporter = get_reporter(args.report)
        report_data = reporter.generate(videos)

        if report_data:
            table = tabulate(
                report_data,
                headers={
                    "title": "title",
                    "ctr": "ctr",
                    "retention_rate": "retention_rate"
                },
                tablefmt="grid",
                floatfmt=".1f"  # один знак после запятой
            )
            print(table)
        else:
            print("Нет видео, соответствующих условиям отчёта")

    except (FileNotFoundError, ValueError) as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

    except Exception as e:
        print(f"Неожиданная ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
