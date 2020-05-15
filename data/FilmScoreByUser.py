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
        error_message = ""
        try:
            FilmScoreByUser.get(FilmScoreByUser.user == user_id,
                                FilmScoreByUser.film == film_id).delete_instance()
        except DatabaseError:
            error_message = "Can't delete user score!\nWrong user_id or film_id!"
        return error_message

    @staticmethod
    def change_by_id(user_id, film_id, new_score):
        error_message = ""
        try:
            record = FilmScoreByUser.get(user=user_id, film=film_id)
            record.score = new_score
            record.save()
        except DatabaseError:
            error_message = "Can't update user score!\nWrong user_id or film_id!"
        return error_message

    @staticmethod
    def get_all():
        return FilmScoreByUser.select(FilmScoreByUser.film,
                                      FilmScoreByUser.score)
