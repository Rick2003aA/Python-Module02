class Plant:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class WaterLevel:
    def __init__(self, water_level):
        self.water_level = water_level


class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __str__(self):
        return("Test Error")
    pass


class WaterError(GardenError):
    pass


def garden_operations(plant, water):
    if plant.age > 20:
        raise PlantError(f"The {plant.name} is wilting!")
    if water.water_level < 20:
        raise WaterError("Not enough water in the tank!")


def test_error_types():
    print("Testing PlantError...")
    try:
        plant = Plant("Tomato", 30)
        water = WaterLevel(100)
        garden_operations(plant, water)
    except PlantError as e:
        print("Caught PlantError:", e)

    print("Testing WaterError...")
    try:
        plant = Plant("Tomato", 5)
        water = WaterLevel(5)
        garden_operations(plant, water)
    except WaterError as e:
        print("Caught WaterError:", e)

    print("Testing catching all garden errors...")
    try:
        plant = Plant("Tomato", 30)
        water = WaterLevel(100)
        garden_operations(plant, water)
    except GardenError as e:
        print("Caught a garden error:", e)

    try:
        plant = Plant("Tomato", 5)
        water = WaterLevel(5)
        garden_operations(plant, water)
    except GardenError as e:
        print("Caught a garden error:", e)

    print("All custom error types work correctly!")


print("=== Custom Garden Errors Demo ===")
test_error_types()
