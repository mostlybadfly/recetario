from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, IngredientForm, InstructionForm

from .models import Recipe

def index(request):
    recipe_list = Recipe.objects.all()
    context = {'recipe_list': recipe_list}
    return render(request, 'recipes/index.html', context)

@login_required
def add(request):
    form = RecipeForm(request.POST)
    if form.is_valid():
        recipe = form.save(commit=False)
        recipe.created_by = request.user
        recipe.save()
        return redirect('edit', recipe_id=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipes/add.html', {'form': form})

@login_required
def edit(request, recipe_id):
    return HttpResponse("editing recipe % s." % recipe_id)

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe': recipe})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def ingredients(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {'ingredients': recipe.ingredients.all(), 'recipe_id': recipe_id}
    return render(request, 'recipes/ingredients.html', context)

@login_required
def edit_ingredients(request, recipe_id):
    form = IngredientForm(request.POST)
    if form.is_valid():
        ingredient = form.save(commit=False)
        ingredient.recipe_id = recipe_id
        ingredient.save()
        return redirect('ingredients', recipe_id)
    else:
        form = IngredientForm()
    return render(request, 'recipes/edit_ingredients.html', {'form': form})

@login_required
def instructions(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {'instructions': recipe.instructions.all(), 'recipe_id': recipe_id}
    return render(request, 'recipes/instructions.html', context)

@login_required
def edit_instructions(request, recipe_id):
    form = InstructionForm(request.POST)
    if form.is_valid():
        instruction = form.save(commit=False)
        instruction.recipe_id = recipe_id
        instruction.save()
        return redirect('instructions', recipe_id)
    else:
        form = InstructionForm()
    return render(request, 'recipes/edit_instructions.html', {'form': form})
