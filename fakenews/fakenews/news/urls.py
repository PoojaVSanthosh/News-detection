from django.urls import path
from .views import home,display

urlpatterns = [
    path('home/',home,name='home'),
    path('display/',display,name='display'),
]