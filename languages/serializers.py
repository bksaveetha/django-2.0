from rest_framework import serializers
from rest_framework.serializers import FileField 
from .models import mishra , Upload , Textfile



class mishraSerializer(serializers.ModelSerializer):
    class Meta:
        model = mishra
        fields = ('id', 'name', 'paradigm')

class UploadSerializer(serializers.ModelSerializer):
    file_uploaded = FileField()
    class Meta:
        model  = Upload
        fields = ['file_uploaded']

class TextfileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Textfile
        fields = ['file']
         





