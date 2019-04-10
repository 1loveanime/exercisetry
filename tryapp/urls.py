from django.urls import path
from . import views

urlpatterns = [
	path('', views.welcome, name='welcome' ),
	path('accounts/register', views.registration, name="registration"),
	path('person/asdihnawudnawidnawd/asdojnbawusdnawidnaiwnd/', views.person_creation, name='person_creation'),
]