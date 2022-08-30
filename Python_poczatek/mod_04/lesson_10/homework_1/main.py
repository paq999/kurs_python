from shop import data_generator
from shop.order import Order


def run_homework():
    some_order_elements = data_generator.generate_order_elements()
    my_order = Order("Bob", "Kowalski", order_elements=some_order_elements)
    print(my_order)


if __name__ == "__main__":
    run_homework()
