from peewee import *
from data.Data import *


# TODO: create this table
class User(Data):
    id = AutoField()
    login = CharField()
    password = CharField()
    email = CharField()
    name = CharField()
    birthday = DateField()

    @staticmethod
    def add(login, password, email, name, birthday):
        if User.select().where(User.login == login).exists():
            print('This login is already used by another user')
            return

        if User.select().where(User.email == email).exists():
            print('User with this email is already registered')
            return

        User.create(login=login, password=password,
                    email=email, name=name, birthday=birthday)

    @staticmethod
    def remove_by_id(user_id):
        if not User.select().where(User.id == user_id).exists():
            print('User with this id doesn\'t exist')
            return

        # TODO: add deleting other connected rows in sub tables
        User.get(User.id == user_id).delete_instance()

    @staticmethod
    def get_all():
        return User.select()
