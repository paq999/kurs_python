from dataclasses import dataclass

from new_movies.movie import Movie


@dataclass
class RentedMove:
    movie: Movie
    views_left: int = 3


