from rest_framework import serializers
from .models import Usuario, Livro, Emprestimo

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class EmprestimoSerializer(serializers.ModelSerializer):
    livro = LivroSerializer(read_only=True)
    usuario = UsuarioSerializer(read_only=True)

    class Meta:
        model = Emprestimo
        fields = '__all__'

