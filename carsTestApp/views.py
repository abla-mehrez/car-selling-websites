from re import U
from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect,HttpResponse

from django.core.paginator import Paginator
from .forms import   CommentsForm, OfferForm, RegisterForm, Bilan_expertForm,Bilan_expert_update_Form

from django.urls import reverse_lazy,reverse


from carsTestApp.models import Offre, Expert,User,Client,Bilan_expert
from django.core.paginator import Paginator

from django.views.generic import UpdateView,DeleteView
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.mixins import PermissionRequiredMixin

#///////////////////////////////////////////////////////////////
    #CRUD using functions: 
    #get all elements: the first step consits on gettings all gthe cars, the second consists on serializing them and the third consists on returning json:
    #############################################################################################################################################################################
    #ESPACE EXPERT
    #############################################################################################################################################################################
@permission_required("carsTestApp.view_bilan_expert",raise_exception=True)
@login_required(login_url="/login/")
def EspaceExpert(request):
 liste_bilan=Bilan_expert.objects.all()
 if request.method=='POST':
     bilan_id=request.POST.get("bilan-id")
     bilan=Bilan_expert.objects.filter(id=bilan_id).first()
     bilan.delete()
 return render (request,'Expert/EspaceExpert.html',{"liste":liste_bilan})
#     #############################################################################################################################################################################
#     #ADD NEW BILAN
#     #############################################################################################################################################################################
@permission_required("carsTestApp.add_bilan_expert",raise_exception=True)
@login_required(login_url="/login/")
def AddBilan(request,**kwargs): 
  if request.method=='POST':
    bilan_expert_form=Bilan_expertForm(request.POST,user=request.user)
    x=request.POST.get("voiture")
    print(x)
    print(request.POST) 
    if bilan_expert_form.is_valid():
     bilan= bilan_expert_form.save(commit=False)
     bilan.expert_id = request.user.id
     bilan.active=True
     #getting the data from voiture_associée field
     data = bilan_expert_form.cleaned_data
     voiture_associée = data['voiture_associée']
     print(voiture_associée)
     get_matricule=Offre.objects.get(matricule=voiture_associée)
     print('la voiture est',get_matricule.matricule)
     bilan.save()
    #  bilan_expert_form.fields['voiture_associée'].queryset=Offre.objects.filter(~Offre(matricule=voiture_associée))
    
     get_all_offers=Offre.objects.all()
     print('les offres enregistrées',get_all_offers)
     for i in get_all_offers:
         if i.matricule==get_matricule.matricule:
           i.bilan_id=bilan.id
           i.prix_enchere=bilan.prix_suggéré
         i.save() 
     return redirect('/app/expert/espaceExpert')
    else:
      return HttpResponse('<h2> not valid </h2>')
  else:
    bilan_expert_form=Bilan_expertForm(user=request.user)
    dict={'form':bilan_expert_form}
    return render(request,'Expert/AddBilan.html',dict)
# #############################################################################################################################################################################
# #update bilan
# #############################################################################################################################################################################

class Update_Bilan(PermissionRequiredMixin,UpdateView):
   permission_required='carsTestApp.schange_bilan_expert'
   model = Bilan_expert
  #  fields='__all__'
   form_class=Bilan_expert_update_Form
   template_name = "Expert/UpdateBilan.html"
   success_url=reverse_lazy('carsApp:espace_expert')

# #############################################################################################################################################################################
def DetBilan(request,  **kwargs):
  pk = int(kwargs['pk'])
  bilanbyid=Bilan_expert.objects.get(pk=pk)
  bilanbyiddic={"bilanid":bilanbyid,'pk':pk}
  return render(request,'Expert/Bilan.html',bilanbyiddic)
#############################################################################################################################################################################
#ESPACE CLIENT
#############################################################################################################################################################################

def EspaceClient(request,**kwargs):
 if request.method=='POST':
  pk = int(kwargs['pk'])
  offerid=Offre.objects.get(pk=pk)
  print(offerid)

 else: 
    offres=Offre.objects.all()
    p=Paginator(offres,3)
    pagenum=request.GET.get('page',1)
    numEle=p.count #nombre total d'élements 
    print("le nombre total d'elements est:" ,numEle)
    nbPages=p.num_pages
    print("le nombre de pages est:",nbPages) #nombre de  pages
    for i in range (1,nbPages+1):
       elementperpage=p.page(i).object_list
       print("les elements de la page", i ,"sont: ", elementperpage,"\n")     
    try:
          page=p.page(pagenum) 
    except EmptyPage:
       page=p.page(1) 
    offresDict={"ListeOffres":offres,"item":page}
    return render(request,'Client/EspaceClient.html',offresDict)
#############################################################################################################################################################################
#détails d'une offre
#############################################################################################################################################################################
def DetOff(request,  **kwargs):
  pk = int(kwargs['pk'])
  offerbyid=Offre.objects.get(pk=pk)
  if request.method=='POST':
    form=CommentsForm(request.POST)
    if form.is_valid():
      comment=form.save(commit=False)
      comment.acheteur = request.user
      comment.offre_id=kwargs['pk']
      comment.save()
      return HttpResponseRedirect(reverse("carsApp:offer_detail", kwargs={'pk':pk}))
  else:     
   form=CommentsForm()
   offerbyiddic={"offreid":offerbyid,"form":form}
   return render(request,'Client/OfferDetail.html',offerbyiddic)

