from django.contrib import admin
from .models import *
from .forms import *


# class RecipeAdmin(admin.ModelAdmin):
#    form = TagForm


class Recipe_IngreInline(admin.TabularInline):
    model = Recipe_Ingre
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = (Recipe_IngreInline,)


class IngredientsAdmin(admin.ModelAdmin):
    inlines = (Recipe_IngreInline,)


class TagsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "color",
        "name",
    )
    search_fields = ("title",)
    list_filter = ("title",)
    empty_value_display = "-пусто-"


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Recipe_Ingre)
admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(FollowUser)
admin.site.register(FollowRecipe)
admin.site.register(ShoppingList)
