from django import forms
from .models import *
from django.forms import ModelForm


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            "title",
            "tag",
            "time",
            "description",
            "image",
        )
        widgets = {
            "tag": forms.CheckboxSelectMultiple(),
        }


# class RecipeForm(forms.ModelForm):
#     class Meta:
#         model = Recipe
#         fields = ('title', 'image', 'tag', 'description', 'time')


class RecipeIngreeForm(forms.ModelForm):
    class Meta:
        model = Recipe_Ingre
        fields = ("count",)


# TAG_CHOICES = (
#         ('завтрак', 'завтрак'),
#         ('обед', 'обед'),
#         ('ужин', 'ужин'),

#     )
