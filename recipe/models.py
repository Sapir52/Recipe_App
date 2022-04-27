from django.db import models
from django.urls import reverse

#-------------------------------------------------
class Book(models.Model):
    book_logo = models.CharField(max_length = 1000)
    artist = models.CharField(max_length = 250)
    book_title = models.CharField(max_length = 500)
    genre = models.CharField(max_length = 100)
   
    def get_absolute_url(self):
        return reverse('recipe:detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.book_title + ' - ' + self.artist

class Recipe(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    recipe_logo = models.CharField(max_length = 1000)
    recipe_title = models.CharField(max_length = 100)
    ingredient_recipe = models.CharField(max_length = 250)
    recipe_description = models.CharField(max_length = 500)
    is_favorite = models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return reverse('recipe:detail', kwargs={'pk': self.book.id})

    def __str__(self):
        return self.recipe_title
    
    
class Feedback(models.Model):
    user_name = models.CharField(max_length = 100)
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    details = models.TextField()

    def get_absolute_url(self):
        return reverse('recipe:feedback_index', kwargs={'pk': self.book.id})
    
    def __str__(self):
        return self.user_name + ' - ' + self.details
    
    
    
