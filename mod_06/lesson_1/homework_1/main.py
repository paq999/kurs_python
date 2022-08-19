from mod_06.lesson_1.homework_1.shop import data_generator
from mod_06.lesson_1.homework_1.shop.order import Order


def run_homework():
    # order_elements_on_limits = data_generator.generate_order_elements(products_to_generate=Order.MAX_ELEMENTS)
    # order_on_limit = Order("Bob", "Kowalski", order_elements=order_elements_on_limits)
    # print(order_on_limit)
    #
    # product = data_generator.generate_product()
    # quantity = data_generator.generate_quantity()
    # order_on_limit.add_product_to_order(product, quantity)

    order_elements_over_limits = data_generator.generate_order_elements(products_to_generate=Order.MAX_ELEMENTS + 1)
    order_over_limit = Order("Bob", "Kowalski", order_elements=order_elements_over_limits)



if __name__ == "__main__":
    run_homework()
