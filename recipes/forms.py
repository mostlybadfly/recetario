from django.forms import ModelForm, inlineformset_factory

from .models import Recipe, Ingredient, Instruction

class RecipeForm(ModelForm):

    class Meta:
        model = Recipe
        fields = ('title', 'cuisine', 'cooking_time', 'servings')

class IngredientForm(ModelForm):

    class Meta:
        model = Ingredient
        fields = ('quantity', 'measurement', 'name')

class InstructionForm(ModelForm):

    class Meta:
        model = Instruction
        fields = ('ordinal', 'instruction_text')

IngredientFormSet = inlineformset_factory(Recipe, Ingredient, form = IngredientForm, extra = 2)
InstructionFormSet = inlineformset_factory(Recipe, Instruction, form = InstructionForm, extra = 2)
