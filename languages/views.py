from django.shortcuts import render
from rest_framework import viewsets , generics, request
from .models import mishra , Upload
from .serializers import mishraSerializer , UploadSerializer,TextfileSerilizer
from rest_framework.response import Response



class mishraView(viewsets.ModelViewSet):
    
    queryset = mishra.objects.all()
    serializer_class  = mishraSerializer

class UploadView(viewsets.ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer

class TextfileView(generics.ListAPIView):
    def get_queryset(self, request):
        filename  = 'bk.txt'
        queryset = Textfile.objects.all()
        serializer = TextfileSerilizer(queryset)
        response = HttpResponse(serializer.data, content_type='text/plain; charset=UTF-8')
        response['Content-Disposition'] = ('attachment; filename={0}'.format(filename))

        return response       
      

