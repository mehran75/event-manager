from datetime import datetime

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from database.models import Event, JoinEvent, Category

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


def join_user_in_event(user, event_id):
    try:
        for i in Event.objects.filter(id=event_id):
            event = i
        JoinEvent.objects.get_or_create(event=event, user=user)
        return True
    except:
        return False
    # pass


def find_event(event):
    for i in Event.objects.filter(id=event):
        return i

    return None


def find_joined_uesr(event, user):
    for i in JoinEvent.objects.filter(user=user, event=event):
        return i

    return None


def create_event(title, body, banner, start_date):
    Event.objects.create(title=title, picture=banner, body=body, start_date=start_date,
                         category=Category.objects.filter(id=1)[0])


def remove_event_from_db(id):
    event = Event.objects.filter(id=id)[0]
    event.is_active = False

    event.save()


def edit_event_in_db(id, title=None, start_time=None, body=None, picture=None):
    event = Event.objects.get(id=id)
    if title is not None:
        event.title = title

    if start_time is not None:
        event.start_time = start_time

    if body is not None:
        event.body = body

    if picture is not None:
        event.picture = picture

    event.save()


def get_event(id):
    return Event.objects.filter(id=id)[0]


def get_request_list():
    return JoinEvent.objects.all()
