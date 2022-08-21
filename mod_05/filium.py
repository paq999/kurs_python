import csv

import folium


CENTER_POSITION = [50.817423, 19.113843]
MAP_FILE_LOCATION = "map.html"


def generate_example_map():
    generated_map = folium.Map(location=CENTER_POSITION, zoom_start=17)

    with open("export.csv", newline="", encoding="UTF-8") as coordinate:
        points = []
        csv_reader = csv.reader(coordinate)
        for index, row in enumerate(csv_reader):
            if index == 0:
                continue
            coord = float(row[2]), float(row[3])
            html = f"""
                <p><b>Data:</b> {row[0]}</p>
                <p><b>Czas:</b> {row[1]}</p>
                <p><b>Szerokość geograficzna:</b> {row[2]}</p>
                <p><b>Długość geograficzna:</b> {row[3]}</p>
                <p><b>Typ lokalizacji:</b> {row[4]}</p>
                <p><b>Prędkość:</b> {row[5]} km/h</p>
                <p><b>Poziom baterii:</b> {row[6]}%</p>
                <a href={row[7][12:-2]} target="_blank">Zobacz w google maps</a>
            """
            iframe = folium.IFrame(html=html, width=300, height=280)
            popup = folium.Popup(iframe)
            generated_map.add_child(
                folium.Marker(
                    location=coord,
                    popup=popup,
                    icon=folium.Icon(color="green")
                )
            )
            points.append(coord)

    folium.PolyLine(points, color="red", weight=3, opacity=1).add_to(generated_map)
    generated_map.save(MAP_FILE_LOCATION)


def run_example():
    generate_example_map()


if __name__ == "__main__":
    run_example()
