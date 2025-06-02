# Генератор отчетов по зарплатам

Инструмент командной строки для генерации отчетов по зарплатам сотрудников из CSV файлов. Проверить работу можно в test.jpg

## Возможности

- Чтение данных сотрудников из нескольких CSV файлов
- Поддержка различных названий колонок для почасовой ставки (hourly_rate, rate, salary)
- Генерация отчетов по выплатам с группировкой по отделам
- Расширяемая архитектура для добавления новых типов отчетов

## Использование

```bash
python3 main.py data1.csv data2.csv data3.csv --report payout
```

### Формат CSV файла

Входные CSV файлы должны содержать следующие колонки:
- id
- email
- name
- department
- hours_worked
- hourly_rate (или rate, или salary)

Пример:
```csv
id,email,name,department,hours_worked,hourly_rate
1,alice@example.com,Alice Johnson,Marketing,160,50
2,bob@example.com,Bob Smith,Design,150,40
```

## Разработка

### Запуск тестов

```bash
pytest tests/
```

### Структура проекта

```
├── __init__.py
├── cli.py            # Интерфейс командной строки
├── csv_parser.py     # Парсер CSV файлов
├── models.py        # Модели данных
├── reports/         # Реализация отчетов
│   ├── __init__.py
│   ├── base.py      # Базовый класс отчета
│   └── payout.py    # Реализация отчета по выплатам
└── tests/          # Тесты
    ├── __init__.py
    ├── test_parser.py
    └── test_reports.py
``` 