# resume/urls.py
from django.urls import path
from . import views
from .views import ResumeUploadView 

urlpatterns = [
    path('upload/', ResumeUploadView.as_view(), name='upload_resume'),
]
