from django.test import TestCase, Client 
from django.contrib.auth.models import User
from app1.models import Event, Ticket
from django.utils import timezone
from django.core.urlresolvers import reverse
from datetime import datetime
# Create your tests here.

class EventTest(TestCase): 
    def create_event(name="test name", description="a test event"):
        return Event.objects.create(name=name, date=timezone.now(),
            pub_date=timezone.now(), num_tickets='5', description=description)
            #picture, host, and attendees can be blank 
           
    def test_event_creation(self): 
        e = self.create_event()
        self.assertTrue(isinstance(e,Event))
        self.assertEqual(e.__str__(), e.name)
        #Check that string returns title 
       
    def test_event_list_view(self): 
        e = self.create_event()
        #log user in so they can run the view 
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        url = reverse('app1.views.events')
        resp = self.client.get(url)
        
        #Should be 302, redirected if not logged in 
        self.assertEqual(resp.status_code, 200)
        
    def test_single_event_view(self): 
        e = self.create_event()
        #log user in so they can run the view 
        user = User.objects.create_user(username='test_user', password='password')
        self.client.login(username='test_user', password='password')
        url = reverse('app1.views.event', args=[e.id])
        resp = self.client.get(url) 
        
        self.assertEqual(reverse('app1.views.event', args=[e.id] ), e.get_absolute_url())
    
class TicketTest(TestCase): 
    def create_ticket(self):
        user = User.objects.create_user(username='test_user', password='password')
        event = Event.objects.create(name="test event", date=timezone.now(),
            pub_date=timezone.now(), num_tickets='5', description="test description")
        return Ticket.objects.create(customer=user, event=event, num_tickets='5')
           
    def test_ticket_creation(self): 
        t = self.create_ticket()
        self.assertTrue(isinstance(t,Ticket))
        
       
    def test_ticket_view(self): 
        t = self.create_ticket()
        #log in with user created in create_ticket 
        self.client.login(username='test_user', password='password')
        url = reverse('app1.views.tickets')
        resp = self.client.get(url)
        
        #Should be 302, redirected if not logged in 
        #self.assertEqual(resp.status_code, 302)    
        self.assertEqual(resp.status_code, 200)
        
    def test_buytickets_view(self): 
        t = self.create_ticket()
        event = Event.objects.create(name="test event", date=timezone.now(),
            pub_date=timezone.now(), num_tickets='5', description="test description")
        self.client.login(username='test_user', password='password')
        #arguments for url are event.id and num_tickets
        url = reverse('app1.views.buytickets', args=[event.id,1])
        resp = self.client.get(url)
        
        #Should redirect home automatically 
        self.assertEqual(resp.status_code, 302) 
        #self.assertEqual(reverse('app1.views.buytickets', args=[event.id,1]), reverse('app1.views.events')

