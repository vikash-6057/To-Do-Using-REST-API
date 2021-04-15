from django.urls import path
from .views import apiView,taskListView,taskDetailView,taskCreateView,taskUpdateView,taskDeleteView
urlpatterns = [
    path('',apiView,name="api-overview"),
    path('task-list/',taskListView,name="task-list"),
    path('task-detail/<int:pk>/',taskDetailView,name="task-detail"),
    path('task-update/<int:pk>/',taskUpdateView,name="task-update"),
    path('task-delete/<int:pk>/',taskDeleteView,name="task-delete"),
    path('task-create/',taskCreateView,name="task-create"),
]