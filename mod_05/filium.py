import csv
import random

import folium


MIERZYN_CENTER_POSITION = [50.817423, 19.113843]
MAP_FILE_LOCATION = "map.html"


def random_point():
    return random.uniform(51.1, 51.4), random.uniform(19.4, 19.8)


def generate_example_map():
    generated_map = folium.Map(location=MIERZYN_CENTER_POSITION, zoom_start=16)

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
    # points = [random_point() for _ in range(10)]
    # print(points)
    with open("export.csv", newline="", encoding="UTF-8") as coordinate:
        points = []
        csv_reader = csv.reader(coordinate)
        for index, row in enumerate(csv_reader):
            if index == 0:
                continue
            coord = float(row[2]), float(row[3])
            html = f"""
                <p>Data: {row[0]}</p>
                <p>Godzina: {row[1]}</p>
                <p>Długość geograficzna: {row[2]}</p>
                <p>Szerokość geograficzna: {row[3]}</p>
                <p>Szybkość przemieszczania: {row[5]}km/h</p>
                <p>Poziom nadładowania baterii: {row[6]}%</p>
            """
            iframe = folium.IFrame(html=html, width=300, height=250)
            popup = folium.Popup(iframe, max_width=2500)
            generated_map.add_child(
                folium.Marker(
                    location=coord,
                    fill="true",
                    radius=8,
                    popup=popup,
                    fill_color="blue",
                    fill_opacity=1
                )
            )
            points.append(coord)

    # generated_map = folium.Map(location=points[0], zoom_start=15)
    folium.PolyLine(points, color="red", weight=3.5, opacity=1).add_to(generated_map)
    generated_map.save(MAP_FILE_LOCATION)


def run_example():
    generate_example_map()


if __name__ == "__main__":
    run_example()
