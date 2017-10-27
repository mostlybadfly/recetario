from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    cuisine = models.CharField(max_length=50)
    cooking_time = models.IntegerField(null=True)
    servings = models.IntegerField(null=True)
    created_by = models.ForeignKey(User, related_name='recipes')

class Ingredient(models.Model):
    quantity = models.IntegerField(null=True)
    measurement = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, related_name='ingredients')

class Instruction(models.Model):
    ordinal = models.IntegerField(null=True)
    instruction_text = models.TextField(null=True)
    recipe = models.ForeignKey(Recipe, related_name='instructions')
