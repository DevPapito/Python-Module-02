class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if "A" <= plant_name[0] <= "Z":
        print(f"Watering {plant_name}: [0K]")
        return
    raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    plants = ["Tomato", "Lettuce", "Carrots", "Tomato", "lettuce"]
    print("Testing valid plants...")
    print("Opening watering system")
    for i in [0, 1, 2]:
        try:
            water_plant(plants[i])
        except PlantError as e:
            print(
                f"Cought PlantError: {e}\n"
                ".. ending tests and returning to main"
            )
        finally:
            pass
    print("Closing watering system\n")
    print("Testing invalid plants...")
    print("Opening watering system")
    for i in [3, 4]:
        try:
            water_plant(plants[i])
        except PlantError as e:
            print(
                f"Cought PlantError: {e}\n"
                ".. ending tests and returning to main"
            )
        finally:
            pass
    print("Closing watering system\n")
    print("Cleanup always happens, even with errors!")


def main() -> None:
    print("=== Garden Watering Systems ===\n")
    test_watering_system()


if __name__ == "__main__":
    main()