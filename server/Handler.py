from data.User import *
from data.Film import *
from data.Filmmaker import *
from data.Actor import *
from data.FilmScoreByUser import *


class Handler:
    @staticmethod
    def handle(data: str):
        try:
            table_name = data.split('&')[0]
        except ValueError:
            return 'predictable error'

        if table_name == 'reg':
            return Handler.registration(data)

        if table_name == 'auth':
            return Handler.authentication(data)

        if table_name == 'film':
            return Handler.film_handler(data)

        if table_name == 'score':
            return Handler.score(data)

        return 'error'

    # Example request:
    # film&add&my_title&my_description&2017&1&John Cena, Leonardo Di Caprio&Bondarchuk
    @staticmethod
    def film_handler(data: str):
        try:
            split_data = data.split('&')
            command = split_data[1]
        except IndexError:
            return 'params error'
        except:
            return 'unknown error'

        if command == 'add':
            try:
                title = split_data[2]
                description = split_data[3]
                year = split_data[4]
                user_id = int(split_data[5])
                actors = split_data[6]
                filmmaker = split_data[7]
            except ValueError:
                return 'params error'

            filmmaker = filmmaker.strip()

            try:
                actors_list = actors.split(',')
            except:
                actors_list = actors

            msg = Film.add(title, description, year, user_id)

            for actor in actors_list:
                actor_name = actor.strip()
                if actor != '':
                    Person.add(actor_name)
                    Actor.add(Film.get_id_by_title(title), Person.get_id_by_name(actor_name))

            if filmmaker != '':
                Person.add(filmmaker)
                Filmmaker.add(Person.get_id_by_name(filmmaker), Film.get_id_by_title(title))

            return 'ok' if msg == '' else msg

        if command == 'getall':
            ans = ''
            films = Film.get_all()

            for film in films:
                actors = Actor.get_names_by_film(film)
                filmmaker = Filmmaker.get_name_by_film(film)
                actors_str = ''
                for actor_name in actors:
                    actors_str += actor_name + ','
                actors_str = actors_str[:len(actors_str) - 1]

                ans += film.title + '&' + film.description + '&' + \
                       str(film.year) + '&' + str(film.score) + '&' + \
                       Film.get_creator_login(film.creator) + '&' + actors_str + '&' + \
                       filmmaker + '\n'

            print(ans)
            return ans

        if command == 'delete':
            try:
                title = split_data[2]
            except ValueError:
                return 'params error'

            film_id = Film.get_id_by_title(title)
            q = Filmmaker.delete().where(Filmmaker.film == film_id)
            q.execute()
            q = Actor.delete().where(Actor.film == film_id)
            q.execute()
            q = FilmScoreByUser.delete().where(FilmScoreByUser.film == film_id)
            q.execute()
            q = Film.select().where(Film.id == film_id)
            q[0].delete_instance()
            return ''



    # Example request:
    # reg&my_login&my_pass&my_name&1
    @staticmethod
    def registration(data: str):
        try:
            split_data = data.split('&')
            login = split_data[1]
            password = split_data[2]
            name = split_data[3]
        except IndexError:
            return 'params error'
        except:
            return 'unknown error'

        msg = User.add(login, password, name, 1)

        if msg == '':
            q = User.select().where(User.login == login)
            return str(q[0].id)
        return msg

    # Example request:
    # auth&my_login&vTk34Fs6
    @staticmethod
    def authentication(data: str):
        try:
            split_data = data.split('&')
            login = split_data[1]
            password = split_data[2]
        except IndexError:
            return 'params error'
        except:
            return 'unknown error'

        check = User.auth(login, password)
        return User.get_user_id_name(login, password) if check else 'auth error'

    @staticmethod
    def score(data: str):
        try:
            split_data = data.split('&')
            method = split_data[1]
        except IndexError:
            return 'params error'
        except:
            return 'unknown error'

        # Example request:
        # score&set&5&123&title
        if method == 'set':
            try:
                score = int(split_data[2])
                user_id = int(split_data[3])
                title = split_data[4]
            except IndexError:
                return 'params error'
            except:
                return 'unknown error'

            film_id = Film.get_id_by_title(title)
            FilmScoreByUser.set_score(film_id, user_id, score)
            return ''

        # Example request:
        # score&get&2&title
        if method == 'get':
            try:
                user_id = split_data[2]
                title = split_data[3]
            except IndexError:
                return 'params error'
            except:
                return 'unknown error'

            film_id = Film.get_id_by_title(title)
            query = FilmScoreByUser.select().where(FilmScoreByUser.user == user_id,
                                                   FilmScoreByUser.film == film_id)
            if len(query) == 0:
                return str(0)

            return str(query[0].score)

        return 'error'
