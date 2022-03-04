from importlib.resources import Resource
from django.shortcuts import get_object_or_404, render
from .models import meeting, meetingminute, resource, event
from django.urls import reverse_lazy
from .forms import resourceForm, meetingForm
from django.contrib.auth.decorators import login_required


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

def resourceview(request, id):
    resource_view=get_object_or_404(resource, pk=id)
    return render(request, 'club/resourceview.html', {'resource_view' : resource_view})

@login_required
def newResource(request):
    form=resourceForm
    if request.method=='POST':
        form = resourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=resourceForm()
    else:
        form=resourceForm()
    return render(request, 'club/newresource.html', {'form': form})

@login_required
def newMeeting(request):
    form=meetingForm
    if request.method=='POST':
        form = meetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=meetingForm()
    else:
        form=meetingForm()
    return render(request, 'club/newmeeting.html', {'form': form})

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')