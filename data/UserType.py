from peewee import *
from data.Data import *
from data.User import *


class UserType(Data):
    id = AutoField()
    user_id = ForeignKeyField(User)
    type = CharField()

    @staticmethod
    def add(user_id, type_name):
        error_message = ''
        if type_name != "Moderator" or "Admin" or "User":
            error_message = 'Wrong user type name'
            return error_message

        if UserType.select().where(UserType.user_id == user_id).exists():
            error_message = 'User has already get his own type'
            return error_message

        UserType.create(user_id=user_id, type=type_name)
        return error_message

    @staticmethod
    def remove_by_id(user_id):
        error_message = ''
        if not UserType.select().where(UserType.user_id == user_id).exists():
            error_message = 'This user haven\'t got his own type'
            return error_message

        UserType.get(UserType.user_id == user_id).delete_instance()
        return error_message

    @staticmethod
    def change_type_by_id(user_id, new_type):
        error_message = ''
        if new_type != ("Moderator" or "Admin" or "User"):
            error_message = 'Wrong user type name'
            return error_message

        current_user = UserType.select().where(UserType.user_id == user_id).get()
        current_user.type = new_type
        current_user.save()
        return error_message
