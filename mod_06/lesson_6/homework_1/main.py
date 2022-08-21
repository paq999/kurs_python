from shop.persistence import load_store, save_store
from shop.user_interface import handle_customer
from shop.store import Store


def run_homework():
    Store.AVAILABLE_PRODUCTS = load_store()
    handle_customer()
    save_store(Store.AVAILABLE_PRODUCTS)


if __name__ == "__main__":
    run_homework()
