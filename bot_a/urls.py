from django.urls import path
from . import views

urlpatterns = [
    path('bot', views.bot_a, name="bot")
]