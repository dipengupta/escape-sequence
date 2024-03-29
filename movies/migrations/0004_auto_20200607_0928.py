# Generated by Django 3.0.6 on 2020-06-07 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20200531_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpcomingReviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieTitle', models.CharField(max_length=300)),
                ('releaseYear', models.IntegerField()),
                ('moviePoster', models.ImageField(default='movies/posters/defaultPoster.jpg', upload_to='movies/posters')),
                ('movieSummary', models.TextField(blank=True)),
                ('movieGenre', models.TextField()),
                ('movieAgeRating', models.TextField(blank=True)),
                ('movieDirectors', models.TextField(blank=True)),
                ('movieActors', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Upcoming Reviews',
            },
        ),
        migrations.RemoveField(
            model_name='allmovies',
            name='movieStill',
        ),
    ]
