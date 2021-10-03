from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:Post_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:Post_id>/current_number/', views.results, name='current_number'),
    # ex: /polls/5/vote/
    path('<int:Post_id>/postal_code/', views.vote, name='postal_code'),
]