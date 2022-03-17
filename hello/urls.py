from django.urls import path #caminho
from . import views

urlpatterns = [
    path('',views.hello)#pasta com a funçao declarada
]
