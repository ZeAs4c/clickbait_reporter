"""Основной модуль CLI приложения."""
import sys

from cli import parse_args
from reporters import get_reporter
from utils import read_csv_files


def main():
    """Главная функция приложения."""
    try:

        # 1. Парсим аргументы
        args = parse_args()

        # 2. Читаем все CSV файлы
        videos = read_csv_files(args.files)

        if not videos:
            print("Предупреждение: не найдено валидных видео в файлах")
            return

        # 3. Получаем нужный репортер
        reporter = get_reporter(args.report)

        # 4. Генерируем отчёт
        report_data = reporter.generate(videos)

        # 5. Выводим таблицу
        if report_data:
            from tabulate import tabulate
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
