from peewee import *
from data.Data import *
from data.User import *


class UserType(Data):
    id = AutoField()
    name = CharField()

    @staticmethod
    def add(type_name):
        error_message = ''

        if UserType.select().where(UserType.name == type_name).exists():
            error_message = 'Type is already exists'
            return error_message

        UserType.create(name=type_name)

        return error_message

    @staticmethod
    def remove_by_name(type_name):
        error_message = ''
        if not UserType.select().where(UserType.name == type_name).exists():
            error_message = 'This type doesn\'t exist!'
            return error_message

        return error_message

    @staticmethod
    def count():
        count = 0
        for record in UserType.select():
            count = count + 1

        return count
