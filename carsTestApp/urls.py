
from django.urls import  path
from.views import   CreateOffer, DetBilan, DetOff, EspaceClient,  SignUP,LoginView,LogoutView,GetExpert,AddBilan,EspaceExpert,Update_Bilan,Update_Offre,OffreDelete
app_name="carsApp"

urlpatterns = [
     path('expert/espaceExpert',EspaceExpert,name='espace_expert'),
     path('expert/add',AddBilan,name='add_bilan'),
     path('expert/update/<int:pk>',Update_Bilan.as_view(),name='update_bilan'),
     
     
     
     
     path('client/listeExpert/<int:pk>',GetExpert,name='get_expert'),
     path('client/espaceClient', EspaceClient,name='espace_client'),
     path('client/espaceClientDet/<int:pk>',DetOff,name='offer_detail'),
     path('client/BilanDet/<int:pk>',DetBilan,name='bilan_detail'),
     
    
     path('client/createOffer', CreateOffer,name='createOffer'),
     path('client/signup', SignUP,name='signup'),
     path('client/update/<int:pk>',Update_Offre.as_view(),name='update_offer'),
     

     path('login',LoginView, name='login'),
     path('logout',LogoutView, name='logout'),
     path('client/espaceClient/<int:pk>',OffreDelete.as_view(),name='delete_offer'),

]