def input_temperature(temp_str):
	print(f"Input data is \'{temp_str}\'")
	return int(temp_str)

def test_temperature():
	try:
		number = input_temperature("25")
		print(f"Temperature is now: {number}°C\n")
		number = input_temperature("abc")
		print(f"Temperature is now: {number}°C\n")
	except ValueError as e:
		print(f"Caught input_temperature error: {e}\n")
	print("All tests completed - program didn't crash!")

def main():
	print("=== Garden Temperature ===\n")
	test_temperature()

if __name__ == '__main__':
	main()
