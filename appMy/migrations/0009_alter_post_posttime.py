# Generated by Django 4.2.1 on 2023-08-23 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0008_alter_post_posttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postTime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
