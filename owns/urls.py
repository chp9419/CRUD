from django.urls import path
from.views import OwnsListView
from.views import DogsListView
urlpatterns = [
    path('/s',OwnsListView.as_view()),
    path('/a',DogsListView.as_view()),

  
]


