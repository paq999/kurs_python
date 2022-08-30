from dataclasses import dataclass
from pprint import pprint

import requests
from bs4 import BeautifulSoup


@dataclass
class PostPreview:
    curse_name: str
    price: float


def curse_a(tag):
    return (
        tag.name == "a" and tag.has_attr("class") and "woocommerce-LoopProduct-link" in tag["class"]
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
        all_curse = self.parsed_page.find_all(curse_a)
        for curs in all_curse:
            curs_name = curs.h2.string
            curs_span_tags = curs.find_all("bdi")
            try:
                curs_price = float(curs_span_tags[1].get_text(strip=" ").replace(",", ".")[:-2])
            except IndexError:
                curs_price = float(curs_span_tags[0].get_text(strip=" ").replace(",", ".")[:-2])
            self.found_curses.append(PostPreview(curse_name=curs_name, price=curs_price))


def run_example():
    paser = InfoShareAcademyParser()
    paser.load_page_html()
    paser.parser_all_curses()
    pprint(paser.found_curses)


if __name__ == "__main__":
    run_example()
