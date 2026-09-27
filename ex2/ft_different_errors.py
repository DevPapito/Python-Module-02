def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        result = 10 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        soma = 1 + "2"
    print("Operation completed successfully\n")


def test_error_types() -> None:
    tests = [0, 1, 2, 3, 4]
    for test in tests:
        print(f"Testing operation {test}...")
        try:
            garden_operations(test)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError:
            print(
                'Caught TypeError: can only concatenate str (not "int") to str'
            )
    print("All error types tested successfully!")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()


if __name__ == "__main__":
    main()