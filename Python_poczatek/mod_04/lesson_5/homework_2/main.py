from shop.delivery import product_delivery


def run_homework():
    needed_product = [
        "Chleb",
        "ciastka",
        "jabłka",
        "dżem",
        "pomarańcze",
        "marchew",
        "bułki",
        "ziemniaki",
        "ser",
        "mleko"
    ]

    received_product = []

    while not set(needed_product) == set(received_product):
        new_product = product_delivery()
        received_product += new_product
        print(f"Otrzymano product: {new_product}")
        missing_products = set(needed_product).difference(received_product)
        print(f"Brakuje jeszcze: {missing_products}")

    print(f"Łącznie otrzymano: {received_product}")


if __name__ == '__main__':
    run_homework()

