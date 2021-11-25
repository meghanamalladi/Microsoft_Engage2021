from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path
from home import views

urlpatterns = [
     path('', TemplateView.as_view(template_name="base.html")),
     path('index', TemplateView.as_view(template_name="index.html")),
     path('about',views.about,name="about"),
     path('contact',views.contact,name="contact"),
     path('upload',views.upload,name="upload"),
     path('edit',views.edit,name="edit"),
     path('view',views.view,name="view"),
]