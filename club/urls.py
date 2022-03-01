from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.getresource, name='resources'),
    path('meetings/', views.meetingview, name='meetings'),
    path('meetingminutes/<int:id>', views.meetingmin, name='somethingelse'),
    path('newresource/', views.newResource, name='newresource'),
    path('resourceview/<int:id>', views.resourceview, name = 'viewresources'),
    path('newmeeting/', views.newMeeting, name='newmeeting')
]