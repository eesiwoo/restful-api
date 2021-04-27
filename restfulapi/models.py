from django.db import models

class Movies(models.Model) :
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    myData = models.CharField(max_length=200)

    def __str__(self):
        return self.title