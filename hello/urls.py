from django.urls import path #caminho
from . import views


app_name = 'hello'
urlpatterns = [
    path('',views.index, name='index'),#pasta com a funçao declarada
    #path('<int:question_id>/',views.detail, name='detail'),
    path('<int:question_id>/results/',views.results, name='results'),
    path('<int:question_id>/vote/',views.vote, name='vote')
]
