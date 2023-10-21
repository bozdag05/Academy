from django import template
from movies.models import Type_movie, Movie

register = template.Library()

@register.simple_tag()
def get_types():
    return Type_movie.objects.all()


@register.inclusion_tag("movies/tags/last_movies.html")
def get_last_movies():
    movies = Movie.objects.order_by("id")[:5]
    return {"last_movies": movies}


