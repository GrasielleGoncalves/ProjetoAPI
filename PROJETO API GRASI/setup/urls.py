from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from biblioteca.views import Livro_viewSet, Usuario_viewSet, Emprestimo_viewSet

router = routers.DefaultRouter()
router.register("livros", Livro_viewSet, basename="livros")
router.register("usuarios", Usuario_viewSet, basename="usuarios")
router.register("emprestimos", Emprestimo_viewSet, basename="emprestimos")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    ]


