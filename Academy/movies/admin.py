from django.contrib import admin
from django.utils.safestring import mark_safe

from django import forms
from .models import Movie, Actor, Country, Category, Movie_shot, Type_movie, Rating, Review, Star

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


class MovieShotsInline(admin.TabularInline):
    model = Movie_shot
    extra = 1
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_img.short_description = 'Изображение'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'type_movie', 'premier', 'get_poster', 'is_published']
    list_display_links = ['id', 'title']
    list_editable = ['is_published']
    list_filter = ['type_movie', 'premier', 'is_published']
    search_fields = ['id', 'title', 'country__title']
    inlines = [MovieShotsInline]
    actions = ["published", "unpublished"]
    form = MovieAdminForm
    readonly_fields = ('get_poster',)
    save_as = True
    save_on_top = True

    def get_poster(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="150" height="160"')

    def published(self, request, queryset):
        row_publish = queryset.update(is_published=True)
        if row_publish == 1:
            message_bit = 'Опубликована 1 запись'
        else:
            message_bit = f'Опубликовано {row_publish} записей'
        self.message_user(request, message=message_bit)


    def unpublished(self, request, queryset):
        row_publish = queryset.update(is_published=False)
        if row_publish == 1:
            message_bit = 'Снята с публикации 1 запись'
        else:
            message_bit = f'Снято с публикации {row_publish} записей'
        self.message_user(request, message=message_bit)

    get_poster.short_description = 'Постер'

    published.short_description = 'Опубликовать'
    published.allowed_permission = ('change',)

    unpublished.short_description = 'Снять с публикации'
    unpublished.allowed_permission = ('change',)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country', 'is_published', 'get_img']
    list_display_links = ['id', 'name', 'get_img']
    list_editable = ['is_published']
    list_filter = ['country', 'is_published']
    search_fields = ['id', 'name', 'country']
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_img.short_description = 'Фото'


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
    list_display = ['name', 'email', 'movie', 'text', 'parent']


admin.site.register(Rating)
admin.site.register(Star)

admin.site.site_title = 'غزة الاحرار'
admin.site.site_header = 'غزة الاحرار'
