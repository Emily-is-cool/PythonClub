from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.getresource, name='Resources'),
    path('meetings/', views.meetingview, name='meetings'),
    path('meeting_min/<int:id>', views.meeting_min, name='somethingelse'),
]