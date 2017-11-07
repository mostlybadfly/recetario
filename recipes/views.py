from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, IngredientForm, InstructionForm, IngredientFormSet
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Recipe, Ingredient, Instruction

class IngredientCreate(CreateView):
    model = Recipe
    fields = ['title', 'cuisine', 'cooking_time', 'servings']
    succes_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        data = super(IngredientCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['ingredients'] = IngredientFormSet(self.request.POST)
        else:
            data['ingredients'] = IngredientFormSet()
        return data
    
    def form_valid(self, form):
        context = self.get_context_data()
        ingredients = context['ingredients']
        with transaction.atomic():
            self.object = form.save()

            if ingredients.is_valid():
                ingredients.instance = self.object
                ingredients.save()
        return super(IngredientCreate, self).form_valid(form)

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
        return redirect('detail', recipe_id=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_edit.html', {'form': form})

@login_required
def edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    form = RecipeForm(request.POST, instance=recipe)
    if form.is_valid():
        recipe = form.save(commit=False)
        recipe.created_by = request.user
        recipe.save()
        return redirect('detail', recipe_id=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_edit.html', {'form': form})

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    ingredients = recipe.ingredients.all()
    instructions = recipe.instructions.all()
    return render(request, 'recipes/detail.html',
                  {'recipe': recipe, 'ingredients': ingredients, 'instructions': instructions})

@login_required
def ingredient_add(request, recipe_id):
    form = IngredientForm(request.POST)
    if form.is_valid():
        ingredient = form.save(commit=False)
        ingredient.recipe_id = recipe_id
        ingredient.save()
        return redirect('detail', recipe_id)
    else:
        form = IngredientForm()
    return render(request, 'recipes/ingredient_edit.html',
                  {'form': form, 'recipe_id': recipe_id})

@login_required
def ingredient_edit(request, recipe_id, ingredient_id):
    ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
    form = IngredientForm(request.POST, instance=ingredient)
    if form.is_valid():
        ingredient = form.save(commit=False)
        ingredient.save()
        return redirect('detail', ingredient.recipe_id)
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'recipes/ingredient_edit.html', {'form': form})

@login_required
def instruction_add(request, recipe_id):
    form = InstructionForm(request.POST)
    if form.is_valid():
        instruction = form.save(commit=False)
        instruction.recipe_id = recipe_id
        instruction.save()
        return redirect('detail', recipe_id)
    else:
        form = InstructionForm()
    return render(request, 'recipes/instruction_edit.html',
                  {'form': form, 'recipe_id': recipe_id})

@login_required
def instruction_edit(request, recipe_id, instruction_id):
    instruction = get_object_or_404(Instruction, pk=instruction_id)
    form = InstructionForm(request.POST, instance=instruction)
    if form.is_valid():
        instruction = form.save(commit=False)
        instruction.save()
        return redirect('detail', instruction.recipe_id)
    else:
        form = InstructionForm(instance=instruction)
    return render(request, 'recipes/instruction_edit.html', {'form': form})

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
