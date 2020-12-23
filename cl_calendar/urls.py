from django.urls import path

from . import views
from cl_services.views import get_service_select

urlpatterns = [
    path('', views.index, name='index'),
    path('next/<int:year>-<int:month>/', views.get_month, name='next'),
    path('register/', views.add_register, name='register'),
    path('select/<int:service>/', get_service_select, name='select'),
]
