from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.TextField(blank=False)

    body = models.TextField()


class Event(models.Model):
    title = models.TextField(blank=False)
    body = models.TextField()

    date = timezone.now()

    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)

    is_active = models.BooleanField(('active'), default=True)


# here is only answer to requests
class Request(models.Model):
    REQUEST_ACCEPT = 'accepted'
    REQUEST_DENY = 'failed'
    REQUEST_WAITING = 'waiting'

    RESULTS = [
        (REQUEST_DENY, 0),
        (REQUEST_ACCEPT, 1),
        (REQUEST_WAITING, 2)
    ]

    # sender is users
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    # receiver is the admin(s)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    date = timezone.now()
    result = models.IntegerField(blank=False, choices=RESULTS)

    # optional
    text = models.TextField()


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    path = models.TextField(blank=False)


class Skill(models.Model):
    title = models.TextField(blank=False)


class Skills(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# u = User(user_type=User.ADMIN)
#
# u.mail = 'mehranrafiee5@gmail.com'
# u.first_name = 'Mehran'
# u.last_name = 'Rafiee'
# u.set_password('1234')
# u.save()
