from django.db import models
from datetime import date
from django.urls import reverse


class Category(models.Model):
    '''Categories[name, description, url]'''
    name = models.CharField(max_length=150)
    description = models.TextField()
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Actor(models.Model):
    '''Actors and film directors[name, age, description, image]'''
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Actor or film director'
        verbose_name_plural = 'Actors or film directors'


class Genre(models.Model):
    '''Genres[name, description, url]'''
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Film(models.Model):
    '''Films
    [title, tagline, description, poster, year, country, directors, actors, genres, 
    world_premiere, buget, box_office,box_office_US, category, url, draft]
    '''
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100, default='')
    description = models.TextField()
    poster = models.ImageField(upload_to='films/')
    year = models.PositiveSmallIntegerField(default='2020')
    country = models.CharField(max_length=30)
    directors = models.ManyToManyField(Actor, related_name='film_director')
    actors = models.ManyToManyField(Actor, related_name='film_actor')
    genres = models.ManyToManyField(Genre)
    world_premiere = models.DateField(default=date.today)
    budget = models.PositiveIntegerField(
        default=0, help_text='Indicate amount the in USD'
    )
    box_office = models.PositiveIntegerField(
        default=0, help_text='Indicate the amount in USD'
    )
    box_office_US = models.PositiveIntegerField(
        default=0, help_text='Indicate the amount in USD'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film_detail', kwargs={'slug': self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'


class FilmStills(models.Model):
    '''Stills from the Film[title, description , image, film]'''
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='film_stills/')
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'FilmStill'
        verbose_name_plural = 'FilmStills'


class RatingStar(models.Model):
    '''Rating Stars[value]'''
    value = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.value}' 

    class Meta:
        verbose_name = 'Rating Star'
        verbose_name_plural = 'Rating Stars'
        ordering = ['-value']


class Rating(models.Model):
    '''Rating Stars[ip, star, film]'''
    ip = models.CharField(max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.star} - {self.film}'

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.film}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
