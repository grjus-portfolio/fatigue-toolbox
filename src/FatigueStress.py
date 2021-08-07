from abc import ABC, abstractmethod

class FatigueStress(ABC):
    @abstractmethod
    def __init__(self, alternating_stress:list[float], mean_stress:list[float]):
        self.mean_stress = mean_stress
        self.alternating_stress = alternating_stress
    @abstractmethod
    def calculate(self)->list[float]:
        pass

class GerberStress(FatigueStress):
    def __init__(self, alternating_stress: list[float], mean_stress: list[float], ultimate_strength:float):
        super().__init__(alternating_stress, mean_stress)
        self.ultimate_strength = ultimate_strength

    def calculate(self) -> list[float]:
        result = map(lambda alt, mean:alt/(1-mean/self.ultimate_strength), self.alternating_stress, self.mean_stress)
        return list(result)


class GoodmanStress(FatigueStress):
        def __init__(self, alternating_stress: list[float], mean_stress: list[float], ultimate_strength:float):
            super().__init__(alternating_stress, mean_stress)
            self.ultimate_strength = ultimate_strength
        def calculate(self) -> list[float]:
            result = map(lambda alt, mean:alt/(1-mean/self.ultimate_strength)**2, self.alternating_stress, self.mean_stress)
            return list(result)