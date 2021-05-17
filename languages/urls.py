from django.urls import path, include
from . import views 
from rest_framework import routers
from django.contrib import admin  




router = routers.DefaultRouter()
router.register('mishra', views.mishraView)
router.register('Upload', views.UploadView)

 

urlpatterns = [
    path('', include(router.urls)),
    path('filewrite',(views.writetofile)),
    path('readfile', (views.readfile))
]
    
   

