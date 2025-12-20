def check_temperature(temp_str):
    print(f"Testing temperature: {temp_str}")
    try:
        int(temp_str)
    except Exception:
        print(f"Error: {temp_str} is not a valid number")
        return
    if int(temp_str) < 0:
        print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
    elif int(temp_str) > 40:
        print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
    else:
        print(f"Temperature {temp_str}°C is perfect for plants!")


print("=== Garden Temperature Checker ===")
check_temperature("25")
check_temperature("abc")
check_temperature("100")
check_temperature("-50")
print("All tests completed - program didn't crash!")
