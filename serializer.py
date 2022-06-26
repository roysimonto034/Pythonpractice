ComplexDatatype-----------serialize----------->Pythonnativetype-----------------renderjson---------------->jsondata

jsondata------------------parsedata------------>Pythondatatype-------------------deserialization------------>Pythonnativedatatype


# complex datatype(DB model)----------------serialization------->Python-------render into json------------>JsonData

#JsonData------------parsedData---------------------->Python native--------------deserialization-------------->complexdatatype 

----------deserialization process--------

from rest_framework.parsers import JSONParser
parsed_data = JSONParser().parse(stream)


create serializer object

serializer = StudentSerializer(data=parsed_data)

---------------admin.py----------------

@admin.register(Student)
class StdentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']

validated data
serializer.is_valid()

serializer.validated_data   
serializer.errors


------------------serializers.py-------------------------

from rest_framework import serializers
from models import Student
class StudentSerializers(serializers.Serializer):
      name = serializers.CharField(max_length=100)
      roll = serilaizers.IntegerField()
      city = serializers.CharField(max_length=100)
      
 def create(self, validate_data):
     return Student.objects.create(**validate_data)
     
 
 
 -----------------------models.py--------------
 
 from django.db import models
 
 
 class Student(models.Model):
    name = models.Field(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
 
 ---------------myapp.py
 
 import requests
 import json 
 
 URL = "http://127.0.0.1:8000/stucreate"
 data = {'name': 'Monty', 'roll': 101, 'city': 'Bangalore'}
 
 json_data = json.dumps(data)
 
 r=request.post(url = URL, data=json_data)
 data = r.json()
 
 ---------------------views.py
 
 from django.shortcuts import render
 import io
 from rest_framework.parsers import JSONParser
 from .serializer import StudentSerializer
 from rest_framework.renderers import JSONRenderer
 from django.http import HttpResponse
 from django.views.decorators.csrf import csrf_exempt
 
 @csrf_exempt #to bypass csrftoken error
 def student_create(request):
     if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data) #convert json data to bytestream
        python_data = JSONParser().parse(stream)  #bytestream to pythondata
        serializer = StudentSerializer(data=python_data)          #convert python data to complex datatype (DBMS)        
        if serializer.is_valid():
           serializer.save()
           res={'msg':'Data inserted'}
           json_data = JSONRenderer.renser(res)  #convert python to json
           return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)  #error case handled
        return HttpResponse(json_data,content_type='application/json')
        
 -----------------------------urls.py------------
 from api import views
 url = [ path('studcreate/',views.student_create)
 ]
