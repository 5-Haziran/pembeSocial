# Generated by Django 4.2.1 on 2023-08-24 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0014_profil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='profil_img',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='Profil fotoğrafı'),
        ),
    ]