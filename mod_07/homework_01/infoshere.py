from dataclasses import dataclass
from pprint import pprint

import requests


@dataclass
class PostPreview:
    curse_name: str
    price: str


class InfoShareAcademyParser:
    PAGE_URL = "https://sklep.infoshareacademy.online/?_gl=1*9yrac4*_ga*MjEyNDE4MzU4LjE2NTM0ODAwNDE.*_ga_22XP0ZYPS0*MTY2MTU3NzY2Ny40OC4xLjE2NjE1Nzc3MzUuNjAuMC4w"

    def __init__(self):
        self.page_html = None
        self.last_post_index = 0
        self.found_post_previews = []

    def load_page_html(self):
        response = requests.get(self.PAGE_URL)
        response.raise_for_status()
        self.page_html = response.text

    def parse_all_previews(self):
        while True:
            try:
                self.search_for_next_post_preview()
            except ValueError:
                return

    def search_for_next_post_preview(self):
        curse_name, curse_name_index = self._find_curse_name()
        price, price_index = self._find_price(curse_name_index)
        self.last_post_index = price_index
        self.found_post_previews.append(PostPreview(curse_name.replace("&#8211;", "-"), price.replace(",", ".")))

    def _find_curse_name(self):
        time_marker_open_begin = self.page_html.index(
            '<h2 class="woocommerce-loop-product__title"', self.last_post_index
        )
        time_marker_open_end = self.page_html.index(">", time_marker_open_begin) + len(">")
        time_marker_close = self.page_html.index("</h2>", time_marker_open_end)
        return self.page_html[time_marker_open_end:time_marker_close], time_marker_close

    def _find_price(self, curse_name_index):
        title_header_open = self.page_html.index('<span class="price">', curse_name_index)
        title_url_open_end = self.page_html.index('<bdi>', title_header_open) + len(
            '<bdi>'
        )
        title_url_close = self.page_html.index("&nbsp", title_url_open_end)
        return self.page_html[title_url_open_end:title_url_close], title_url_close


def run_example():
    parser = InfoShareAcademyParser()
    parser.load_page_html()
    parser.parse_all_previews()
    for post in parser.found_post_previews:
        print(f"Cena kursu: {post.curse_name} to: {post.price}zł.")


if __name__ == "__main__":
    run_example()
