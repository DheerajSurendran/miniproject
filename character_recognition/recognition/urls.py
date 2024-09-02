# recognition/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.upload_image, name='upload_image'),
    # Add other URL patterns here if needed
]
