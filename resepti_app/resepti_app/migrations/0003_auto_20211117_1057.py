# Generated by Django 3.2.8 on 2021-11-17 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resepti_app', '0002_auto_20211117_1048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basic_ingredient',
            options={'ordering': ('basicing_name',)},
        ),
        migrations.RenameField(
            model_name='basic_ingredient',
            old_name='ing_name',
            new_name='basicing_name',
        ),
    ]