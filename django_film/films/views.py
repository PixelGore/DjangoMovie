from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.db.models import Q
from django.http import JsonResponse
# Local imports
from .models import Film, Category, Actor, Genre, Rating, Reviews
from .forms import ReviewForm, RatingForm


class GenreYear():
    '''Genre and release year of film'''

    def get_genre(self):
        return Genre.objects.all()

    def get_year(self):
        return Film.objects.filter(draft=False).values("year")


class FilmView(GenreYear, ListView):
    '''Film List'''

    model = Film
    queryset = Film.objects.filter(draft=False)
    paginate_by = 3


class FilmDetailView(GenreYear, DetailView):
    '''Full description'''

    model = Film
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
        context["form"] = ReviewForm()
        return context


class FilterFilmView(GenreYear, ListView):
    '''Film Filter'''

    paginate_by = 2

    def get_queryset(self):
        queryset = Film.objects.all()
        if "year" in self.request.GET:
            queryset = queryset.filter(
                year__in=self.request.GET.getlist('year'))
        if "genre" in self.request.GET:
            queryset = queryset.filter(
                genres__in=self.request.GET.getlist('genre'))
        return queryset


class AddReview(View):
    '''Film Reviews'''

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        film = Film.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get("parent"))
            form.film = film
            form.save()
        return redirect(film.get_absolute_url())


class AddStarRating(View):
    '''Adding rating to film'''
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid:
            Rating.objects.update_or_create(
                ip = self.get_client_ip(request),
                film_id = int(request.POST.get('film')),
                defaults = {'star_id' : int(request.POST.get('star'))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


class ActorView(GenreYear, DetailView):
    '''Info about an actor or film director'''

    model = Actor
    template_name = 'films/actor.html'
    slug_field = "name"


class JsonFilterFilmsView(ListView):
    '''Json films filter'''

    def get_queryset(self):
        queryset = Film.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) |
            Q(genres__in=self.request.GET.getlist('genre'))
        ).distinct().values("title", "tagline", "url", "poster")
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({'films': queryset}, safe=False)


class Search(ListView):
    '''View for searching films'''

    paginate_by = 3

    def get_queryset(self):
        return Film.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context
