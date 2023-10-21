from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie, Type_movie
from .forms import ReviewForm

# Create your views here.

class MoviesView(ListView):
    model = Movie

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.filter(is_published=True)
        context['types'] = Type_movie.objects.all()
        return context

    template_name = 'movies/movies.html'


class MovieDetailView(DetailView):
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
