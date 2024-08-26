from django.urls import path
from document import views

urlpatterns = [
    path('file/save-extract', views.ExtractAndSaveFileUploadView.as_view(), name='file-extract'),
]
