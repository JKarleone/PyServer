from peewee import *
from data.Data import *


# TODO: create this table #3
class UserType(Data):
    id = AutoField()
    user_id = IntegerField()
    # TODO: change user_id type to ForeignKeyField(User) when User will be added
    type = CharField()

    @staticmethod
    def add(user_id, type):
        if type != "Moderator" or "Admin" or "User":
            print('Wrong user type name')
            return

        if UserType.select().where(UserType.user_id == user_id).exists():
            print('User has already get his own type')
            return

        UserType.create(user_id=user_id, type=type)

    @staticmethod
    def remove_by_id(user_id):
        if not UserType.select().where(UserType.user_id == user_id).exists():
            print('This user haven\'t got his own type')
            return

        UserType.get(UserType.user_id == user_id).delete_instance()

    @staticmethod
    def change_type_by_id(user_id, new_type):
        if new_type != "Moderator" or "Admin" or "User":
            print('Wrong user type name')
            return

        # TODO: check right update func
