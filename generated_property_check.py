import random

def check_property(repetitions) -> bool:
    correct_count = 0
    for _ in range(repetitions):
        x = random.random()
        y = random.random()
        z = random.random()

        # Check if the associative property holds
        result1 = (x+y) + z
        result2 = x+ (y+z)
        if result1 == result2:
            correct_count += 1
        
    print(f"Out of {repetitions} trials, the property held {correct_count} times.")

# Define the number of repetitions
repetitions = 1000

#Call the function
check_property(repetitions)