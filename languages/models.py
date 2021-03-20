from django.db import models

class mishra(models.Model):
    name = models.CharField(max_length= 50)
    paradigm  = models.CharField(max_length = 50)
   
        
    

    def __str__(self):
        return self.name

class Upload(models.Model):
    file_uploaded = models.FileField()

class Textfile(models.Model):
    file = models.CharField(max_length =50)


