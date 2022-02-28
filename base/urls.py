from django.urls import URLPattern, path
from . import views

urlpatterns = [
    # homepage
    path('', views.home, name="home"),
    # other pages str=string pk=primaryvaluekey
    path('room/<str:pk>/', views.room, name="room"),
    # login page
    path('login/', views.loginPage, name="login"),
    path('signup/', views.signup, name="signup")

]
