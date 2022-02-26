from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.getresource, name='resources'),
    path('meetings/', views.meetingview, name='meetings'),
    path('meetingmin/<int:id>', views.meetingmin, name='somethingelse'),
    
]