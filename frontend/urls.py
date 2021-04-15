from django.urls import path,include
from .views import mainView

urlpatterns = [
    path('',mainView,name='main'),
]