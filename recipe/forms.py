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


class RecipeIngreeForm(forms.ModelForm):
    class Meta:
        model = Recipe_Ingre
        fields = ("count",)
