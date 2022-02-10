from django.shortcuts import render
from .models import meeting, meetingminute, resource, event

# Create your views here.
def index(request):
    return render(request, 'club/index.html') 

def getresource(request):
    resource_list=resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list' : resource_list})