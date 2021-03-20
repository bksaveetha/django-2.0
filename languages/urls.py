from django.urls import path, include
from . import views 
from rest_framework import routers


router = routers.DefaultRouter()
router.register('mishra', views.mishraView)
router.register('Upload', views.UploadView)
router.register('Textfile', views.TextfileView, basename = Textfile)
 

urlpatterns = [
    path('', include(router.urls)),
    
   
]