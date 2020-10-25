from django.contrib import admin

from .models import (FollowRecipe, FollowUser, Ingredients, Recipe,
                     RecipeIngre, ShoppingList, Tags, User)


class RecipeIngreInline(admin.TabularInline):
    model = RecipeIngre
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngreInline,)


class IngredientsAdmin(admin.ModelAdmin):
    inlines = (RecipeIngreInline,)


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
admin.site.register(RecipeIngre)
admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(FollowUser)
admin.site.register(FollowRecipe)
admin.site.register(ShoppingList)
