class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class SunLightError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = {}

    def add_plants(self, name, water, sunlight):
        if name == "":
            raise PlantError("Error adding plant: Plant name cannot be empty!")
        else:
            print(f"Added {name} successfully")
            self.plants[name] = {"water": water,
                                 "sunlight": sunlight}

    def water_plants(self):
        print("Opening watering system")
        try:
            for p in self.plants:
                print(f"Watering {p} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name):
        if name == "":
            raise PlantError("Error: Plant name cannot be empty!")
        if name not in self.plants:
            raise PlantError(f"Plant '{name}' does not exist!")
        if self.plants[name]['water'] > 10:
            raise WaterError(f"Error: Water level {self.plants[name]['water']}"
                             f" is too high (max 10)")
        if self.plants[name]['sunlight'] < 2:
            raise SunLightError(f"Error: Sunlight hours"
                                f" {self.plants[name]['sunlight']}"
                                f" is too low (min 2)")


print("=== Garden Management System ===")
garden = GardenManager()
try:
    garden.add_plants("Tomato", 1, 1)
    garden.add_plants("Banana", 1, 1)
except GardenError as e:
    print(e)

garden.water_plants()
try:
    garden.check_plant_health("Tomato")
except GardenError as e:
    print("Caught GardenError:", e)
    print("System recovered and continuing...")
