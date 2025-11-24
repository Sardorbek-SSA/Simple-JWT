from django.urls import path
from .views import ToyListCreateView, ToyUpdateView
urlpatterns = [
    path('',ToyListCreateView.as_view()),
    path('<int:pk>/',ToyUpdateView.as_view()),
]
