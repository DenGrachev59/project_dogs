from django.urls import path

from dogs.apps import DogsConfig
from dogs.views import index, CategoryListView, DogListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, \
   DogCreateView, DogUpdateView, DogDeleteView

app_name = DogsConfig.name

urlpatterns = [
   path('', index, name='index'),
   # path('categories/', categories, name='categories'),
   path('categories/', CategoryListView.as_view(), name='categories'),
   path('<int:pk>/dogs/', DogListView.as_view(), name='dog_list'),
   # path('<int:pk>/dogs/', CategoryCreateView.as_view(), name='category_create'),
   # path('<int:pk>/dogs/', CategoryUpdateView.as_view(), name='category_update'),
   # path('<int:pk>/dogs/', CategoryDeleteView.as_view(), name='category_delete'),
   path('<int:pk>dogs/create/', DogCreateView.as_view(), name='dog_create'),
   path('<int:pk>/dogs/update', DogUpdateView.as_view(), name='dog_update'),
   path('<int:pk>/dogs/delete', DogDeleteView.as_view(), name='dog_delete'),

]