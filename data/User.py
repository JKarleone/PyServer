from peewee import *
from data.Data import *
from data.UserType import *


class User(Data):
    id = AutoField()
    login = CharField()
    password = CharField()
    name = CharField()
    usertype_id = ForeignKeyField(UserType)

    @staticmethod
    def add(login, password, name, usertype_id):
        error_message = ''
        if User.select().where(User.login == login).exists():
            error_message = 'This login is already used by another user'
            return error_message

        User.create(login=login, password=password,
                    name=name, usertype_id=usertype_id)
        return error_message

    @staticmethod
    def auth(login, password):
        return User.select().where(User.login == login and
                                   User.password == password).exists()

    @staticmethod
    def get_user_id_name(login, password):
        query = User.select().where(User.login == login and
                                    User.password == password)
        return str(query[0].usertype_id) + "&" + str(query[0].name) + '&' + str(query[0].id)

