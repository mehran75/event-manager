from datetime import datetime

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from database.models import Event

from django.contrib import admin

salt = '12@{}E#E}{'
hash_algorithm = 'default'


def get_hashed_password(password):
    return make_password(password, salt, hash_algorithm)


def check_user_exist(mail, raw_password):
    """
    validate user
    :param mail: str
    :param raw_password: plain text
    :return: User model if validate otherwise, None
    """
    u = User(email=mail, password=make_password(raw_password, salt, hash_algorithm))

    if u.objects.count() == 0:
        return None
    else:
        return u.objects


def register_new_user(fields_dic, is_admin=False):
    """
    register new User
    :param is_admin: only if Admin is creating a user
    :param fields_dic: dictionary
    :return: User object
    """

    # check if required fileds exists in dictionary
    if 'mail' and 'password' and 'first_name' and 'last_name' not in fields_dic.keys():
        return None
    #
    # user = User(email=fields_dic['mail'], username=fields_dic['mail'],
    #             password=get_hashed_password(fields_dic['password']),
    #             first_name=fields_dic['first_name'], last_name=fields_dic['last_name'])

    user = User.objects.create_user(fields_dic['mail'], email=fields_dic['mail'],
                                    password=get_hashed_password(fields_dic['password']),
                                    first_name=fields_dic['first_name'], last_name=fields_dic['last_name'])

    user.is_active = is_admin
    user.is_staff = is_admin
    user.date_joined = datetime.now()

    if User.objects.filter(username=fields_dic['mail']).exists():
        return None
    user.save()

    return user


def get_active_events():
    # print(Event.objects.filter(is_active=True))
    return Event.objects.filter(is_active=True)


def get_all_events():
    return Event.objects.all()


def get_users_count():
    return User.objects.count()
