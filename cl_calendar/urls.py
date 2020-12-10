from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('next/<int:year>/<int:month>/', views.get_month, name='next'),

]
