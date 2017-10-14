from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Recipe

def index(request):
    recipe_list = Recipe.objects.all()
    context = {'recipe_list': recipe_list}
    return render(request, 'recipes/index.html', context)

def add(request):
    return HttpResponse("A new recipe is added here.")

def edit(request, recipe_id):
    return HttpResponse("editing recipe % s." % recipe_id)

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe': recipe})
