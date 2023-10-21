from django.db import models
from datetime import date


# Create your models here.
from django.urls import reverse


class Movie(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    tagline = models.CharField(max_length=200, verbose_name='Тег', blank=True)
    premier = models.DateField(verbose_name='Премьера фильма', default=date.today)
    poster = models.ImageField(verbose_name='Постер', upload_to='movies/movies', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    directors = models.ManyToManyField('Actor', verbose_name='Режиссёр', related_name='film_director')
    actors = models.ManyToManyField('Actor', verbose_name='Актёр', related_name='film_actor')
    country = models.ManyToManyField('Country', verbose_name='Страна', blank=True)
    type_movie = models.ForeignKey('Type_movie', verbose_name='Тип произведения',
                                   help_text='Фильм, сериал, аниме, мультик и т.д.',
                                   on_delete=models.SET_DEFAULT, default=0)
    category = models.ManyToManyField('Category', verbose_name='Категория', related_name='category')
    genre = models.ManyToManyField('Category', verbose_name='Жанр', related_name='genre')
    fees = models.CharField(max_length=25, verbose_name='Доход', blank=True)
    budget = models.CharField(max_length=25, verbose_name='Бюджет', blank=True)
    url = models.SlugField(max_length=100, verbose_name='Ссылка', unique=True)
    date_publication = models.DateTimeField(verbose_name='Дата публикация', auto_now_add=True)
    date_changed = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={"slug": self.url})

    def get_review(self):
        return self.review_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Type_movie(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тип произведения',
                             help_text='Фильм, сериал, аниме, мультик и т.д.')
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Категория')
    description = models.TextField(max_length=150, verbose_name='Описание', blank=True)
    url = models.SlugField(max_length=100, verbose_name='ссылка')
    date_publication = models.DateTimeField(verbose_name='Дата публикация', auto_now_add=True)
    date_changed = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Actor(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    image = models.ImageField(verbose_name='Фото', upload_to='movies/actors', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    date_birth = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    date_death = models.DateField(verbose_name='Дата смерти', blank=True, null=True)
    country = models.ForeignKey('Country', verbose_name='Страна', on_delete=models.SET_NULL, null=True, blank=True, default=0)
    date_publication = models.DateTimeField(verbose_name='Дата публикация', auto_now_add=True)
    date_changed = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актёр'
        verbose_name_plural = 'Актёры'


class Country(models.Model):
    title = models.CharField(max_length=150, verbose_name='Страна')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Movie_shot(models.Model):
    image = models.ImageField(verbose_name='картинка', upload_to='movies/movie_shot')
    tag = models.CharField(max_length=75, verbose_name='Загаловок', blank=True)
    movie = models.ForeignKey('Movie', verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Кадр к фильму'
        verbose_name_plural = 'Кадры к фильму'


class Review(models.Model):
    email = models.EmailField(verbose_name='Почта')
    text = models.TextField(verbose_name='Описание', max_length=5000)
    name = models.CharField(max_length=150, verbose_name='Имя')
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey('Movie', verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Rating(models.Model):
    ip = models.CharField(max_length=25, verbose_name='IP адрес')
    star = models.ForeignKey('Star', verbose_name='звезда', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Star(models.Model):
    value = models.PositiveSmallIntegerField(verbose_name='Звезда', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда'
        verbose_name_plural = 'Звёзды'
