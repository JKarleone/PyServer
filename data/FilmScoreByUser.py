from peewee import *
from data.Data import *
from data.Film import *
from data.User import *


class FilmScoreByUser(Data):
    id = BigAutoField()
    film = ForeignKeyField(Film)
    user = ForeignKeyField(User)
    score = SmallIntegerField()

    @staticmethod
    def set_score(film_id: int, user_id: int, new_score: int):
        if FilmScoreByUser.exists(user_id, film_id):
            q = FilmScoreByUser.update(score=new_score).where(FilmScoreByUser.user == user_id,
                                               FilmScoreByUser.film == film_id)
            q.execute()
        else:
            FilmScoreByUser.create(film=film_id, user=user_id, score=new_score)

        query = FilmScoreByUser.select().where(FilmScoreByUser.film == film_id)
        count = 0
        total_score = .0
        for record in query:
            count += 1
            total_score += record.score

        film_query = Film.update(score=(total_score / count)).where(Film.id == film_id)
        film_query.execute()


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
    def exists(user_id: int, film_id: int):
        return FilmScoreByUser.select().where(FilmScoreByUser.user == user_id,
                                       FilmScoreByUser.film == film_id).exists()

    @staticmethod
    def get_all(film_id: int):
        return FilmScoreByUser.select(FilmScoreByUser.score).where(FilmScoreByUser.film == film_id)
