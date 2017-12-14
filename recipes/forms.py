from django.forms import ModelForm, inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div

from .models import Recipe, Ingredient, Instruction

class RecipeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_show_labels = False
        self.helper.layout = Layout (
            Div(Field('title', placeholder="Title"), css_class='col-md-5'),
            Div(Field('cuisine', placeholder="Cuisine"), css_class='col-md-3'),
            Div(Field('cooking_time', placeholder="Cooking Time"), css_class='col-md-2'),
            Div(Field('servings', placeholder="Servings"), css_class='col-md-2'),
        )

    class Meta:
        model = Recipe
        fields = ('title', 'cuisine', 'cooking_time', 'servings')

class IngredientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(IngredientForm, self).__init__(*args, **kwargs)
        self.helper = FormSetHelper()
        self.helper.layout = Layout (
            Div(Field('quantity', placeholder="Quantity"), css_class='col-md-2'),
            Div(Field('measurement', placeholder="Measurement"), css_class='col-md-2'),
            Div(Field('name', placeholder="Name", size=45), css_class='col-md-7')
        )

    class Meta:
        model = Ingredient
        fields = ('quantity', 'measurement', 'name')

class InstructionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(InstructionForm, self).__init__(*args, **kwargs)
        self.helper = FormSetHelper()
        self.helper.layout = Layout (
            Div(Field('ordinal', placeholder="Position", readonly=True), css_class='col-md-1'),
            Div(Field('instruction_text', placeholder="Add a Step", rows=1, cols=75), css_class='col-md-10')
        )

    class Meta:
        model = Instruction
        fields = ('ordinal', 'instruction_text')

class FormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(FormSetHelper, self).__init__(*args, **kwargs)
        self.form_tag = False
        self.render_hidden_fields = True
        self.disable_csrf = True
        self.form_show_labels = False


IngredientFormSet = inlineformset_factory(Recipe, Ingredient, form = IngredientForm, extra=1)
InstructionFormSet = inlineformset_factory(Recipe, Instruction, form = InstructionForm, extra=1)
