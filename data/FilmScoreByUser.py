from peewee import *
from data.Data import *
from data.Film import *
from data.User import *


# TODO: create this table
class FilmScoreByUser(Data):
    id = BigAutoField()
    film = ForeignKeyField(Film)
    user = ForeignKeyField(User)
    score = SmallIntegerField()

    @staticmethod
    def add(film_id, user_id, score):
        FilmScoreByUser.create(film=film_id, user=user_id, score=score)

    @staticmethod
    def remove_by_id(user_id, film_id):
        FilmScoreByUser.get(FilmScoreByUser.user == user_id,
                            FilmScoreByUser.film == film_id).delete_instance()

    @staticmethod
    def change_by_id(user_id, film_id, new_score):
        record = FilmScoreByUser.get(user=user_id, film=film_id)
        record.score = new_score
        record.save()

    @staticmethod
    def get_all():
        return FilmScoreByUser.select(FilmScoreByUser.film,
                                      FilmScoreByUser.score)
