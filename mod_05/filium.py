import random

import folium


MIERZYN_CENTER_POSITION = [51.2667981, 19.6664517]
MAP_FILE_LOCATION = "map.html"


def random_point():
    return random.uniform(51.1, 51.4), random.uniform(19.4, 19.8)


def generate_example_map():
    generated_map = folium.Map(location=MIERZYN_CENTER_POSITION, zoom_start=13)

    # for number in range(20):
    #     generated_map.add_child(
    #         folium.CircleMarker(
    #             location=random_point(),
    #             fill="true",
    #             radius=8,
    #             popup=str(number),
    #             fill_color="blue",
    #             fill_opacity=1
    #         )
    #     )
    points = [random_point() for _ in range(5)]

    folium.PolyLine(points, color="red", weight=3.5, opacity=1).add_to(
        generated_map
    )

    generated_map.save(MAP_FILE_LOCATION)


def run_example():
    generate_example_map()


if __name__ == "__main__":
    run_example()
