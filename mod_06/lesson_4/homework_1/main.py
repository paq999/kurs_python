from shop.user_interface import handle_customer


def ask_for_me():
    name = input("Podaj pierwsze trzy litery swojego imienia: ")
    name_len = len(name)

    if name_len < 3:
        raise ValueError("Za krótkie!")

    if name_len > 3:
        raise ValueError("Za długie!")

    print("Dziękuje :) Ja jestem python następca języka ABC")


def run_homework():
    try:
        ask_for_me()
    except ValueError as error:
        print(f"Wprowadzone złe dane: {error}")
    else:
        print("Wszytko w porządku możemy kontynuować")
    finally:
        print("Niezależnie od wszystkego jest spoko")


if __name__ == "__main__":
    run_homework()
