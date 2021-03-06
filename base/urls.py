from django.urls import URLPattern, path
from . import views


urlpatterns = [
    # homepage
    path('', views.home, name="home"),
    # other pages str=string pk=primaryvaluekey
    # login page
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('volunteer/', views.volunteerPage, name="volunteer"),
    path('about/', views.aboutPage, name="about"),
    path('contact/', views.contactPage, name="contact"),
    path('volunteerform/', views.volunteerFormPage, name='volunteerForm'),
]
