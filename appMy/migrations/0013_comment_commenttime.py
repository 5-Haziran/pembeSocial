# Generated by Django 4.2.1 on 2023-08-24 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0012_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commentTime',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name=''),
        ),
    ]