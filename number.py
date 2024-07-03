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
target_product = 2160
print(find_smallest_integer_with_product(target_product),"Join https://discord.gg/MqvmBu5tWa")
