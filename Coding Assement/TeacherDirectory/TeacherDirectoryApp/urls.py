from django.urls import path,include
from .views import *

urlpatterns = [
    path('file_upload/', TeacherDataUpload.as_view()),
    path('dashboard/', TeacherInformation.as_view()),
    path('details/<int:id>/', TeacherDetails.as_view()),
]