from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.db.models import Q
from .models import Movie, Type_movie, Actor, Country, Category
from .forms import ReviewForm


# Create your views here.

class GenreCategoryCountry:
    def get_category(self):
        return Category.objects.all()

    def get_country(self):
        return Country.objects.all()


class MoviesView(GenreCategoryCountry, ListView):
    model = Movie
    template_name = 'movies/movies.html'
    paginate_by = 2
    context_object_name = 'movies'


class MovieDetailView(GenreCategoryCountry, DetailView):
    model = Movie
    slug_field = 'url'
    template_name = 'movies/moviedetail.html'


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST, pk)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class ActorDetailView(DetailView):
    model = Actor
    template_name = 'movies/actordetail.html'
    slug_field = 'name'


class FilterMovieView(GenreCategoryCountry, ListView):

    paginate_by = 2

    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(country__in=self.request.GET.getlist("country")) |
            Q(category__in=self.request.GET.getlist("category"))
        ).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["country"] = ''.join([f"country={x}&" for x in self.request.GET.getlist("country")])
        context["category"] = ''.join([f"category={x}&" for x in self.request.GET.getlist("category")])
        return context

    context_object_name = 'movies'
    template_name = "movies/movies.html"


class Search(ListView):
    context_object_name = 'movies'
    template_name = "movies/movies.html"
    paginate_by = 2

    def get_queryset(self):
        return Movie.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}'
        return context
