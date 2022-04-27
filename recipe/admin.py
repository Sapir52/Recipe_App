from django.contrib import admin

# Register your models here.
#----------------------------------
from .models import Book, Recipe, Feedback
admin.site.register(Book)
admin.site.register(Recipe)
admin.site.register(Feedback)
#----------------------------------