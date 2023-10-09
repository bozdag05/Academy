from django.contrib import admin
from .models import Movie, Actor, Country, Category, Movie_shot, Type_movie, Rating, Review, Star


# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type_movie', 'premier', 'is_published')
    list_display_links = ['id', 'title']
    list_editable = ['is_published']
    list_filter = ['type_movie', 'premier', 'is_published']
    search_fields = ['id', 'title']


admin.site.register(Actor)
admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Movie_shot)
admin.site.register(Type_movie)
admin.site.register(Rating)
admin.site.register(Review)
admin.site.register(Star)
