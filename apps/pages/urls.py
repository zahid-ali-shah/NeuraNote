from django.urls import path
from .views import home, contact_us, privacy_policy, terms_of_service

urlpatterns = [
    path('', home, name='home'),
    path('contact-us/', contact_us, name='contact_us'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('terms-of-service/', terms_of_service, name='terms_of_service'),
]