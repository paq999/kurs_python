from dataclasses import dataclass
from pprint import pprint

import requests
from bs4 import BeautifulSoup


@dataclass
class PostPreview:
    curse_name: str
    price: float


def curse_name_div(tag):
    return (
        tag.name == "h2"
        and tag.has_attr("class")
        and "woocommerce-loop-product__title" in tag["class"]
    )


def curse_price_div(tag):

    return (
        tag.name == "span"
        and tag.bdi
        and tag.has_attr("class")
        and "woocommerce-Price-amount" in tag["class"]
    )


class InfoShareAcademyParser:
    PAGE_URL = "https://sklep.infoshareacademy.online/?_gl=1*9yrac4*_ga*MjEyNDE4MzU4LjE2NTM0ODAwNDE.*_ga_22XP0ZYPS0*MTY2MTU3NzY2Ny40OC4xLjE2NjE1Nzc3MzUuNjAuMC4w"

    def __init__(self):
        self.page_html = None
        self.last_post_index = 0
        self.found_curses = []

    def load_page_html(self):
        response = requests.get(self.PAGE_URL)
        response.raise_for_status()
        self.parsed_page = BeautifulSoup(response.text, features="html.parser")

    def parser_all_curses(self):
        curses_name = self.parsed_page.find_all(curse_name_div)
        curses_price = self.parsed_page.find_all(curse_price_div)

        for curse_name, curse_price in zip(curses_name, curses_price):
            self.found_curses.append(
                PostPreview(
                    curse_name.string, float(curse_price.get_text(strip=" ").replace(",", ".")[:-2])
                )
            )


def run_example():
    paser = InfoShareAcademyParser()
    paser.load_page_html()
    paser.parser_all_curses()
    print(paser.found_curses)


if __name__ == "__main__":
    run_example()
