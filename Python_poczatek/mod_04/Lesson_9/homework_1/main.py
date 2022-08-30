from shop.apple import Apple
from shop.potato import Potato


def run_homework():
    green_apple = Apple(species_name="Green", size="M", price=3.5)
    red_apple = Apple(species_name="Red", size="S", price=2.5)
    print(green_apple.species_name, green_apple.size, green_apple.price)
    print(red_apple.species_name, red_apple.size, red_apple.species_name)

    old_potato = Potato(species_name="Green", size="M", price=3.5)
    print(old_potato.species_name, old_potato.price, old_potato.size)


if __name__ == "__main__":
    run_homework()
