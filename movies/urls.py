from django.urls import path
from.views import ActorsView
from.views import MoviesView
urlpatterns = [
path('/act',ActorsView.as_view()),
path('/mov',MoviesView.as_view()),
]

