from abc import ABC, abstractmethod
from models import Employee


class Report(ABC):
    """Базовый класс для всех отчетов."""
    
    def __init__(self, employees: list[Employee]) -> None:
        self.employees = employees
    
    @abstractmethod
    def generate(self) -> str:
        """Сгенерировать содержимое отчета."""
        pass
