# Generated by Django 3.1.4 on 2021-05-20 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('bmi', models.IntegerField()),
                ('wrkout', models.IntegerField()),
                ('alcol', models.IntegerField()),
                ('gender', models.IntegerField()),
                ('bp', models.IntegerField()),
                ('chol', models.IntegerField()),
                ('suger', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('race', models.IntegerField()),
                ('marital', models.IntegerField()),
                ('edu', models.IntegerField()),
                ('smoke', models.IntegerField()),
                ('preg', models.IntegerField()),
                ('diabetes', models.IntegerField(null=True)),
            ],
        ),
    ]
