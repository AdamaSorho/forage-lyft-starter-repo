from tire.tire import Tire

class CarriganTire(Tire):
    
    def __init__(self, sensors: list) -> None:
        super().__init__()
        self.sensors = sensors

    def needs_service(self) -> bool:
        be_serviced = False
        for n in self.sensors:
            if n >= 0.9:
                be_serviced = True
                break
            
        return be_serviced