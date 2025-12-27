def check_temperature(temp_str):
    """
    temp_str -> str
    temp_strをint型に変換する
    変換できない場合、exceptに入る
    変換後、値が0未満 or 40より大きい場合はエラーメッセージを表示
    """
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
        if temp < 0:
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp_str}°C is perfect for plants!")
            return temp
    except: # noqa
        print(f"Error: {temp_str} is not a valid number")


def main():
    print("=== Garden Temperature Checker ===")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
