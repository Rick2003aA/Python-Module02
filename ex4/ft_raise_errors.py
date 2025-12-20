def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Error: Water level {water_level}"
                         f" is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                         f" is too low (min 2)")


def test_plant_checks():
    print("Testing good values ...")
    plant = "Tomato"
    try:
        check_plant_health(plant, 5, 10)
        print(f"Plant {plant} is healthy!")
    except ValueError as e:
        print(e)
    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 10)
    except ValueError as e:
        print(e)
    print("Testing bad water level ...")
    try:
        check_plant_health("Tomato", 15, 10)
    except ValueError as e:
        print(e)
    print("Testing bad sunlight hours ...")
    try:
        check_plant_health("Tomato", 5, 0)
    except ValueError as e:
        print(e)
    print("All error rising tests completed!")


print("=== Garden Plant Health Checker ===")
test_plant_checks()
