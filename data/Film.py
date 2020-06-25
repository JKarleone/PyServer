from peewee import *
from data.Data import *


class Film(Data):
    id = AutoField()
    title = CharField()
    description = TextField()
    year = SmallIntegerField()
    score = FloatField()

    @staticmethod
    def add(title, description, year):
        error_message = ''
        if Film.select().where(Film.title == title and
                               Film.description == description and
                               Film.year == year).exists():
            error_message = 'This film has already been added'
            return error_message

        Film.create(title=title, description=description, year=year)

        return error_message

    @staticmethod
    def remove_by_id(film_id):
        error_message = ''
        if not Film.select().where(Film.id == film_id).exists():
            error_message = 'This film doesn\'t exist'
            return error_message

        Film.get(Film.id == film_id).delete_instance()
        return error_message

    @staticmethod
    def get_all():
        return Film.select()

    @staticmethod
    def exist(film_id):
        return Film.select().where(Film.id == film_id).exists()