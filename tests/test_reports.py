from models import Employee
from reports.payout import PayoutReport


def test_payout_report():
    """Проверяет корректность генерации отчета по выплатам, включая группировку по отделам и расчет итогов."""
    employees = [
        Employee(1, "alice@example.com", "Alice Johnson", "Marketing", 160, 50),
        Employee(2, "bob@example.com", "Bob Smith", "Design", 150, 40),
        Employee(3, "carol@example.com", "Carol Williams", "Design", 170, 60),
    ]
    
    report = PayoutReport(employees)
    output = report.generate()
    
    # Проверяем группировку и сортировку по отделам
    assert "Design Department" in output
    assert "Marketing Department" in output
    
    # Проверяем корректность отображения сотрудников и расчетов
    assert "Alice Johnson" in output
    assert "Bob Smith" in output
    assert "Carol Williams" in output
    
    # Проверяем итоговые суммы
    assert "8000.00" in output  # Выплата Alice
    assert "6000.00" in output  # Выплата Bob
    assert "10200.00" in output  # Выплата Carol
    
    # Проверяем итоги по отделам
    assert "16200.00" in output  # Итого по отделу Design
    assert "8000.00" in output  # Итого по отделу Marketing 