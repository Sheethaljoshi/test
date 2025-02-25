import random

def generate_random_numbers(count, start, end):
    return [random.randint(start, end) for _ in range(count)]

if __name__ == "__main__":
    random_numbers = generate_random_numbers(10, 1, 100)
    print("Random Numbers:", random_numbers)