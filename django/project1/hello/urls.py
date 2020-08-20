from django.urls import path
from . import views
#lista de todos os urls que podem ser acessados
 
urlpatterns = [
    path("", views.index, name="index/hello"),
    path("<str:name>", views.greet, name="greet")
]