from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField (max_length=200) #stands for character field (google Django datatypes)
    language = models.CharField (max_length=100)
    price = models.CharField (max_length=10) #olden times compute space is limited

    def __str__(self): #need space after DEFINE
        return self.name #just the name on top