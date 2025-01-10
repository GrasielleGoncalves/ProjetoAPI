from django.contrib import admin
from .models import Usuario, Livro, Emprestimo

class Usuario_Admin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'papel')
    list_display_links = ('nome', 'telefone')
    list_per_page = 10
    search_fields = ('autor', 'genero','data_publicacao ', 'isbn','descricao')

admin.site.register(Usuario, Usuario_Admin)

class Livro_Admin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'genero', 'data_publicacao', 'isbn', 'descricao')
    list_display_links = ('titulo', 'autor')
    list_per_page = 10
    search_fields = ('titulo', 'autor', 'genero','data_publicacao ', 'isbn','descricao')

admin.site.register(Livro, Livro_Admin)

class Emprestimo_Admin(admin.ModelAdmin):
    list_display = ('livro', 'usuario', 'data_devolucao', 'status')
    list_display_links = ('livro', 'usuario')
    list_per_page = 10
    search_fields = ('livro', 'usuario', 'data_devolucao', 'status')

admin.site.register(Emprestimo,Emprestimo_Admin)