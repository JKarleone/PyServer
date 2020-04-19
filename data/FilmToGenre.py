from peewee import *
from data.Data import *
from data.Film import *
from data.Genre import *


# TODO: create this table
class FilmToGenre(Data):
    id = BigAutoField()
    film = ForeignKeyField(Film)
    genre = ForeignKeyField(Genre)
