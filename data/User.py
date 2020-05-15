from peewee import *
from data.Data import *


# TODO: create this table
class User(Data):
    id = AutoField()
    login = CharField()
    password = CharField()
    email = CharField()
    name = CharField()

    @staticmethod
    def add(login, password, email, name):
        error_message = ''
        if User.select().where(User.login == login).exists():
            error_message = 'This login is already used by another user'
            return error_message

        if User.select().where(User.email == email).exists():
            error_message = 'User with this email is already registered'
            return error_message

        User.create(login=login, password=password,
                    email=email, name=name)
        return error_message

    @staticmethod
    def remove_by_id(user_id):
        error_message = ''
        if not User.select().where(User.id == user_id).exists():
            error_message = "User with this id doesn't exist"
            return error_message

        # TODO: add deleting other connected rows in sub tables
        User.get(User.id == user_id).delete_instance()

        return error_message

    @staticmethod
    def get_all():
        return User.select()
