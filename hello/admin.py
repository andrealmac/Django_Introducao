from django.contrib import admin

#Trazer as informacoes do banco de dados para a pagina admin
from .models import Question
admin.site.register(Question)
