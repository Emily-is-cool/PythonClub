from django.shortcuts import render
from .models import meeting, meetingminute, resource, event

# Create your views here.
def index(request):
    return render(request, 'club/index.html')  

def meeting(reqest):
    meeting_list=meeting.objects.all()
    return render(request, 'club/meeting.html', {'meeting_list': meeting_list})

def resource(request):
    resource_list=request.objects.all()
    return render(request, 'club/resource.html',{'resource_list': resource_list})