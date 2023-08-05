from service.serviceable import Serviceable
from engine.engine import Engine
from battery.battery import Battery
from tire.tire import Tire

class Car(Serviceable):
    
    def __init__(self, engine: Engine, battery: Battery, tire: Tire) -> None:
        super().__init__()
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self) -> bool:
        return (self.engine.needs_service() 
                or self.battery.needs_service() 
                or self.tire.need_service())