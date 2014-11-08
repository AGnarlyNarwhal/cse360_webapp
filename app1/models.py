from django.db import models
from django.core.files import File
from django.contrib.auth.models import User
from userprofile.models import UserProfile
from django.utils import timezone
# Create your models here.
# Users will have a name, that we display when they're logged in 
# A email, which we will use to register them and send a password reset link to 
# A password which we will authenticate when they log in 

class Event(models.Model): 
    name = models.CharField(max_length=255) 
    date = models.DateTimeField('event_date') #Blank
    pub_date = models.DateTimeField('date published')
    num_tickets = models.IntegerField()
    description = models.TextField()
    picture = models.ImageField(upload_to='photos/event_thumbnails', 
        default="photos/event_thumbnails/event_default.jpeg", blank=True, null=True)
    #Needed to import pillow to use this 
    host = models.ForeignKey(User, related_name="Event_Host", blank=True, null=True)
    #Links the event to the user who published it.     
    attendees = models.ManyToManyField(User, related_name="Attendees",blank=True,null=True)
    #e_ticket = models.ForeignKey('Ticket', related_name="ticket", blank=True,null=True)
    #Will create an event.attendees and a person.event_set
    #These will be created and have methods I can use to operate on them
    def __str__(self): 
        return self.name
    def get_absolute_url(self): 
        return '/app1/get/%i/' % self.id
    def get_date(self): 
        return self.date

class Ticket(models.Model):
    event = models.ForeignKey('Event', blank=True, null=True)
    customer = models.ForeignKey(User, blank=True, null=True)
    num_tickets = models.IntegerField(default='0', blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    #Tickets are accessed via 'event.ticket_set' or 'User.ticket_set'
    def __str__(self): 
        return "%s %s" % (self.event.name, self.customer.username)
    
    
