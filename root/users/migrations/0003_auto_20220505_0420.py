# Generated by Django 3.2.13 on 2022-05-05 04:20

import random

from django.db import migrations
from django.contrib.auth.hashers import make_password

def add_users(apps, schema_editor):
    Organization = apps.get_model('kudos', 'Organization')
    o = Organization.objects.get(id=1)

    User = apps.get_model('users', 'User')

    users = []
    users_to_create = [('jake', 'jake@example.com'), ('john', 'john@example.com'), ('jane', 'jane@example.com')]
    for user in users_to_create:
        u = User(username=user[0], email=user[1], organization=o)
        u.password = make_password('1234')
        u.save()
        users.append(u)

    Kudos = apps.get_model('kudos', 'Kudos')

    for user in users:
        other_users = [u for u in users if user is not u]
        receiver = random.choice(other_users)
        k = Kudos(sender=user, receiver=receiver)
        k.save()

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_kudos_left'),
        ('kudos', '0003_kudos'),
    ]

    operations = [
        migrations.RunPython(add_users)
    ]
