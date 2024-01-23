from django.shortcuts import get_object_or_404, render
from datetime import datetime
# Create your views here.
from django.shortcuts import render, redirect
from .models import Medcine,Patient,Facture,Dossier_Medicale,Taches
from .forms import LoginForm, PatientForm,MedcineForm,Rendez_Vous,RendezVousForm,FactureForm,DosierForm,TachesForm

######################gestion patient #############################################
def add_patient(request): 
    patients = Patient.objects.all().values()  
    fields = ['NSS', 'NOM','PRENOM', 'TYPE_GROUPAGE', 'ADRESSE']  
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            mssg="commande envoyée, vous pouvez saisir une autre"
            context = {'patients': patients, 'fields': fields}
            return render(request, 'list_patient.html',context)  
    else:
        form = PatientForm()
    context = {'patients': patients, 'fields': fields,'form':form}
    return render(request, 'add_patient.html', context)
def delete_patient(request, patient_NSS):
    patients = Patient.objects.all().values()
    patient = get_object_or_404(Patient, NSS=patient_NSS)
    patient.delete()
    fields = ['NSS', 'NOM','PRENOM', 'TYPE_GROUPAGE', 'ADRESSE']  
    context = {'patients': patients, 'fields': fields}
    return render(request, 'list_patient.html', context)
def patient_list(request):
    patients = Patient.objects.all().values()  
    fields = ['NSS', 'NOM','PRENOM', 'TYPE_GROUPAGE', 'ADRESSE']  
    context = {'patients': patients, 'fields': fields}
    return render(request, 'list_patient.html', context)

####################gestion medcine ################################################
def add_medcine(request):
    doctors = Medcine.objects.all().values() 
    fields = ['id', 'NOM', 'PRENOM', 'Specialite', 'Email', 'Adresse', 'Departement_id']  
    
    if request.method == 'POST':
        form = MedcineForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            context = {'doctors': doctors, 'fields': fields}
            mssg="commande envoyée, vous pouvez saisir une autre"
            return render(request, 'list_medcin.html', context) 
    else:
        form = MedcineForm()
    context = {'doctors': doctors, 'fields': fields,'form':form}
    return render(request, 'add_medcine.html', context)
def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(Medcine, id=doctor_id)
    doctor.delete()
    return redirect('list_medcin')
def doctor_list(request):
    doctors = Medcine.objects.all().values() 
    fields = ['id', 'NOM', 'PRENOM', 'Specialite', 'Email', 'Adresse', 'Departement_id']  
    context = {'doctors': doctors, 'fields': fields}
    return render(request, 'list_medcin.html', context)
def login_medcin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            your_id = form.cleaned_data['your_id']
            your_name = form.cleaned_data['your_name']
            medcin_entry = Medcine.objects.filter(id=your_id, NOM=your_name).first()

            if medcin_entry:
                return redirect('list_dossier',doctor_id=your_id)
            else:
                form = LoginForm()
                return render(request, 'login.html', {'form': form})

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
######################### gestion Facture #################################
def add_facture(request):
    facture = Facture.objects.all().values()  
    fields = ['id','Remarques','Total'] 
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            taches_selectionnees = form.cleaned_data['taches']
            prix_total = sum(tache.prix for tache in taches_selectionnees)
            form.save ()
            derniere_facture = Facture.objects.latest('id')
            factur = Facture.objects.get(pk=derniere_facture.id)
            factur.Total = prix_total
            factur.save()
            facture = Facture.objects.all().values() 
            context = {'factuer': facture, 'fields': fields}
            return render(request, 'list_facture.html', context) 
    else:
        form =FactureForm()
    context = {'facture': facture, 'fields': fields,'form':form}
    return render(request, 'add_facture.html', context)
def facture_list(request):
    facture = Facture.objects.all().values()  
    fields = ['id','Remarques', 'Total'] 
    context = {'facture': facture, 'fields': fields}
    return render(request, 'list_facture.html', context)
