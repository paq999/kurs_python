from shop.product import Product


def test_product_comparison():
    parameters = [
        ("Ciastka", "Jedzenie", 4, "Ciastka", "Jedzenie", 4, True),
        ("Ciastka", "Jedzenie", 4, "Ciastka", "Jedzenie", 4, False),
        ("Ciastka", "Jedzenie", 4, "Ciastka", "Słodycze", 4, False),
        ("Ciastka", "Jedzenie", 4, "Ciastka", "Jedzenie", 8, False)
    ]

    for params in parameters:
        name, category_name, price, other_name, other_category, other_price, expected_result = params

        result = Product(name, category_name, price) == Product(other_name, other_category, other_price)
        if result == expected_result:
            print("Ok")
        else:
            print(f"Błąd! Dla danch {params} wynik porównania jest {result} a powinien być {expected_result}")


def run_homework():
    test_product_comparison()


if __name__ == '__main__':
    run_homework()

