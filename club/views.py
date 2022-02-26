from django.shortcuts import get_object_or_404, render
from .models import meeting, meetingminute, resource, event
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    return render(request, 'club/index.html') 

def getresource(request):
    resource_list=resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list' : resource_list})

def meetingview(request):
    meeting_list=meeting.objects.all()
    return render(request, 'club/meetings.html', {'meeting_list' : meeting_list})

def meetingmin(request, id):
    meet=get_object_or_404(meeting, pk=id)
    return render(request, 'club/meetingminutes.html', {'meet' : meet})