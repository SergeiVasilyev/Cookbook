# Generated by Django 3.2.8 on 2021-11-17 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resepti_app', '0003_auto_20211117_1057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe_ingredient',
            old_name='ingredient_id',
            new_name='ingredient',
        ),
        migrations.RenameField(
            model_name='recipe_ingredient',
            old_name='recipe_id',
            new_name='recipe',
        ),
    ]