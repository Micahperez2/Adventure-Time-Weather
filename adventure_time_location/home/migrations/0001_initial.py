# Generated by Django 3.0.9 on 2020-12-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_city', models.CharField(max_length=25)),
                ('at_city', models.CharField(max_length=25)),
                ('at_image', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('temp', models.FloatField(default=0)),
                ('desc', models.CharField(max_length=25)),
            ],
        ),
    ]
