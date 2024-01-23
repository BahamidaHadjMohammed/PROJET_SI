from django.urls import path
from .views import  add_patient,add_medcine,add_rendez_vous,delete_doctor
from .views import  doctor_list,add_facture,patient_list,delete_patient,facture_list,list_dossier
from .views import  modify_dossier,taches_list,add_taches,delete_taches,login_medcin

urlpatterns = [
    path('add_patient/', add_patient, name='add_patient'),
    path('add_facture/', add_facture, name='add_facture'),
    path('add_medcine/', add_medcine, name='add_medcine'),
    path('add_rendez_vous/',add_rendez_vous,name='add_rendez_vous'),
    path('list_medcin/',doctor_list , name='list_medcin'),
    path('delete_doctor/<int:doctor_id>/', delete_doctor, name='delete_doctor'),
    path('list_patient/',patient_list , name='list_patient'),
    path('delete_patient/<int:patient_NSS>/', delete_patient, name='delete_patient'),
    path('delete_taches/<int:tache_id>/', delete_taches, name='delete_taches'),
    path('list_facture/',facture_list , name='list_facture'),
    path('list_dossier/<int:doctor_id>/',list_dossier,name='list_dossier'),
    path('modify_dossier/<int:dossier_id>/<int:doctor_id>/',modify_dossier,name='modify_dossier'),
    path('add_tache/',add_taches,name='add_tache'),
    path('list_tache/',taches_list , name='taches_list'),
    path('login/',login_medcin,name='login')
   
    
]