from django import forms

from .models import Recipe, Ingredient, Instruction

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('title', 'cuisine', 'cooking_time', 'servings')

class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ('quantity', 'measurement', 'name')

class InstructionForm(forms.ModelForm):

    class Meta:
        model = Instruction
        fields = ('ordinal', 'instruction_text')

