from django.contrib import admin

from .models import Recipe, Ingredient, Instruction
models = [Recipe, Ingredient, Instruction]

admin.site.register(models)
