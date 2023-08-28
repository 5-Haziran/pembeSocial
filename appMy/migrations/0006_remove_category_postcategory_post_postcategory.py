# Generated by Django 4.2.1 on 2023-08-18 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0005_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='postCategory',
        ),
        migrations.AddField(
            model_name='post',
            name='postCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.category', verbose_name='Kategory'),
        ),
    ]
