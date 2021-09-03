from django.urls import path
from . import views
from . import apiviews

urlpatterns = [
    path('', views.home, name='home'),
    path('signup' , views.signup , name='signup' ),
    path('login' , views.login , name='login' ),
    path('logout' , views.logout , name='logout' ),
    
    path('edit_un', views.edit_un, name='edit_un'),
    path('delete_un', views.delete_un, name='delete_un'), 
    path('edit_e', views.edit_e, name='edit_e'),
    path('delete_e', views.delete_e, name='delete_e'),

    path('hello', apiviews.hello)
]