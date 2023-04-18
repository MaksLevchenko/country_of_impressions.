# Generated by Django 4.1.7 on 2023-03-19 09:30

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название города')),
                ('title', models.TextField(max_length=500, verbose_name='Краткое описание города')),
                ('city_emblem', models.ImageField(upload_to='', verbose_name='Герб')),
                ('url', models.SlugField(unique=True)),
                ('founding_date', models.CharField(max_length=15, verbose_name='Дата основания города')),
                ('founder', models.CharField(max_length=30, verbose_name='Основатель города')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
                'ordering': ['-value'],
            },
        ),
        migrations.CreateModel(
            name='Sight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название достопримечательности')),
                ('title', models.TextField(max_length=500, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('place', models.CharField(max_length=150, verbose_name='Месторасположения')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_in_Russia.city')),
            ],
            options={
                'verbose_name': 'Достопримечательность',
                'verbose_name_plural': 'Достопримечательности',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='travel_in_Russia.city', verbose_name='город')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='travel_in_Russia.review', verbose_name='родитель')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адрес')),
                ('city', models.ForeignKey(on_delete=django.db.models.fields.CharField, related_name='rating', to='travel_in_Russia.city', verbose_name='город')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_in_Russia.ratingstar', verbose_name='звезда')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='photo/', verbose_name='Изображение')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_in_Russia.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
    ]
