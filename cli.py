import argparse
from csv_parser import read_employees_from_files
from reports.payout import PayoutReport


def get_report_class(report_type: str):
    """Получает соответствующий класс отчета на основе типа отчета."""
    report_classes = {
        'payout': PayoutReport,
    }
    
    if report_type not in report_classes:
        raise ValueError(f"Неизвестный тип отчета: {report_type}")
    
    return report_classes[report_type]


def main():
    parser = argparse.ArgumentParser(description='Генерация отчетов по сотрудникам из CSV файлов')
    parser.add_argument('files', nargs='+', help='CSV файлы для обработки')
    parser.add_argument('--report', required=True, help='Тип генерируемого отчета')
    
    args = parser.parse_args()
    
    # Читаем данные сотрудников из всех файлов
    employees = read_employees_from_files(args.files)
    
    # Генерируем и выводим отчет
    report_class = get_report_class(args.report)
    report = report_class(employees)
    print(report.generate())


if __name__ == '__main__':
    main() 