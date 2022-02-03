from django.db import models
from django.urls import reverse 
from django.forms import ModelForm
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    category_slug = models.SlugField(max_length=69, unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("list", args=[self.id])

class Negocio(models.Model):
    title = models.CharField(max_length=255)
    negocio_slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, related_name="negocios", on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='uploads/', blank=True, null=True)
    description = models.TextField()
    
    def __str__(self):
        return self.title

    

    

   
class Contacto(models.Model):
    name = models.CharField(max_length=150)
    mail = models.EmailField(blank=True, max_length=254)
    subject = models.CharField(max_length=150)
    description = models.TextField()
    created = models.DateTimeField(default=datetime.datetime.now, blank=True,null=True)


    def __str__(self):
        return self.name
