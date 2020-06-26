from peewee import *
from data.Data import *
from data.User import *


class Film(Data):
    id = AutoField()
    title = CharField()
    description = TextField()
    year = SmallIntegerField()
    score = FloatField()
    creator = ForeignKeyField(User)

    @staticmethod
    def add(title, description, year, creator_id):
        if Film.select().where(Film.title == title and
                               Film.description == description and
                               Film.year == year).exists():
            return 'already added'

        Film.create(title=title, description=description,
                    year=year, score=0.0, creator=creator_id)

        return ''

    @staticmethod
    def remove_by_id(film_id):
        if not Film.select().where(Film.id == film_id).exists():
            return 'Film doesn\'t exist'

        Film.get(Film.id == film_id).delete_instance()

        return ''

    @staticmethod
    def get_all():
        return Film.select()

    @staticmethod
    def exist(film_id):
        return Film.select().where(Film.id == film_id).exists()

    @staticmethod
    def get_creator_login(creator_id):
        query = User.select().where(User.id == creator_id)
        return query[0].login

    @staticmethod
    def get_id_by_title(title: str):
        query = Film.select().where(Film.title == title)
        return query[0].id
