# Generated by Django 2.1.7 on 2019-03-18 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='title',
            new_name='well_name',
        ),
    ]