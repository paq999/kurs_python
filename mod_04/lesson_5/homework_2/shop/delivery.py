import random


def product_delivery():
    available_product = [
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
    return [available_product[random.randint(0, 9)]]

