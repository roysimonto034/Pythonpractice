--------------------models.py
from django.db import models

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    
  #makemigration,migrate,createsuperuser
  
 -------------------------admin.py
 from django.contrib import admin
 from .models import Snippet
 
 @admin.register(Snippet)
 class StudentAdmin(admin.ModelAdmin):
    list_display=['created','title','code','language']

------------------------serializers.py
from rest_framework import serializers

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    created = serializers.DateTimeField(auto_now_add=True)
    title = serializers.CharField(max_length=100, blank=True, default='')
    code = serializers.TextField()
    linenos = serializers.BooleanField(default=False)
    language = serializers.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = serializers.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    
    -------------------------views.py
    
    from django.shortcuts import render
    from .models import Snippet
    from .serializers import SnippetSerializer
    from rest_framework.renderers import JSONRenderer
    from  django.http import HttpResponse,JsonResponse
    
    def snippet_detail(request):
        stud = Snippet.objects.get(id=1)
        serializer = SnippetSerializer(stud)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    
    def snippet_detail_id(request,pk):
        stud = Snippet.objects.get(id=pk)
        serializer = SnippetSerializer(stud)
        --------------------------------------------------------
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
        ------------------or-------------------------------------
        return JsonResponse(serializer.data,safe=True) # safe=True is default and  by defualt it supports only dict
        
    def snippet_detail_all(request,pk):
        stud = Snippet.objects.all()
        serializer = SnippetSerializer(stud,many=True)
        ---------------------------------------------------------
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
        -----------------or-------------------------------------
        return JsonResponse(serializer.data,safe=False)  #safe=False to support all types of data like list,tuple  
     
     -----------------------urls.py
     
    from django.contrib import admin
    from django.urls import path
    from api import views
    
    urlpatterns=
    [ path('snippetinfo/',views.snippet_detail),
      path('snippetinfo/<int:pk>',views.snippet_detail_id),
      path('snippetall/',views.snippet_detail_all)]