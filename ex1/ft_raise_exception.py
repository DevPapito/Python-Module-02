def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    ntemp_str = int(temp_str)
    if ntemp_str < 0:
        raise AttributeError
    if ntemp_str > 40:
        raise TypeError
    return int(temp_str)


def test_temperature() -> None:
    tests = ["25", "abc", "100", "-50"]
    number = 0
    for test in tests:
        try:
            number = input_temperature(test)
            print(f"Temperature is now: {number}°C\n")
        except TypeError:
            print(
                f"Caught input_temperature error: {test}°C is too hot "
                "for plants (max 40°C)\n"
            )
        except AttributeError:
            print(
                f"Caught input_temperature error: {test}°C is too cold "
                "for plants (min 0°C)\n"
            )
        except Exception:
            print(
                "Caught input_temperature error: invalid literal for int() "
                f"with base 10: '{test}'\n"
            )
    print("All tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature Checker ===\n")
    test_temperature()


if __name__ == "__main__":
    main()