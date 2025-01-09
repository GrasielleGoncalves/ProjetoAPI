from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    papel = models.CharField(max_length=20,choices=(("administrador", "Administrador"), ("leitor", "Leitor")),default="leitor"
    ) 

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    genero = models.CharField(max_length=100)
    data_publicacao = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    descricao = models.TextField()

def _str_(self):
        return self.titulo

class Emprestimo(models.Model):
    STATUS_CHOICES = (("pendente", "Pendente"), ("devolvido", "Devolvido"))

    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name="emprestimos")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="emprestimos")
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pendente")