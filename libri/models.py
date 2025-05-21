from django.db import models

class Libro(models.Model):
    titolo = models.CharField(max_length=100)
    autore = models.CharField(max_length=100)
    anno_pubblicazione = models.IntegerField()

    def __str__(self):
        return self.titolo
