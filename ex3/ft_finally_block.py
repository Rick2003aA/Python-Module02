class WateringError(Exception):
    pass


def water_plants(plant_list):
    plants_in_garden = ["tomato", "lettuce", "carrots"]
    print("Opening watering system")
    try:
        for p in plant_list:
            if p not in plants_in_garden:
                print(f"Error: Cannot water {p} - invalid plant !")
                return
            else:
                print(f"Watering {p}")
        return True
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("Testing normal watering ...")
    good_list = ["tomato", "lettuce", "carrots"]
    try:
        success = water_plants(good_list)
    except:# 修正必要
        print("Cleanup always happens, even with errors!")
    finally:
        if success:
            print("Watering completed successfully!")
    print("Testing with error ...")
    bad_list = ["tomato", "banana", "carrots"]
    try:
        success = water_plants(bad_list)
    except Exception:
        ("Cleanup always happens, even with errors!")
        success = False
    finally:
        if not success:
            print("Cleanup always happens, even with errors!")


print("=== Garden Watering System ===")
test_watering_system()
