from django import forms

from .models import Recipe, Ingredient

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('title', 'cuisine', 'cooking_time', 'servings')

class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ('quantity', 'measurement', 'name')
