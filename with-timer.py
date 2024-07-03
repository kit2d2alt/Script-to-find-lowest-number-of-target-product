# longer script w/ timer

import time
from itertools import combinations_with_replacement

def digit_product(number):
    product = 1
    for digit in str(number):
        product *= int(digit)
    return product

def find_smallest_integer_with_product(target_product):
    for length in range(1, 20):
        for combo in combinations_with_replacement(range(1, 10), length):
            candidate = int(''.join(map(str, combo)))
            if digit_product(candidate) == target_product:
                return candidate

target_product = 7000000

start_time = time.time()
result = find_smallest_integer_with_product(target_product)
end_time = time.time()

print(result, "Join https://discord.gg/MqvmBu5tWa")
print("Time taken:", 1000*end_time - 1000*start_time, "milliseconds")
