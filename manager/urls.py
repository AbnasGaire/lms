from django.urls import path
from . import views
urlpatterns=[
    path('addmanager/',views.addmanager,name='addmanager'),
    path('error/',views.error,name='error'),
    path('managerdetail/',views.managerdetail,name='managerdetail')
]