from django.db import models

class Employee(models.Model):       
    #Empcode = models.CharField(max_length=10, default='')
    Navn = models.CharField(max_length=150,null=True)
    Gruppe = models.CharField(max_length=100,null=True)    
    Morgen = models.CharField(max_length=100,null=True)
    Eftermiddag = models.CharField(max_length=30,null=True)
    Ferie = models.CharField(max_length=12, default='',null=True)
    #address = models.CharField(max_length=500, default='',null=True)     
    DOB = models.DateField(null=True, blank=True)   
    gender = models.CharField(max_length=5, default='',null=True)
    qualification = models.CharField(max_length=50,default='',null=True) 
    Alder = models.FloatField(max_length=50,default='',null=True)   
     
    def __str__(self):
        return self.Name
                 
    objects = models.Manager()
