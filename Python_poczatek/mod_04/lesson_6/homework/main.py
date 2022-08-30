import random


def add_random_number_to_set(numbers):
    number = random.randint(0, 10)
    numbers.add(number)
    return numbers


def add_random_number_to_frozenset(numbers):
    number = random.randint(0, 10)
    return numbers.union({number})


def run_example():
    #numbers = set()
    numbers = frozenset()

    while len(numbers) < 11:
        print(numbers)
        #add_random_number_to_set(numbers)

        numbers = add_random_number_to_frozenset(numbers)


def run_example_remember_results():
    #numbers = frozenset()
    numbers = set()
    results = []

    while len(numbers) < 11:
        results.append(numbers)
        #numbers = add_random_number_to_frozenset(numbers)
        numbers = add_random_number_to_set(numbers)

    print(results)


if __name__ == "__main__":
    run_example_remember_results()