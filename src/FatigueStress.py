from abc import ABC, abstractmethod

class FatigueStress(ABC):
    @abstractmethod
    def __init__(self, alternating_stress:list[float], mean_stress:list[float]):
        self.mean_stress = mean_stress
        self.alternating_stress = alternating_stress
    @abstractmethod
    def calculate(self)->list[float]:
        pass