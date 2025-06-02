import io
import pytest
from csv_parser import parse_csv_file, find_rate_column


def test_find_rate_column():
    """Проверяет корректность определения названия колонки с почасовой ставкой в заголовке CSV."""
    assert find_rate_column(['id', 'hourly_rate', 'name']) == 'hourly_rate'
    assert find_rate_column(['id', 'rate', 'name']) == 'rate'
    assert find_rate_column(['id', 'salary', 'name']) == 'salary'
    
    with pytest.raises(ValueError):
        find_rate_column(['id', 'name'])


def test_parse_csv_file():
    """Проверяет корректность парсинга CSV файла с данными сотрудников."""
    csv_content = """id,email,name,department,hours_worked,hourly_rate
1,alice@example.com,Alice Johnson,Marketing,160,50
2,bob@example.com,Bob Smith,Design,150,40"""
    
    file = io.StringIO(csv_content)
    employees = parse_csv_file(file)
    
    assert len(employees) == 2
    assert employees[0].name == "Alice Johnson"
    assert employees[0].department == "Marketing"
    assert employees[0].hours_worked == 160
    assert employees[0].hourly_rate == 50
    assert employees[0].payout == 8000
    
    assert employees[1].name == "Bob Smith"
    assert employees[1].department == "Design"
    assert employees[1].hours_worked == 150
    assert employees[1].hourly_rate == 40
    assert employees[1].payout == 6000


def test_parse_csv_file_with_different_rate_column():
    """Проверяет корректность парсинга CSV файла с альтернативным названием колонки ставки."""
    csv_content = """id,email,name,department,hours_worked,rate
1,alice@example.com,Alice Johnson,Marketing,160,50"""
    
    file = io.StringIO(csv_content)
    employees = parse_csv_file(file)
    
    assert len(employees) == 1
    assert employees[0].hourly_rate == 50
    assert employees[0].payout == 8000 