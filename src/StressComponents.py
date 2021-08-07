from typing import Union
class StressComponents:
    def __init__(self, min_stress:list[float], max_stress:list[float]) -> None:
        self.min_stress = min_stress
        self.max_stress = max_stress

    def alternating_stress(self)->list[float]:
        result = map(lambda min_stress, max_stress:(max_stress-min_stress)*0.5, self.min_stress, self.max_stress )
        return list(result)

    def mean_stress(self)->list[float]:
        result = map(lambda min_stress, max_stress:(max_stress+min_stress)*0.5, self.min_stress, self.max_stress )
        return list(result)