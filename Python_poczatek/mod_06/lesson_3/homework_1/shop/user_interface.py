from .order import Order
from .errors import TemporaryOutOfStock, NotValidInput, ProductNotAvailable
from .store import Store


def handle_customer():
    say_hallo()
    order = init_order()
    while want_more_products():
        add_product_to_order(order, Store.AVAILABLE_PRODUCTS)
    print_order_summary(order)


def say_hallo():
    print("Witaj w naszym sklepie!")


def init_order():
    first_name = input("Jak masz na imię? ")
    last_name = input("Jakie jest Twoje Nazwisko? ")
    return Order(first_name, last_name)


def want_more_products():
    selection = input("Czy chcesz dodać producty do zamówienia? T/N")
    if selection.upper() != "T" and selection.upper() != "N":
        print("Opcje są tylko dwie")
        return True
    return selection.upper() == "T"


def parse_product_index(product_index_str, max_index):
    try:
        product_index = int(product_index_str)
    except ValueError:
        raise NotValidInput(f"Numer productu musi być liczbą")

    if not 0 <= product_index <= max_index:
        raise NotValidInput(f"Numer productu musi mieścić się w przedziale 0 - {max_index}")

    return product_index


def parse_quantity(quantity_str):
    try:
        quantity = int(quantity_str)
    except ValueError:
        raise NotValidInput(f"Liczba sztuk musi być liczbą")

    if quantity < 1:
        raise NotValidInput(f"Liczba sztuk to co najmniej 1")

    return quantity


def print_order_summary(order):
    print("Twoje zamówienie to:")
    print(order)
    print("Dziękujemy i zapraszamy ponownie")


def add_product_to_order(order, available_products):
    print("Oto dostępne producty: ")
    for index, available_product in enumerate(available_products):
        print(f"{index}) {available_product.product}")

    try:
        product_index_str = input("Wybierz numer: ")
        product_index = parse_product_index(product_index_str, max_index=len(available_products) - 1)

        quantity_str = input("Podaj liczbę sztuk: ")
        quantity = parse_quantity(quantity_str)

    except NotValidInput as input_error:
        print(input_error)
        return

    try:
        order.add_product_to_order(available_products[product_index].product, quantity)
    except TemporaryOutOfStock as error:
        print(
            f"Niestety mamy dostępne tylko {error.available_quantity} sztuk productu {error.product_name}"
        )
    except ProductNotAvailable as error:
        print(f"Produkt {error.product_name} nie jest dostępny. Wybierz inny.")
