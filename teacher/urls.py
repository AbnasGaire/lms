from django.urls import path
from . import views
urlpatterns=[
    path('addteacher/',views.addteacher,name='addteacher'),
    path('teacherdata/',views.teacherdata,name='teacherdata'),
    path('viewteacher',views.viewteacher,name='viewteacher'),
    path('suspendteacher/<int:x>',views.suspendteacher,name='suspendteacher'),
    path('continueteacher/<int:x>',views.continueteacher,name='continueteacher')


]