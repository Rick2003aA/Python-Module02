class GardenError(Exception):
    """
    Exceptionを継承し、エラーとして機能させる
    """
    pass


class PlantError(GardenError):
    """
    GardenErrorを継承
    """
    pass


class WaterError(GardenError):
    """
    GardenErrorを継承
    """
    pass


class SunLightError(GardenError):
    """
    GardenErrorを継承
    """
    pass


class GardenManager:
    """
    エラーケース：
    - nameが""の時
    - water_levelが1未満、10より大きい時
    - sunlight_hoursが2未満、12より大きい時
    """
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
        if self.plants[name]['water'] < 1:
            raise WaterError(f"Error: Water level {self.plants[name]['water']}"
                             f"is too low (min 1)")
        if self.plants[name]['water'] > 10:
            raise WaterError(f"Error: Water level {self.plants[name]['water']}"
                             f" is too high (max 10)")
        if self.plants[name]['sunlight'] < 2:
            raise SunLightError(f"Error: Sunlight hours"
                                f" {self.plants[name]['sunlight']}"
                                f" is too low (min 2)")
        if self.plants[name]['sunlight'] > 12:
            raise SunLightError(f"Error: Sunlight hours"
                                f" {self.plants[name]['sunlight']}"
                                f" is too high (max 12)")
        return (f"{name}: healthy (water: {self.plants[name]['water']}, "
                f"sun: {self.plants[name]['sunlight']})")


def main():
    print("=== Garden Management System ===")
    print()
    garden = GardenManager()
    print("Adding plants to garden...")
    try:
        garden.add_plants("Tomato", 5, 8)
    except GardenError as e:
        print(e)

    try:
        garden.add_plants("lettuce", 1, 1)
    except GardenError as e:
        print(e)

    # === Error case ===
    try:
        garden.add_plants("", 1, 1)
    except GardenError as e:
        print(e)

    print()

    print("Watering plants...")
    garden.water_plants()
    print()

    try:
        result = garden.check_plant_health("Tomato")
        print(result)
    except GardenError as e:
        print("Caught GardenError:", e)
        print("System recovered and continuing...")
    try:
        result = garden.check_plant_health("lettuce")
        print(result)
    except GardenError as e:
        print("Caught GardenError:", e)
        print("System recovered and continuing...")
    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    main()
