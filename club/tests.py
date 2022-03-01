from django.test import TestCase

from club.forms import resourceForm
from .models import event, resource, meeting, meetingminute
import datetime
from .views import index, getresource, meetingview, meetingmin
from django.urls import reverse
from .forms import resourceForm, meetingForm


# Create your tests here.
class eventsTest(TestCase):
    def setUp(self):
        self.events=event(eventname='Python Party')

    def test_eventstring(self):
        self.assertEqual(str(self.events), 'Python Party') #ok

    def test_tablename(self):
        self.assertEqual(str(event._meta.db_table), 'event') #ok

class resourceTest(TestCase):
    def setUp(self):
        self.resources=resource(resourcename='Python Visualizer')  

    def test_resourcestring(self):
        self.assertEqual(str(self.resources), 'Python Visualizer') #ok

    def test_tablename2(self):
        self.assertEqual(str(resource._meta.db_table), 'resource') #ok

class meetingTest(TestCase):
    def setUp(self) -> None:
        self.meeting=meeting(meetingtitle='Orientation', meetingdate=datetime.date(2019, 10, 2), 
        meetingtime=datetime.time(8,48,45) , meetinglocation='DisneyLand' ,
        agenda='introductions')
        return super().setUp()
    def test_meeting(self):
        self.assertEqual(str(self.meeting), 'Orientation') #ok
    def test_meetingName(self):
        self.assertEqual(str(meeting._meta.db_table), 'meeting') #ok

class meetingminuteTest(TestCase):
    def setUp(self):
        self.meetingminutes=meetingminute(pk=1)
    def test_meetingminutes(self):
        self.assertEqual(self.meetingminutes), 1 #FAIL
    def test_tablename3(self):
        self.assertEqual(str(meetingminute._meta.db_table), 'meetingminutes') #ok

class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200) #ok

class ResourceTest(TestCase):
    def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('resources'))
       self.assertEqual(response.status_code, 200) #FAIL

class ResourceFormTest(TestCase):
    def test_resourceForm(self):
        form=resourceForm (data={
            'resourcename' : 'Meow', 
            'resourcetype':'Meow', 
            'resourceurl': 'http://meow.com', 
            'dateentered': '2022-2-2', 
            'resourcedescription': 'meow', 
            'userid': 1
            })
        self.assertFalse(form.is_valid())

class meetingFormTest(TestCase):
    def test_meetingForm(self):
        form=meetingForm (data={
            'meetingtitle': 'meow',
            'meetingdate': '2022-8-4',
            'meetingtime': '1:00',
            'meetinglocation': 'meow',
            'agenda': 'meow'
            })
        self.assertTrue(form.is_valid())