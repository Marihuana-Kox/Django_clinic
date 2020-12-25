from django.urls import path

from . views import index_select_diagnos, get_month, get_free_date_time

from cl_medication.views import get_service_select

urlpatterns = [
    path('records/', index_select_diagnos, name='record-views'),
    path('records/month/<int:year>-<int:month>/', get_month, name='month'),
    path('get_medication/<int:medications>/', get_service_select, name='get_medication'),
    path('free_time/<int:day>-<int:mont>-<int:year>-<int:medic/', get_free_date_time, name='get_free_time'),
]   