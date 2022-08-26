from django.urls import path
from .views import *


urlpatterns = [
    path('', GamesPage.as_view(),name='home'),
]