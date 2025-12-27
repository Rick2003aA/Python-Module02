def garden_operations(mode):
    """
    mode -> str
    modeに入ってきた引数によって対応するエラーを引き起こす
    """
    if mode == "value":
        int("abc")
    elif mode == "zero":
        1 / 0
    elif mode == "file":
        open("missing.txt")
    elif mode == "key":
        d = {"a": "b"}
        d["c"]
    else:
        int("abc")
        1 / 0


def test_error_types():
    """
    tryでgarden_operationsに引き起こすべきエラーの種類を渡す
    garden_operationsで起こしたエラーをexceptで拾う
    拾ったエラーに応じて表示するメッセージを変える
    """
    error_list = ["value", "zero", "file", "key"]
    for mode in error_list:
        try:
            garden_operations(mode)
        except ValueError:
            print("Testing ValueError")
            print("Caught ValueError: invalid literal for int()")
        except ZeroDivisionError:
            print("Testing ZeroDivisionError")
            print("Caught ZeroDivisionError: division by zero")
        except FileNotFoundError:
            print("Testing FileNotFoundError")
            print(f"Caught FileNotFoundError: No such file {mode}")
        except KeyError:
            print("Testing KeyError")
            print(f"Caught KeyError: {mode}")
    print("Testing multiple errors together...")
    try:
        garden_operations("value")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("All error types tested successfully!")


def main():
    print("=== Garden Error Types Demo ===")
    test_error_types()


if __name__ == "__main__":
    main()
