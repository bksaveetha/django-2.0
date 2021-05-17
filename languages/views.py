from django.shortcuts import render
from django.core.files import File
from django.http import HttpResponse
from rest_framework import viewsets 
from .models import mishra , Upload 
from .serializers import mishraSerializer , UploadSerializer 
from rest_framework.response import Response



def writetofile(request):
    f = open('/home/anand/Downloads/bk.txt', 'w')
    testfile = File(f)
    testfile.write('hello rohit dubey')
    testfile.close()
    f.close()
    return HttpResponse()

def readfile(request):
    f = open('/home/anand/Downloads/bk.txt', 'r')
    if f.mode =='r':
        contents = f.read()
        print(contents)
    return HttpResponse()           

class mishraView(viewsets.ModelViewSet):
    
    queryset = mishra.objects.all()
    serializer_class  = mishraSerializer

class UploadView(viewsets.ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer


    
      

