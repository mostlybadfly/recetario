from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    cuisine = models.CharField(max_length=50)
    cooking_time = models.IntegerField(blank=True, null=True)
    servings = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='recipes')

class Ingredient(models.Model):
    quantity = models.IntegerField(blank=True, null=True)
    measurement = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, related_name='ingredients')

class Instruction(models.Model):
    ordinal = models.IntegerField(blank=True, null=True)
    instruction_text = models.TextField(null=True)
    recipe = models.ForeignKey(Recipe, related_name='instructions')
