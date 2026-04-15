# Clickbait Reporter

CLI утилита для анализа YouTube видео и выявления кликбейтного контента.

## Запуск

```bash
python main.py --files stats1.csv stats2.csv --report clickbait
```

<img width="1452" height="347" alt="image" src="https://github.com/user-attachments/assets/f8baeab7-af8d-422f-9e71-1046c2243bb2" />


## Архитектура

Проект построен с возможностью расширения через добавление новых отчётов.

Каждый отчёт реализуется в виде отдельного класса в папке `reporters`
и наследуется от `BaseReporter`.

Для добавления нового отчёта достаточно:
1. Создать новый класс в `reporters/`
2. Добавить его в `REPORTERS` в `reporters/__init__.py`