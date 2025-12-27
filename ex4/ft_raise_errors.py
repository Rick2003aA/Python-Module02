def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    water_levelが1未満、10より大きい時
    sunlight_hoursが2未満、12より大きい時
    上記のケースでValueErrorをraiseする
    """
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Error: Water level {water_level}"
                         f"is too low (min 1)")

    if water_level > 10:
        raise ValueError(f"Error: Water level {water_level}"
                         f" is too high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                         f" is too low (min 2)")

    if sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                         f" is too high (max 12)")

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """
    check_plant_healthでエラーを引き起こす
    エラーの場合exceptに入り、エラーメッセージを表示
    """
    print("Testing good values...")
    plant = "tomato"
    try:
        result = check_plant_health(plant, 5, 10)
        print(result)
        print()
    except ValueError as e:
        print(e)
        print()

    print("Testing empty plant name...")
    try:
        result = check_plant_health("", 5, 10)
        print(result)
        print()
    except ValueError as e:
        print(e)
        print()

    print("Testing bad water level ...")
    try:
        result = check_plant_health("Tomato", 15, 10)
        print(result)
        print()
    except ValueError as e:
        print(e)
        print()

    print("Testing bad sunlight hours ...")
    try:
        result = check_plant_health("Tomato", 5, 0)
        print(result)
        print()
    except ValueError as e:
        print(e)
        print()

    print("All error rising tests completed!")


def main():
    print("=== Garden Plant Health Checker ===")
    print()
    test_plant_checks()


if __name__ == "__main__":
    main()
