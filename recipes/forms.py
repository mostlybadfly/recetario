from django.forms import ModelForm, inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

from .models import Recipe, Ingredient, Instruction

class RecipeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'

    class Meta:
        model = Recipe
        fields = ('title', 'cuisine', 'cooking_time', 'servings')

class IngredientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(IngredientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.form_tag = False
        self.helper.render_hidden_fields = True
        self.helper.disable_csrf = True
        self.helper.form_show_labels = False
        self.helper.layout = Layout (
            Field('quantity', placeholder="Quantity"),
            Field('measurement', placeholder="Measurement"),
            Field('name', placeholder="Name")
        )

    class Meta:
        model = Ingredient
        fields = ('quantity', 'measurement', 'name')

class InstructionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(InstructionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.render_hidden_fields = True
        self.helper.disable_csrf = True
        self.helper.form_show_labels = False
        self.helper.layout = Layout (
            Field('ordinal', placeholder="Position"),
            Field('instruction_text', placeholder="Add a Step"),
        )

    class Meta:
        model = Instruction
        fields = ('ordinal', 'instruction_text')

IngredientFormSet = inlineformset_factory(Recipe, Ingredient, form = IngredientForm, extra=1)
InstructionFormSet = inlineformset_factory(Recipe, Instruction, form = InstructionForm, extra=1)
