from django.urls import path
from . import views

app_name = 'converter'

urlpatterns = [
    path('', views.text_to_html, name='text_to_html'),
]
