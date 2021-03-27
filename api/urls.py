from django.urls import path

from api import views

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello'),
    path('create-team/', views.add_team, name='api_add_team'),
    path('notify-team/', views.notify_team, name='api_add_team'),

]