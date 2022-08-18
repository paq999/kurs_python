from dataclasses import dataclass

from geopy import Nominatim
from geopy import distance as geopy_distance


@dataclass(frozen=True)
class StreetLocation:
    latitude: float
    longitude: float

    @property
    def location(self):
        return self.latitude, self.longitude


class GeoLocator:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="geo-leo-test")

    def street_location_from_address(self, address) -> StreetLocation:
        geocode_location = self.geolocator.geocode(address)
        return StreetLocation(geocode_location.latitude, geocode_location.longitude)


def meter_distance(src, dst) -> int:
    return int(geopy_distance.distance(src.location, dst.location).meters)