################################ rendez_vous ###########################################
def add_rendez_vous(request):
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
           date = form.cleaned_data['date']
           time = form.cleaned_data['time']
           date_time = datetime.combine(date, time)
           if date_time > datetime.now():
            existing_appointment = Rendez_Vous.objects.filter(
                Date_Time_RendezV=date_time,
            ).exists()
            if not existing_appointment:
                instance = form.save(commit=False)
                instance.Date_Time_RendezV = date_time
                instance.save()
                form = RendezVousForm()
                return render(request, 'add_rendez_vous.html', {'form': form})  
            else:
                form.add_error(None, "exists une rendezvous dans cette data")
           else:
               form.add_error(None, "reglier la Data .")
    else: 
        form = RendezVousForm()
    return render(request, 'add_rendez_vous.html', {'form': form})

################### gestion taches ###################################
def add_taches(request):
    taches = Taches.objects.all().values() 
    fields = ['NOMT', 'Activities','prix'] 
    if request.method == 'POST':
        form = TachesForm(request.POST)
        if form.is_valid():
            form.save()
            mssg="commande envoyée, vous pouvez saisir une autre"
            context = {'taches': taches, 'fields': fields}
            return render(request, 'list_taches.html',context) 
    else:
        form = TachesForm()   
    context = {'taches': taches, 'fields': fields,'form':form}
    return render(request, 'add_taches.html', context)
def taches_list(request):
    taches = Taches.objects.all().values()  
    fields = ['NOMT', 'Activities','prix']  
    context = {'taches': taches, 'fields': fields}
    return render(request, 'list_taches.html', context)
def delete_taches(request, tache_id):
    taches = Taches.objects.all().values()
    tache = get_object_or_404(Taches, id=tache_id)
    tache.delete()
    fields = ['NOMT', 'Activities','prix'] 
    context = {'taches': taches, 'fields': fields}
    return render(request, 'list_taches.html', context)
######################### gestion dossier medical ##################################
def list_dossier(request,doctor_id):
    dossier_values=requpire(doctor_id)
    fields = ['id', 'patient', 'Antecedents_Medicaux', 'Antecedents_Familiaux', 'Prescriptions', 'Allergies', 'Traitements_En_Cours', 'Autres_Informations_Pertientes']
    context = {'dossiers': dossier_values, 'fields': fields,'doctor_id':doctor_id}
    return render(request, 'list_dossier.html', context)
def modify_dossier(request,dossier_id,doctor_id):
    dossiers =requpire(doctor_id)
    dossier_instance = get_object_or_404(Dossier_Medicale, id=dossier_id)
    fields = ['patient','Antecedents_Medicaux', 'Antecedents_Familiaux','Prescriptions', 'Allergies', 'Traitements_En_Cours','Autres_Informations_Pertientes']  
    if request.method == 'POST':
        form = DosierForm(request.POST,instance=dossier_instance)
        if form.is_valid():
            form.save()
            context = {'dossiers': dossiers, 'fields': fields,'doctor_id':doctor_id}
            return render(request, 'list_dossier.html',context) 
    else:
        dossier_instance = Dossier_Medicale.objects.get(id=dossier_id)
        form = DosierForm(instance=dossier_instance)
    context = {'dossiers': dossiers, 'fields': fields,'form':form}
    return render(request, 'modify_dossier.html', context)


############## fonction semplifer travaile ###################""
def requpire(doctor_id):
    rendezvous_list = Rendez_Vous.objects.filter(Medcine_id=doctor_id).select_related('Dossier')
    dossier_ids = [rendezvous.Dossier_id for rendezvous in rendezvous_list]
    dossiers = Dossier_Medicale.objects.in_bulk(dossier_ids) 
    
    dossier_values = [
        {
            'id': dossier.id,
            'patient': dossier.patient.NSS,
            'Antecedents_Medicaux': dossier.Antecedents_Medicaux,
            'Antecedents_Familiaux': dossier.Antecedents_Familiaux,
            'Prescriptions': dossier.Prescriptions,
            'Allergies': dossier.Allergies,
            'Traitements_En_Cours': dossier.Traitements_En_Cours,
            'Autres_Informations_Pertientes': dossier.Autres_Informations_Pertientes,
            
        }
        for dossier in dossiers.values()
    ]
    return dossier_values


