from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Tags(models.Model):
    TAG_CHOICES = [
        ("breakfast", "Завтрак"),
        ("lunch", "Обед"),
        ("dinner", "Ужин"),
    ]
    title = models.CharField(max_length=10, choices=TAG_CHOICES)

    def __str__(self):
        return self.title

    @property
    def color(self):
        if self.title == "breakfast":
            return "orange"
        if self.title == "lunch":
            return "green"
        return "purple"

    @property
    def name(self):
        if self.title == "breakfast":
            return "Завтрак"
        if self.title == "lunch":
            return "Обед"
        return "Ужин"


class Ingredients(models.Model):
    title = models.CharField(max_length=300)
    dimension = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.title} {self.dimension}"


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    title = models.CharField(max_length=45)
    image = models.ImageField(upload_to="recipe/", blank=True, null=True)
    description = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    tag = models.ManyToManyField(Tags)
    ingredients = models.ManyToManyField(
        Ingredients, through="Recipe_Ingre", through_fields=("recipe", "ingredients")
    )
    time = models.CharField(max_length=45)

    def __str__(self):
        return self.title


class Recipe_Ingre(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    count = models.FloatField()

    def __str__(self):
        return f"{self.recipe}"


class FollowUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")

    def __str__(self):
        return self.user.username


class FollowRecipe(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower_recipe"
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="following_recipe"
    )

    def __str__(self):
        return f"user - {self.user} recipe - {self.recipe}"


class ShoppingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shop_list")
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="shop_list"
    )

    def __str__(self):
        return self.recipe.title
