from .serializers import LivroSerializer, UsuarioSerializer, EmprestimoSerializer
from .models import Livro, Usuario, Emprestimo
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class Livro_viewSet(viewsets.ModelViewSet):
    authention_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = LivroSerializer

    def get_queryset(self):
        queryset = Livro.objects.all()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome=nome)

        return queryset

class Usuario_viewSet(viewsets.ModelViewSet):
    authention_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Livro.objects.all()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome=nome)

        return queryset

class Emprestimo_viewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated] 
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer


    def get_queryset(self):
        livro_id = self.request.query_params.get("livro")
        usuario_id = self.request.query_params.get("usuario")
        queryset = self.queryset
        if livro_id:
            queryset = queryset.filter(livro_id=livro_id)
        if usuario_id:
            queryset = queryset.filter(usuario_id=usuario_id)
        return queryset
