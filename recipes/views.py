from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, IngredientForm, InstructionForm, IngredientFormSet, InstructionFormSet
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.db import transaction

from .models import Recipe, Ingredient, Instruction

class RecipeCreate(CreateView):
    model = Recipe
    form_class = RecipeForm

    def get_success_url(self):
        return reverse_lazy('detail', args = (self.object.id,))

    def get_context_data(self, **kwargs):
        data = super(RecipeCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['ingredients'] = IngredientFormSet(self.request.POST, prefix='ingredients')
            data['instructions'] = InstructionFormSet(self.request.POST, prefix='instructions')
        else:
            data['ingredients'] = IngredientFormSet()
            data['instructions'] = InstructionFormSet()
        return data

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        context = self.get_context_data()
        ingredients = context['ingredients']
        instructions = context['instructions']
        with transaction.atomic():
            if form.is_valid() and ingredients.is_valid() and instructions.is_valid():
                self.object = form.save()
                ingredients.instance = self.object
                instructions.instance = self.object
                ingredients.save()
                instructions.save()
        return super(RecipeCreate, self).form_valid(form)

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['title', 'cuisine', 'cooking_time', 'servings']

    def get_success_url(self):
        return reverse_lazy('detail', args = (self.object.id,))

    def get_context_data(self, **kwargs):
        data = super(RecipeUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['ingredients'] = IngredientFormSet(self.request.POST, instance=self.object, prefix='ingredients')
            data['instructions'] = InstructionFormSet(self.request.POST, instance=self.object, prefix='instructions')
        else:
            data['ingredients'] = IngredientFormSet(instance=self.object)
            data['instructions'] = InstructionFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        ingredients = context['ingredients']
        instructions = context['instructions']
        with transaction.atomic():
            if form.is_valid() and ingredients.is_valid() and instructions.is_valid():
                self.object = form.save()
                ingredients.instance = self.object
                instructions.instance = self.object
                ingredients.save()
                instructions.save()
        return super(RecipeUpdate, self).form_valid(form)

def index(request):
    recipe_list = Recipe.objects.all()
    context = {'recipe_list': recipe_list}
    return render(request, 'recipes/index.html', context)

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    ingredients = recipe.ingredients.all()
    instructions = recipe.instructions.all()
    return render(request, 'recipes/detail.html',
                  {'recipe': recipe, 'ingredients': ingredients, 'instructions': instructions})

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
