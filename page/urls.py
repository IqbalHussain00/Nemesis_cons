from django.urls import path
#from . import views
# from . import apiviews
from .views import *
from .apiviews import *

urlpatterns = [
    path('', home , name='home'),
    path('signup' , signup , name='signup' ),
    path('login' , login , name='login' ),
    path('logout' , logout , name='logout' ),
    
    path('edit_un', edit_un, name='edit_un'),
    path('delete_un', delete_un, name='delete_un'), 
    path('edit_e', edit_e, name='edit_e'),
    path('delete_e', delete_e, name='delete_e'),

    # path('get', apiviews.get, name='get'),
    # path('post', apiviews.post, name='post'),
    # path('put/<id>/', apiviews.put, name='put'),
    # path('patch/<id>/', patch, name='patch'),
    # path('delete/<id>/', apiviews.delete, name='delete'),
    path('getbook', getbook, name='getbook'),

    path('student', StudentAPI.as_view()),
    path('student/<id>', StudentAPI.as_view()),
    path('register', Userregister.as_view())

]