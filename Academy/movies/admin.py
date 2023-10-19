from django.contrib import admin
from .models import Movie, Actor, Country, Category, Movie_shot, Type_movie, Rating, Review, Star


# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'type_movie', 'premier', 'is_published']
    list_display_links = ['id', 'title']
    list_editable = ['is_published']
    list_filter = ['type_movie', 'premier', 'is_published']
    search_fields = ['id', 'title', 'country__title']
    inlines = [ReviewInline]
    save_as = True
    save_on_top = True


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'country', 'is_published']
    list_display_links = ['id', 'name', 'image']
    list_editable = ['is_published']
    list_filter = ['country', 'is_published']
    search_fields = ['id', 'name', 'country']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title']


@admin.register(Type_movie)
class TypeMovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'url', 'is_published']
    list_display_links = ['id', 'title']
    list_editable = ['is_published']
    search_fields = ['id', 'title', 'url']
    list_filter = ['is_published']


@admin.register(Movie_shot)
class MovieShotAdmin(admin.ModelAdmin):
    list_display = ['image', 'tag', 'movie']
    list_display_links = ['image']
    search_fields = ['movie']
    list_filter = ['movie']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'movie']


admin.site.register(Rating)
admin.site.register(Star)
