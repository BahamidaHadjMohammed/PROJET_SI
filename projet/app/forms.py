from django import forms
from .models import Patient,Medcine,Rendez_Vous,Facture,Taches,Dossier_Medicale

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__' 
        
class MedcineForm(forms.ModelForm):
   class Meta:
       model = Medcine
       exclude = ['Specialite']  
       fields = '__all__'
       
class TachesForm(forms.ModelForm):
   class Meta:
       model = Taches
       fields = '__all__'    
                
class LoginForm(forms.Form):
    your_id = forms.IntegerField()  
    your_name = forms.CharField(max_length=30)    
       
class DosierForm(forms.ModelForm):
    class Meta:
        model=Dossier_Medicale
        exclude = ['Allergies','Antecedents_Familiaux','patient']
        fields = '__all__'

class FactureForm(forms.ModelForm):
    taches = forms.ModelMultipleChoiceField(queryset=Taches.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Facture
        exclude = ['Total','Taches']  
        fields = '__all__'  
                     

class RendezVousForm(forms.ModelForm):
    
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Rendez_Vous
        
        exclude = ['Date_Time_RendezV','Status_R','Salle']  
        fields= '__all__'
        
              