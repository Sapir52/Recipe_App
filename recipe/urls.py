#-----------------------------------------------
from django.conf.urls import url
from . import views
app_name = 'recipe'
urlpatterns = [
    # /recipe/register
    url(r'^register/$', views.UserRegister.as_view(), name = 'register'),
    # /recipe/logout
    url(r'^logout/$', views.Logout, name="logout"),
    # /recipe/login
    url(r'^login/$', views.UserLogin.as_view(), name="login"),
    #-------------------------------------------------------------------------------
    # /recipe/book
    url(r'^book$', views.IndexView.as_view(), name = 'index'),
    # /recipe/book/<book_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
    # /recipe/book/add/
    url(r'book/add/$', views.BookCreate.as_view(), name = 'book-add'),
    # /recipe/book/<book_id>/update
    url(r'book/(?P<pk>[0-9]+)/update/$', views.BookUpdate.as_view(), name = 'book-update'),
    # /recipe/book/<recipe_id>/delete/update
    url(r'book/(?P<pk>[0-9]+)/delete/$', views.BookDelete.as_view(), name = 'book-delete'),
    #-------------------------------------------------------------------------------
     # /recipe/recipes/<recipe_id>/update
    url(r'recipes/(?P<pk>[0-9]+)/update/$', views.RecipeUpdate.as_view(), name = 'recipe-update'),
    # /recipe/recipes/<recipe_id>/add
    url(r'recipes/add/$', views.RecipeCreate.as_view(), name="recipe-add"),
    # /recipe/recipes/<recipe_id>/delete
    url(r'recipes/(?P<pk>[0-9]+)/delete/$', views.RecipeDelete.as_view(), name="recipe-delete"),
    # /recipe/recipes/<book_id>/favorite
    url(r'recipes/(?P<pk>[0-9]+)/favorite/$', views.RecipeFavorite, name="recipe-favorite"),
    # /recipe/recipes
    url(r'recipes/$', views.RecipeListView.as_view(), name='recipes'),
    #/recipe/recipes/search
    url(r'recipes/search/$', views.SearchView.as_view(), name='search'),
    #/recipe/recipes/feedback
    url(r'recipes/feedback/$', views.Feedback_form, name='feedback'),
    #/recipe/recipes/search/feedback/views
    url(r'recipes/feedback/views/$', views.FeedbackView.as_view(), name = 'feedback_show'),

]

#-----------------------------------------------
