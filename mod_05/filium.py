import csv

import folium


CENTER_POSITION = [50.817423, 19.113843]
MAP_FILE_LOCATION = "map.html"


def generate_example_map():
    generated_map = folium.Map(location=CENTER_POSITION, zoom_start=17)

    with open("export.csv", newline="", encoding="UTF-8") as csv_file:
        points = []
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        for row in csv_reader:
            coord = float(row[2]), float(row[3])
            html = f"""
                <p><b>{header[0]}:</b> {row[0]}</p>
                <p><b>{header[1]}:</b> {row[1]}</p>
                <p><b>{header[2]} geograficzna:</b> {row[2]}</p>
                <p><b>{header[3]}:</b> {row[3]}</p>
                <p><b>{header[4]}:</b> {row[4]}</p>
                <p><b>Prędkość:</b> {row[5]} km/h</p>
                <p><b>Poziom baterii:</b> {row[6]}%</p>
                <a href={row[7][12:-2]} target="_blank">Zobacz w google maps</a>
            """

            iframe = folium.IFrame(html=html, width=300, height=280)
            popup = folium.Popup(iframe)
            icon = folium.Icon(icon="envelope", color="green")
            generated_map.add_child(
                folium.Marker(
                    location=coord,
                    popup=popup,
                    icon=icon
                )
            )
            points.append(coord)

    folium.PolyLine(points, color="red", weight=3, opacity=1).add_to(generated_map)
    generated_map.save(MAP_FILE_LOCATION)


def run_example():
    generate_example_map()


if __name__ == "__main__":
    run_example()
