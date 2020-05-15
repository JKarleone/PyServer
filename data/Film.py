from peewee import *
from data.Data import *
from data.FilmToGenre import *


# TODO: create this table
class Film(Data):
    id = AutoField()
    title = CharField()
    description = TextField()
    year = SmallIntegerField()
    score = FloatField()

    @staticmethod
    def add(title, description, year, genres_id):
        error_message = ''
        if Film.select().where(Film.title == title and
                               Film.description == description and
                               Film.year == year).exists():
            error_message = 'This film has already been added'
            return error_message

        Film.create(title=title, description=description, year=year)

        for genre_id in genres_id:
            FilmToGenre.create(film=Film.id, genre=genre_id)
        return error_message

    @staticmethod
    def remove_by_id(film_id):
        error_message = ''
        if not Film.select().where(Film.id == film_id).exists():
            error_message = 'This film doesn\'t exist'
            return error_message

        all_genres = FilmToGenre.select().where(FilmToGenre.film == Film.id).get()
        all_genres.delete_instance()

        Film.get(Film.id == film_id).delete_instance()
        return error_message

    @staticmethod
    def get_all():
        return Film.select()

    @staticmethod
    def exist(film_id):
        return Film.select().where(Film.id == film_id).exists()