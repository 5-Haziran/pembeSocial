# Generated by Django 4.2.1 on 2023-08-28 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0020_alter_profil_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
