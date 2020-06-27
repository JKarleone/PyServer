from data.User import User
from data.UserType import UserType
from data.Film import Film
from data.FilmScoreByUser import FilmScoreByUser
from data.Person import Person
from data.Filmmaker import Filmmaker
from data.Actor import Actor
from server.Server import Server


if __name__ == '__main__':
    # Create tables if they're not exist
    UserType.create_table()
    User.create_table()
    Person.create_table()
    Film.create_table()
    FilmScoreByUser.create_table()
    Actor.create_table()
    Filmmaker.create_table()

    if UserType.count() == 0:
        UserType.add("User")
        UserType.add("Admin")

    # Main Loop
    server = Server()
    server.start()
