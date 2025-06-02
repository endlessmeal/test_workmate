from dataclasses import dataclass


@dataclass
class Employee:
    """Класс, представляющий сотрудника."""
    id: int
    email: str
    name: str
    department: str
    hours_worked: float
    hourly_rate: float

    @property
    def payout(self) -> float:
        """Рассчитывает общую сумму выплаты сотруднику."""
        return self.hours_worked * self.hourly_rate


@dataclass
class Department:
    """Класс, представляющий отдел компании."""
    name: str
    employees: list[Employee]

    @property
    def total_payout(self) -> float:
        """Рассчитывает общую сумму выплат по отделу."""
        return sum(employee.payout for employee in self.employees)

    @property
    def average_hourly_rate(self) -> float:
        """Рассчитывает среднюю почасовую ставку по отделу."""
        if not self.employees:
            return 0.0
        return sum(employee.hourly_rate for employee in self.employees) / len(self.employees)
