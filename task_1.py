from abc import ABC, abstractmethod
from typing import List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


class Vehicle(ABC):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> "Car":
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> "Motorcycle":
        pass


class Car(Vehicle):
    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Мотор заведено")


class USVehicleFactory(VehicleFactory):
    spec = "(US Spec)"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, f"{model} {self.spec}")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, f"{model} {self.spec}")


class EUVehicleFactory(VehicleFactory):
    spec = "(EU Spec)"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, f"{model} {self.spec}")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, f"{model} {self.spec}")


def run_vehicle(vehicles: List[Vehicle]):
    for vehicle in vehicles:
        vehicle.start_engine()


if __name__ == "__main__":
    # Використання
    us_vehicle_factory = USVehicleFactory()
    vehicle1 = us_vehicle_factory.create_car("Toyota", "Corolla")
    vehicle2 = us_vehicle_factory.create_motorcycle("Harley-Davidson", "Sportster")

    eu_vehicle_factory = EUVehicleFactory()
    vehicle3 = eu_vehicle_factory.create_car("Toyota", "Corolla")
    vehicle4 = eu_vehicle_factory.create_motorcycle("Harley-Davidson", "Sportster")

    run_vehicle([vehicle1, vehicle2, vehicle3, vehicle4])
