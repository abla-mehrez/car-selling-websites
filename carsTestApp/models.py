from decimal import Decimal
from django.db import models
from tkinter import CASCADE

from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


# Create your models here.



# Create your models here.
class User(AbstractUser):
  is_client=models.BooleanField(default=False)
  is_expert=models.BooleanField(default=False)
class Expert(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='expert_user')
  first_name=None
  last_name=None
  notifie=models.BooleanField(default=False)
  # nbre_notification=models.IntegerField(default=0,null=True,blank=True)
  nom=models.CharField(max_length=50,unique=True)
  prenom=models.CharField(max_length=50)
  adresse_mail=models.EmailField(max_length=500)
  ARIANA='Ariana'
  TUNIS='Tunis'
  BENAROUS='Ben Arous'
  MANOUBA='Manouba'
  BEJA='Beja'
  BIZERTE='Bizerte'
  GABES='Gabes'
  GAFSA='Gafsa'
  JENDOUBA='Jendouba'
  KAIROUAN='Kairouan'
  KASSERINE='Kasserine'
  KEBILI='Kebili'
  KEF='Kef'
  MAHDIA='Mahdia'
  MEDENINE='Medenine'
  MONASTIR='Monastir'
  NABEUL='Nabeul'
  SFAX='Sfax'
  SIDIBOUZID='Sidi Bouzid'
  SILIANA='Siliana'
  SOUSSE='Sousse'
  TATAOUINE='Tataouine'
  TOUZEUR='Tozeur'
  ZAGHOUAN='Zaghouan'
  REGION=[(ARIANA,'Ariana'),(TUNIS,'Tunis'),(BENAROUS,'Ben Arous'),(MANOUBA,'Manouba'),(BEJA,'Beja'),(BIZERTE,'Bizerte'),(GABES,'Gabes'),(GAFSA,'Gafsa'),(JENDOUBA,'Jendouba'),(KAIROUAN,'Kairouan'),(KASSERINE,'Kasserine'),(KEBILI,'Kebili'),(KEF,'Kef'),(MAHDIA,'Mahdia'),(MEDENINE,'Medenine'),(MONASTIR,'Monastir'),(NABEUL,'Nabeul'),(SFAX,'Sfax'),(SIDIBOUZID,'Sidi Bouzid'),(SILIANA,'Siliana'),(SOUSSE,'Sousse'),(TATAOUINE,'Tataouine'),(TOUZEUR,'Tozeur'),(ZAGHOUAN,'Zaghouan')]
  region=models.CharField(max_length=20,choices=REGION,default=TUNIS)
  photo=models.ImageField(upload_to='cars/fichierExpert/photos')
  numero_de_téléphone = PhoneNumberField(blank=True)
  def __str__(self):
        return self.nom + self.prenom
  
class Client(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True) 
  name=models.CharField(max_length=40,default=None)
class Bilan_expert(models.Model):
  active=models.BooleanField(default=False)
  prix_suggéré=models.FloatField(default=0)
  note= models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0), validators=PERCENTAGE_VALIDATOR)
  batterie_cmd_electronique=models.CharField(max_length=200)
  tableau_de_bord_alertes_temoins_allumes=models.CharField(max_length=200)
  moteur_niveaux=models.CharField(max_length=200)
  fixation=models.CharField(max_length=200)
  courroies_accessoires=models.CharField(max_length=200)
  boite_vitesse_embrayage=models.CharField(max_length=200)
  echappement_pollution=models.CharField(max_length=200)
  identification=models.CharField(max_length=200)
  vision_eclairage_avertisseur_sonore=models.CharField(max_length=200)
  direction=models.CharField(max_length=200)
  train=models.CharField(max_length=200)
  transmission_roulement=models.CharField(max_length=200)
  jantes_pneus=models.CharField(max_length=200)
  freinage=models.CharField(max_length=200)
  suspension=models.CharField(max_length=200)
  infrastructure=models.CharField(max_length=200)
  aspect_carrosserie=models.CharField(max_length=200)
  interieur=models.CharField(max_length=200)
  clim_chauffage=models.CharField(max_length=200)
  essai_routier=models.CharField(max_length=200)
  commentaire=models.TextField()
  expert=models.ForeignKey(Expert,on_delete=models.CASCADE,default=None,related_name='exp')
  def __str__(self):
        return self.commentaire

class Offre(models.Model):
  matricule=models.CharField(max_length=30,unique=True)
  marque=models.CharField(max_length=30)
  couleur=models.CharField(max_length=30)
  region=models.CharField(max_length=40)
  puissance=models.CharField(max_length=10)
  cylindres=models.FloatField(default=0)
  kilometrage=models.FloatField(default=0)
  Automatique='auto'
  Manuelle='manuelle'
  TRANSMISSION=[(Automatique,'Auto'),(Manuelle,'manuelle')]
  transmission=models.CharField(max_length=20,choices=TRANSMISSION)
  carburant=models.CharField(max_length=30)
  annee=models.IntegerField(default=2000,verbose_name="année")
  image=models.ImageField(upload_to='cars/fichier/images',blank=True)
  prix_propose=models.FloatField(default=0)
  prix_enchere=models.FloatField(default=0,blank=True)
  vendeur=models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=True,blank=True,related_name='vendeur_offre')
  expert=models.ForeignKey(Expert,on_delete=models.CASCADE,default=None,null=True,blank=True,related_name='exp_offre')
  bilan=models.OneToOneField(Bilan_expert,on_delete=models.CASCADE,null=True,blank=True,related_name='voiture_associée')
  def __str__(self):
        return self.matricule
class Commentaire(models.Model):
  contenu=models.TextField()
  cree_le = models.DateTimeField(auto_now_add=True)
  modifie_le = models.DateTimeField(auto_now=True)
  acheteur=models.ForeignKey(User,on_delete=models.CASCADE)
  offre=models.ForeignKey(Offre,related_name="comments",on_delete=models.CASCADE)
  def __str__(self):
        return self.contenu 
        
class Notification(models.Model):
  ident=models.IntegerField(default=100)
  exp_not=models.ForeignKey(Expert,on_delete=models.CASCADE,default=None,related_name='exp_notification')
  client_not=models.ForeignKey(User,on_delete=models.CASCADE,default=None,related_name='client_notification')
  number=models.IntegerField(default=0)
  def __str__(self):
    return f'{self.ident}  {self.exp_not} {self.client_not} {self.number}'