import math
import random

value1 = random.randrange(1, 100)
value2 = random.randrange(1, 100)

print(f"{value1} * {value2} = {value1*value2}")
value1 = random.uniform(1.0, 100.0)
value2 = random.uniform(1.0, 100.0)
result = value1+value2

print(f"{value1} + {value2} = {result} (rounded: {math.ceil(result)})")
#print(f"{value1:.2f} + {value2:.2f} = {result:.2f} (rounded: {math.ceil(result)})")