from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('getresource/', views.getresource, name='Resources')
]