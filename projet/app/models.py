from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    NSS=models.IntegerField(primary_key=True)
    NOM=models.CharField(max_length=30)
    PRENOM=models.CharField(max_length=30)
    DATE_NAISSANCE=models.DateField()
    TYPE_GROUPAGE=models.CharField(max_length=50)
    ADRESSE=models.CharField(max_length=30)
class Dossier_Medicale(models.Model):
      Antecedents_Medicaux=models.CharField(max_length=60)
      Antecedents_Familiaux=models.CharField(max_length=60)
      Prescriptions=models.CharField(max_length=60)
      Allergies=models.CharField(max_length=60)
      Traitements_En_Cours=models.CharField(max_length=60)
      Autres_Informations_Pertientes=models.CharField(max_length=60)
      patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
class Departement(models.Model):
    NOMD=models.CharField(max_length=30)     
class Medcine(models.Model):
     
     NOM=models.CharField(max_length=30)
     PRENOM=models.CharField(max_length=30)   
     Specialite=models.CharField(max_length=30,default='')
     Email=models.CharField(max_length=30)
     Adresse=models.CharField(max_length=30)
     Departement=models.ForeignKey(Departement,on_delete=models.CASCADE)  
class Taches(models.Model):
    NOMT=models.CharField(max_length=30) 
    Activities=models.CharField(max_length=100)
    prix=models.DecimalField(max_digits=10, decimal_places=2)
    Departement=models.ForeignKey(Departement,on_delete=models.CASCADE)  
    
class Rendez_Vous(models.Model):
     Date_Time_RendezV=models.DateTimeField() 
     Type_R=models.CharField(max_length=30)
     Salle=models.CharField(max_length=20,default='S01')
     Status_R=models.CharField(max_length=20,default='confirme')
     Remarques=models.CharField(max_length=100)
     Medcine=models.ForeignKey(Medcine,on_delete=models.CASCADE)
     Dossier=models.ForeignKey(Dossier_Medicale,on_delete=models.CASCADE)  
class Facture(models.Model):
    Remarques=models.CharField(max_length=100)
    Total=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    Taches=models.ManyToManyField(Taches)
    Rendez_Vous = models.OneToOneField(Rendez_Vous, on_delete=models.CASCADE)
    
    
    
        
        
        
    
