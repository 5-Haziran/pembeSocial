# Generated by Django 4.2.1 on 2023-08-18 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0002_post_postimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postTime',
            field=models.DateTimeField(blank=True, null=True, verbose_name=''),
        ),
    ]
