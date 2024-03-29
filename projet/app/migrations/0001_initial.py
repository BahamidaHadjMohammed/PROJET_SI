# Generated by Django 5.0 on 2024-01-19 16:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOMD', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('NSS', models.IntegerField(primary_key=True, serialize=False)),
                ('NOM', models.CharField(max_length=30)),
                ('PRENOM', models.CharField(max_length=30)),
                ('DATE_NAISSANCE', models.DateField()),
                ('TYPE_GROUPAGE', models.CharField(max_length=50)),
                ('ADRESSE', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Medcine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOM', models.CharField(max_length=30)),
                ('PRENOM', models.CharField(max_length=30)),
                ('Specialite', models.CharField(default='', max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('Adresse', models.CharField(max_length=30)),
                ('Departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.departement')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dossier_Medicale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Antecedents_Medicaux', models.CharField(max_length=60)),
                ('Antecedents_Familiaux', models.CharField(max_length=60)),
                ('Prescriptions', models.CharField(max_length=60)),
                ('Allergies', models.CharField(max_length=60)),
                ('Traitements_En_Cours', models.CharField(max_length=60)),
                ('Autres_Informations_Pertientes', models.CharField(max_length=60)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Rendez_Vous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Time_RendezV', models.DateTimeField()),
                ('Type_R', models.CharField(max_length=30)),
                ('Salle', models.CharField(default='S01', max_length=20)),
                ('Status_R', models.CharField(default='confirme', max_length=20)),
                ('Remarques', models.CharField(max_length=100)),
                ('Dossier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dossier_medicale')),
                ('Medcine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medcine')),
            ],
        ),
        migrations.CreateModel(
            name='Taches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOMT', models.CharField(max_length=30)),
                ('Activities', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.departement')),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Remarques', models.CharField(max_length=100)),
                ('Total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('Rendez_Vous', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.rendez_vous')),
                ('Taches', models.ManyToManyField(to='app.taches')),
            ],
        ),
    ]
