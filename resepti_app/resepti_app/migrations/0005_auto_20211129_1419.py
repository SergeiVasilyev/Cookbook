# Generated by Django 3.2.8 on 2021-11-29 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resepti_app', '0004_auto_20211117_1147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe_ingredient',
            options={'ordering': ('id',)},
        ),
        migrations.AddField(
            model_name='recipe_ingredient',
            name='ing_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ing_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]