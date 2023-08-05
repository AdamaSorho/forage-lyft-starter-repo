from tire.tire import Tire

class OctoprimeTire(Tire):
    
    def __init__(self, sensors: list) -> None:
        super().__init__()
        self.sensors = sensors

    def needs_service(self) -> bool:
        return sum(self.sensors) >= 3
            