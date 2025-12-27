class Plant():
    """
    Plantクラス
    name, agem water_levelを持つ
    """
    def __init__(self, name, age, water_level):
        self.name = name
        self.age = age
        self.water_level = water_level


class GardenError(Exception):
    """
    Exceptionを継承することでエラーとして機能させる
    """
    pass


class PlantError(GardenError):
    """
    GardenErrorを継承する
    個別のエラーメッセージを保持する
    """
    def __init__(self):
        super().__init__("The tomato plant is wilting!")


class WaterError(GardenError):
    """
    GardenErrorを継承する
    個別のエラーメッセージを保持する
    """
    def __init__(self):
        super().__init__("Not enough water in the tank!")


def test_error_types():
    """
    実際にエラーを引き起こす
    PlantError → ageが30より大きい場合
    WaterError → water_levelが20未満
    """
    print("=== Custom Garden Errors Demo ===")
    print()

# === PlantError ===

    tomato = Plant("Tomato", 40, 100)
    try:
        print("Testing PlantError...")
        if tomato.age > 30:
            raise PlantError
    except PlantError as e:
        print("Caught PlantError:", e)

# === WaterError ===

    tomato = Plant("Tomato", 20, 10)
    try:
        print("Testing WaterError...")
        if tomato.water_level < 20:
            raise WaterError
    except WaterError as e:
        print("Caught WaterError:", e)

# === All Errors ===

    print("Testing catching all garden errors...")
    tomato = Plant("Tomato", 40, 10)
    try:
        if tomato.age > 30:
            raise PlantError()
        if tomato.water_level < 20:
            raise WaterError()
    except GardenError as e:
        print("Caught a garden error:", e)

    print()
    print("All custom error types work correctly!")


def main():
    """コードの入口"""
    test_error_types()


if __name__ == "__main__":
    main()
