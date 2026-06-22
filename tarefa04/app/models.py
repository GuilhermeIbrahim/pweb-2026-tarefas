from django.db import models

# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    conclusion_date = models.DateTimeField()
    COMPLETO = "CO"
    ANDAMENTO = "AN"
    STATUS = {
        COMPLETO: "Completo",
        ANDAMENTO: "Andamento",
    }
    status = models.CharField(max_length=2, choices=STATUS, default=ANDAMENTO)
    
    def __str__(self):
        return self.text 