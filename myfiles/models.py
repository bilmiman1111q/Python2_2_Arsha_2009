from django.db import models
# Create your models here.
class Type(models.Model):
    nomi = models.CharField(max_length=30)
    def __str__(self):
        return self.nomi

class Portfoliyo(models.Model):
    nomi = models.CharField(max_length=30)
    company_name = models.CharField(max_length=50)
    date = models.DateField()
    url = models.URLField()
    malumot = models.TextField()
    tur = models.ForeignKey(Type, on_delete=models.CASCADE)
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media',null=True, blank=True)
    rasm3 = models.ImageField(upload_to='media',null=True, blank=True)


class Servise(models.Model):
    nomi = models.CharField(max_length=30)
    malumot = models.TextField()
    rasm1 = models.ImageField(upload_to='media')


class Team(models.Model):
    ismi = models.CharField(max_length=30)
    malumot = models.TextField()
    lavozimi = models.CharField(max_length=50)
    fecebook_link = models.CharField(max_length=40)
    instgram_link = models.CharField(max_length=40)
    tik_tok_link = models.CharField(max_length=40)
    yutube_link = models.CharField(max_length=40)
    rasm1 = models.ImageField(upload_to='media')


class Murojaat(models.Model):
    name = models.CharField(max_length=30)
    mail = models.EmailField(max_length=40)
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateField()



class Email(models.Model):
    email = models.EmailField(max_length=40)

