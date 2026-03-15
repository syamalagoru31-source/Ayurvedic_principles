from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('diseases/', views.diseases, name='diseases'),
    path('remedies/', views.remedies, name='remedies'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('diet/', views.diet, name='diet'),
]