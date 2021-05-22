# Generated by Django 3.1.4 on 2021-05-22 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diabetes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='diabetes',
        ),
        migrations.AddField(
            model_name='dataset',
            name='feed',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='dataset',
            name='pred',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]