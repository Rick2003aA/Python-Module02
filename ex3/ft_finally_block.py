def water_plants(plant_list):
    """
    listの中身がNoneの場合にexceptに入り、エラーメッセージを表示
    finallyでexceptに入ったとしてもcloseする
    """
    print("Opening watering system")
    try:
        for p in plant_list:
            if p is None:
                1 / 0
            print(f"Watering {p}")
        print("Watering completed successfully!")
    except:# noqa
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """
    water_plantsを良い例と悪い例で試す
    """
    print("Testing normal watering...")
    try:
        water_plants(["tomato", "lettuce", "carrots"])
        print("Watering completed successfully!")
    except:# noqa
        None
    finally:
        None

    print("Testing with error...")
    try:
        water_plants(["tomato", None, "carrots"])
    except:# noqa
        None
    finally:
        print("Cleanup always happens, even with errors!")


def main():
    print("=== Garden Watering System ===")
    test_watering_system()


if __name__ == "__main__":
    main()
