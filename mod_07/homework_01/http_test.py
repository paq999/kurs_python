import requests


def demo_request():
    try:
        response = requests.get("https://infoshareacademy.com")
    except requests.RequestException as error:
        print(error)
        return

    try:
        response.raise_for_status()
    except requests.HTTPError as error:
        print(error)
        return

    print(response.text)


if __name__ == "__main__":
    demo_request()
