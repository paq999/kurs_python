from collections import namedtuple

Apple = namedtuple("Apple", ["species_name", "size", "price"])


def run_homework():
    green_apple = Apple(species_name="Green", size="M", price=3.5)

    print(green_apple.species_name, green_apple.size, green_apple.price)
    print(green_apple[0], green_apple[1], green_apple[2])

    for value in green_apple:
        print(value)


if __name__ == "__main__":
    run_homework()
