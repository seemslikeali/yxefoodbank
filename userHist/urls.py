from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('history/', views.userHistPage, name="userHist"),
]