#############################################################################################################################################################################
#SIGN-UP
#############################################################################################################################################################################
def SignUP (request):
  if request.method=='POST':
    form=RegisterForm(request.POST)
    if form.is_valid():
      user=form.save(commit=False)
      user.is_client=True
    #   user.first_name=form.cleaned_data.get('first_name')
    #   user.last_name=form.cleaned_data.get('last_name')
      user=form.save()
      print("the user is",user)
      print("the user is a client=",user.is_client)
      client=Client.objects.create(user_id=user.id,name=user.username)
      print("from user to client is",client)
      client=form.save(commit=False)
    #   client.name=user.username
      client=form.save()
      print("le client est",client)
      login(request,user)
      messages.success(request,f"account was created for  {user.username}")
      return redirect('/app/client/espaceClient')
  else:
    form=RegisterForm()    
    
  return render(request,'Client/SignUp.html',{'form':form})



#########################################################################################################################
#create offer
#########################################################################################################################
@login_required(login_url="app/login")
def CreateOffer(request):
 if User.is_client:
  if request.method=='POST':
    offerform=OfferForm(request.POST,request.FILES)
    if offerform.is_valid():
      offer=offerform.save(commit=False)
      offer.vendeur=request.user
      offer.save()
      return redirect('/app/client/espaceClient')
  else:
    offerform=OfferForm()
  return render (request,'Client/CreateOffer.html',{'form':offerform})
#########################################################################################################################
#login 
#########################################################################################################################
def LoginView(request):
  if request.method=="POST":
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(request,username=username,password=password)
    if user is not None and user.is_client:
      print("theuseris",user.username,user.password)
      login(request,user)
      return redirect('carsApp:espace_client')
    elif user is not None and user.is_expert:
      login(request,user)
      return redirect('carsApp:espace_expert')
    else:
      return redirect('carsApp:login')
  else:
    return render(request,'registration/login.html')


#########################################################################################################################
#logout
#########################################################################################################################
def LogoutView(request):
   logout(request)
   messages.info(request, "Logged out successfully!")
   return redirect('carsApp:login')
#########################################################################################################################
#Getting expert
 ########################################################################################################################

def GetExpert (request,**kwargs):
 if User.is_expert: 
  pk = int(kwargs['pk'])
  offerid=Offre.objects.get(pk=pk)
  print(offerid)
  if request.method=='POST': 
     gouv=request.POST.get('region')
     print('le gouvernorat selectionné est',gouv)
     expert_par_region=Expert.objects.filter(region=gouv)
     expert_par_region_dict={"expert_par_region":expert_par_region,'pk':pk}
     print ("lexpert de la region:",gouv,"est:",expert_par_region)
     if 'choisir' in request.POST:
      name=request.POST.get('choisir')
      exp=Expert.objects.get(user_id=name)
      print('lexpert est',exp)
      exp.notifie=True
      exp.save()
      # nbre=0
      # notif=Notification.objects.create(ident=200,exp_not=exp,client_not=request.user,number=nbre)
      # print(notif) 
      # notif.number=notif.number+1
      # notif.save()
      # nbre+=1
      # notif.number=nbre
      # nbre=notif.number
      # print("l'expert choisi est",name)
      get_vendeur=request.user
      get_not=Offre.objects.filter(expert=exp)
      print(get_not)
      compteur=get_not.count()
      print('choisi',compteur,'fois')
      
      ######################################
      #get the offer id
      ##################
    
      get_offre=Offre.objects.filter(vendeur=request.user,id=pk).first()
      print('loffre est',get_offre.matricule)
    
      print('le vendeur de loffre est',get_offre.vendeur)
      get_offre.expert=exp
      get_offre.save()
      # form.field['vendeur_offre'].queryset=Client.objects.filter(user=request.user)
      # get_offre=Expert.objects.get(matricule)
      # print('loffre est',get_offre)
      return redirect('/app/client/espaceClient')
     return render (request,'Expert/ListeExpert.html',expert_par_region_dict)  
  else :
     expert=Expert.objects.all()
     expert_list={'expert_list':expert}
    #  if 'choisir' in request.POST:
    #   name=request.POST.get('choisir')
    #   print("choisi",name)
    #   return redirect('/app/client/listeExpert')
     return render(request,'Expert/ListeExpert.html',expert_list)
 else:
    return HttpResponse("<h2>erreur</h2>")
###############################################################################################################
class Update_Offre(UpdateView):
   model = Offre
  #  fields='__all__'
   form_class=OfferForm
   template_name = "Client/UpdateOffer.html"
   success_url=reverse_lazy('carsApp:espace_client')
###############################################################################################################
class OffreDelete(DeleteView):
   model = Offre
   pk_url_kwarg = 'pk'
   template_name = "Client/DeleteOffre.html"
   success_url=reverse_lazy('carsApp:espace_client')