# Generated by Django 3.2.4 on 2021-07-17 12:43

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=140)),
                ('description', models.TextField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('city', models.CharField(max_length=80)),
                ('price', models.IntegerField()),
                ('address', models.CharField(max_length=140)),
                ('guests', models.IntegerField()),
                ('beds', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('baths', models.IntegerField()),
                ('check_in', models.TimeField()),
                ('check_out', models.TimeField()),
                ('instent_book', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
