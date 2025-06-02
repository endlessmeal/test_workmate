from typing import TextIO
from models import Employee

# Возможные названия колонок для почасовой ставки
RATE_COLUMNS = {'hourly_rate', 'rate', 'salary'}


def find_rate_column(header: list[str]) -> str:
    """Находит название колонки, представляющей почасовую ставку."""
    for col in RATE_COLUMNS:
        if col in header:
            return col
    raise ValueError("Колонка со ставкой не найдена в заголовке CSV")


def parse_csv_file(file: TextIO) -> list[Employee]:
    """Парсит CSV файл и возвращает список объектов Employee."""
    # Читаем заголовок
    header = next(file).strip().split(',')
    rate_col = find_rate_column(header)
    
    # Создаем отображение названий колонок на их индексы
    col_indices = {col: idx for idx, col in enumerate(header)}
    
    employees = []
    for line in file:
        values = line.strip().split(',')
        if len(values) != len(header):
            continue  # Пропускаем некорректные строки
            
        employee = Employee(
            id=int(values[col_indices['id']]),
            email=values[col_indices['email']],
            name=values[col_indices['name']],
            department=values[col_indices['department']],
            hours_worked=float(values[col_indices['hours_worked']]),
            hourly_rate=float(values[col_indices[rate_col]])
        )
        employees.append(employee)
    
    return employees


def read_employees_from_files(file_paths: list[str]) -> list[Employee]:
    """Читает данные сотрудников из нескольких CSV файлов."""
    all_employees = []
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            employees = parse_csv_file(f)
            all_employees.extend(employees)
    return all_employees 