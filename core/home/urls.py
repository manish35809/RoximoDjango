from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('aboutus/', aboutus, name="aboutus"),
    path('lenses/', lenses, name="lenses"),
    path('contact/', contact, name="contact")
]