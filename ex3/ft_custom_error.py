class GardenError(Exception):
	def __init__(self, message = "Unknown garden error"):
		super().__init__(message)

class PlantError(GardenError):
	def __init__(self, message = "Unknown plant error"):
		super().__init__(message)

class WaterError(GardenError):
	def __init__(self, message = "Unknown water error"):
		super().__init__(message)

def main():
	print("=== Custom Garden Errors Demo ===\n")
	tests = [0, 1, 2, 2]
	i = 0
	message = False
	for test in tests:
		try:
			if (test == 0):
				print(f"Testing PlantError...")
				raise PlantError("The tomato plant is wilting!\n")
			elif (test == 1):
				print(f"Testing WaterError...")
				message = True
				raise WaterError("Not enough water is the tank!\n")
			elif (test == 2):
				if (message):
					message = False
					print("Testing catching all garden errors...")
				if (i == 2):
					raise GardenError("The tomato plant is wilting!")
				elif (i == 3):
					raise GardenError("Not enough water in the tank!")
		except PlantError as e:
			print(f"Caught PlantError: {e}")
		except WaterError as e:
			print(f"Caught WaterError: {e}")
		except GardenError as e:
			print(f"Caught GardenError: {e}")
		i += 1
	print("\nAll custom error types work correctly!")

if __name__ == '__main__':
	main()
