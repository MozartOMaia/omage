from django.db import models

# Create your models here.
class Card(models.Model):
    texto = models.CharField(max_length=250, null=True)
    assinatura = models.CharField(max_length=250)    
    pub_date = models.DateTimeField('data de publicacao')
    image = models.ImageField()

    def __str__(self):
        return self.assinatura