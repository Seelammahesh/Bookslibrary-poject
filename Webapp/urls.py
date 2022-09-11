#from django.contrib import admin
from django.urls import path, include
from Webapp.views import get_view,create_book,update_view,delete_view,register
from django.contrib.auth.urls import *

urlpatterns = [



    path('register/',register),
  #  path('accounts/', include('django.contrib.auth.urls')),
    path('get/',get_view),
    path('create/',create_book),
    path("update/<int:id>/",update_view),
    path("delete/<int:id>/",delete_view)

]
