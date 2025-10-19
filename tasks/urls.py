from django.urls import path
from .views import ListCreateTask, RetrieveUpdateDestroyTask

urlpatterns = [
    path('task/', ListCreateTask.as_view(), name="list-create-task"),
    path('task/<int:pk>/', RetrieveUpdateDestroyTask.as_view(), name="detail-task"),
]