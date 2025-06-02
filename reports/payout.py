from collections import defaultdict
from models import Employee, Department
from .base import Report


class PayoutReport(Report):
    """Отчет, показывающий выплаты сотрудникам, сгруппированные по отделам."""
    
    def generate(self) -> str:
        """Отчет, показывающий выплаты сотрудникам, сгруппированные по отделам."""
        departments: dict[str, list[Employee]] = defaultdict(list)
        for employee in self.employees:
            departments[employee.department].append(employee)
        
        # Создаем объекты отделов
        dept_objects = [
            Department(name=dept_name, employees=employees)
            for dept_name, employees in sorted(departments.items())
        ]
        
        # Генерируем отчет
        lines = []
        lines.append(f"{'Name':<20} {'Hours':>8} {'Rate':>8} {'Payout':>10}")
        lines.append("-" * 48)
        
        for dept in dept_objects:
            lines.append(f"\n{dept.name} Department")
            lines.append("-" * 48)
            
            for employee in sorted(dept.employees, key=lambda e: e.name):
                lines.append(
                    f"{employee.name:<20} "
                    f"{employee.hours_worked:>8.1f} "
                    f"{employee.hourly_rate:>8.1f} "
                    f"{employee.payout:>10.2f}"
                )
            
            lines.append("-" * 48)
            lines.append(
                f"{'Total':<20} {'':>8} {'':>8} {dept.total_payout:>10.2f}"
            )
        
        return "\n".join(lines)
