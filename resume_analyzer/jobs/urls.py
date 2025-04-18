from django.urls import path
from .views import JobCreateView, JobMatchingView

urlpatterns = [
    path('create/', JobCreateView.as_view(), name='job-create'),
    path('match/', JobMatchingView.as_view(), name='job-match'),
]
