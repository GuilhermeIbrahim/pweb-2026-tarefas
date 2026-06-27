from django.db import models
from datetime import date


class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    prazo = models.DateField()
    concluida = models.BooleanField(default=False)

    @property
    def status(self):
        if self.concluida:
            return "Concluída"
        elif self.prazo < date.today():
            return "Pendente/Atrasada"
        return "Em andamento"

    @property
    def atrasada(self):
        return not self.concluida and self.prazo < date.today()

    def __str__(self):
        return self.nome