from new_movies.rented_move import RentedMove
from new_movies import permissions
from new_movies.exceptions import (
    NoCreditsForMovieRent,
    MovieNotFound,
    ViewsLimitReached,
    ActionNotAllowed,
)


def rent_movie(user, move):
    if user.credits_left < 1:
        raise NoCreditsForMovieRent()
    user.rented_movies.append(RentedMove(move))
    user.credits_left -= 1


#
# def watch_movie(user, movie):
#     def get_rented_movie():
#         for rented_move in user.rented_movies:
#             if rented_move.movie == movie:
#                 return rented_move
#
#     user_rented_movie = get_rented_movie()
#     if not user_rented_movie:
#         raise MovieNotFound()
#
#     if user_rented_movie.views_left < 1:
#         raise ViewsLimitReached()
#
#     user_rented_movie.views_left -= 1
#     _start_streaming(user, movie)


def _start_streaming(user, movie):
    print(f"User: {user} is watching {movie}")


def _get_rented_movie(user, movie):
    for rented_move in user.rented_movies:
        if rented_move.movie == movie:
            return rented_move


def watch_movie(user, movie):
    rented_movie = _get_rented_movie(user, movie)
    if not rented_movie:
        raise MovieNotFound()

    if rented_movie.views_left < 1:
        raise ViewsLimitReached()

    rented_movie.views_left -= 1
    _start_streaming(user, movie)


def refresh_credits(acting_user, user_to_be_refreshed):
    if permissions.is_admin(acting_user) or permissions.is_moderator(acting_user):
        user_to_be_refreshed.credits_left = 5
    else:
        raise ActionNotAllowed()
