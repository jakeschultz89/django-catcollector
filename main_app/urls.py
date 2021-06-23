from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='cats_index'),
    path('cats/<int:cat_id>/', views.cats_show, name='cats_show')
]

# when thinking about making a webpage inside of Django
# 1. create a function
# 2. create your html page
# 3. create a path inside of urls.py (main_app.py)