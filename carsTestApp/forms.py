

from asyncio.windows_events import NULL
from contextlib import nullcontext
from django import forms
from dataclasses import fields

from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import  Offre,Commentaire,User,Bilan_expert

class Bilan_expertForm(forms.ModelForm):

  voiture_associée= forms.ModelChoiceField(queryset=None)
  def __init__(self, *args, **kwargs):
        user=kwargs.pop('user')
        super(Bilan_expertForm,self).__init__(*args, **kwargs)
        self.fields['voiture_associée'].queryset = Offre.objects.filter(expert_id=user.id,bilan_id__isnull=True ) 
  class Meta:
        model=Bilan_expert
        fields =['voiture_associée','note','prix_suggéré','batterie_cmd_electronique',
        'tableau_de_bord_alertes_temoins_allumes','moteur_niveaux',
        'fixation','courroies_accessoires','boite_vitesse_embrayage',
        'echappement_pollution','identification', 'vision_eclairage_avertisseur_sonore',
        'direction','train','transmission_roulement',
        'jantes_pneus','freinage','suspension','infrastructure',
        'aspect_carrosserie','interieur','interieur','clim_chauffage',
        'essai_routier','commentaire'] 
  
        widgets={
          
           'active':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'voiture_associée':forms.Select(attrs={'class':'form-select'}),
           'batterie_cmd_electronique' :forms.TextInput(attrs={'class':'form-control','placeholder':"batterie"}),
           'tableau_de_bord_alertes_temoins_allumes':forms.TextInput(attrs={'class':'form-control'}),
           'moteur_niveaux':forms.TextInput(attrs={'class':'form-control'}),
           'fixation':forms.TextInput(attrs={'class':'form-control'}),
           'courroies_accessoires':forms.TextInput(attrs={'class':'form-control'}),
           'boite_vitesse_embrayage':forms.TextInput(attrs={'class':'form-control'}),
           'echappement_pollution':forms.TextInput(attrs={'class':'form-control'}),
           'identification':forms.TextInput(attrs={'class':'form-control'}),
           'vision_eclairage_avertisseur_sonore':forms.TextInput(attrs={'class':'form-control'}),
           'direction':forms.TextInput(attrs={'class':'form-control'}),
           'train':forms.TextInput(attrs={'class':'form-control'}),
           'transmission_roulement':forms.TextInput(attrs={'class':'form-control'}),
           'jantes_pneus':forms.TextInput(attrs={'class':'form-control'}),
           'freinage':forms.TextInput(attrs={'class':'form-control'}),
           'suspension':forms.TextInput(attrs={'class':'form-control'}),
           'infrastructure':forms.TextInput(attrs={'class':'form-control'}),
           'aspect_carrosserie':forms.TextInput(attrs={'class':'form-control'}),
           'interieur':forms.TextInput(attrs={'class':'form-control'}),
           'clim_chauffage':forms.TextInput(attrs={'class':'form-control'}),
           'essai_routier':forms.TextInput(attrs={'class':'form-control'}),
           'commentaire':forms.Textarea(attrs={'class':'form-control'}),
       }
  



class Bilan_expert_update_Form(forms.ModelForm):
    
    class Meta:
        model=Bilan_expert
        fields =model=Bilan_expert
        fields =['batterie_cmd_electronique',
        'tableau_de_bord_alertes_temoins_allumes','moteur_niveaux',
        'fixation','courroies_accessoires','boite_vitesse_embrayage',
        'echappement_pollution','identification', 'vision_eclairage_avertisseur_sonore',
        'direction','train','transmission_roulement',
        'jantes_pneus','freinage','suspension','infrastructure',
        'aspect_carrosserie','interieur','interieur','clim_chauffage',
        'essai_routier','commentaire'
        ] 
        widgets={
           'active':forms.CheckboxInput(attrs={'class':'form-check-input'}),
           'voiture_associée':forms.Select(attrs={'class':'form-select'}),
           'batterie_cmd_electronique' :forms.TextInput(attrs={'class':'form-control','placeholder':"batterie"}),
           'tableau_de_bord_alertes_temoins_allumes':forms.TextInput(attrs={'class':'form-control'}),
           'moteur_niveaux':forms.TextInput(attrs={'class':'form-control'}),
           'fixation':forms.TextInput(attrs={'class':'form-control'}),
           'courroies_accessoires':forms.TextInput(attrs={'class':'form-control'}),
           'boite_vitesse_embrayage':forms.TextInput(attrs={'class':'form-control'}),
           'echappement_pollution':forms.TextInput(attrs={'class':'form-control'}),
           'identification':forms.TextInput(attrs={'class':'form-control'}),
           'vision_eclairage_avertisseur_sonore':forms.TextInput(attrs={'class':'form-control'}),
           'direction':forms.TextInput(attrs={'class':'form-control'}),
           'train':forms.TextInput(attrs={'class':'form-control'}),
           'transmission_roulement':forms.TextInput(attrs={'class':'form-control'}),
           'jantes_pneus':forms.TextInput(attrs={'class':'form-control'}),
           'freinage':forms.TextInput(attrs={'class':'form-control'}),
           'suspension':forms.TextInput(attrs={'class':'form-control'}),
           'infrastructure':forms.TextInput(attrs={'class':'form-control'}),
           'aspect_carrosserie':forms.TextInput(attrs={'class':'form-control'}),
           'interieur':forms.TextInput(attrs={'class':'form-control'}),
           'clim_chauffage':forms.TextInput(attrs={'class':'form-control'}),
           'essai_routier':forms.TextInput(attrs={'class':'form-control'}),
           'commentaire':forms.Textarea(attrs={'class':'form-control'}),
       }

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model=Client
#         fields=('adresse_mail','mot_de_passe')
#         widgets={'mot_de_passe':forms.PasswordInput(),
#         'adresse_mail':forms.TextInput(attrs={'class':'form-control'}),
#         'mot_de_passe':forms.TextInput(attrs={'class':'form-control','required':'True'}),
        
#         }


class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    
    class Meta:
        model= User
        fields=["username","email","password1","password2"]
class CommentsForm(forms.ModelForm):
    
    class Meta:
        model = Commentaire
        fields = ["contenu"]
    
class OfferForm(forms.ModelForm):
    class Meta:
        model=Offre
        fields=['matricule','marque','couleur','region','puissance','cylindres','kilometrage','transmission','carburant','annee','image','prix_propose']