from django.contrib import admin
from carsTestApp.models import  User,Expert,Client,Offre,Bilan_expert
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class UserAdmin(UserAdmin): 
   fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('is_expert', 'is_client')
        })
    )
   list_display = ('username','is_expert','is_client') 
   list_filter = ('is_expert',)

admin.site.register(User, UserAdmin)

@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin): 
   list_display = ("nom","prenom","region") 
   list_filter = ('notifie',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin): 
   list_display = ("name",) 
@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin): 
   list_display = ("matricule",) 

@admin.register(Bilan_expert)
class Bilan_expertAdmin(admin.ModelAdmin): 
   list_display = ("commentaire",) 