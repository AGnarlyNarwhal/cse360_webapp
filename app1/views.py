from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from app1.models import Event,Ticket
#from app1.forms import EventForm, buy_tickets
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from datetime import *
from django.contrib.auth.decorators import login_required
from django.utils import timezone 

# Create your views here.
@login_required
def events(request): 
    #session_lin = request.session.get('lin','nlin')
    today = timezone.now()
   
    #if (session_lin == 'lin'):
    user = request.user
    return render_to_response("app1/events.html", 
    {'event_list': Event.objects.exclude(date__lt=timezone.now()), 'user': user, 'today': today})
            
    #else: 
        #return HttpResponseRedirect('/accounts/login')
@login_required
def event(request, event_id=1): 
            return render_to_response('app1/event.html', {'event':  Event.objects.get(id=event_id), 'user': request.user})

"""
def publish(request): 
    if request.POST:
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("app1/events.html")
        else:
            form = EventForm()
        
        args = {}
        args.update(csrf(request))
        args['form'] = form 
        return HttpResponse("You need to create a page for publishing events")
        #return render_to_response("app1/events.html", args)
"""
@login_required
def buytickets(request, event_id, num_ticks): 
    _event = Event.objects.get(id=event_id)
    user = request.user
    tickets = _event.num_tickets 
    buy_ticks = int(num_ticks)
    _event.ticket_set.create(customer=user, num_tickets=buy_ticks, event_date=_event.date) 
    #This will link to both event and customer for querying, event.ticket_set, and user.ticket_set 
    tickets = tickets - buy_ticks
    _event.num_tickets = tickets
    _event.save()
    return HttpResponseRedirect("/home/")
    #return render_to_response("app1/event.html", {'event': event } )

@login_required
def tickets(request): 
    user = request.user
    return render_to_response('cse360_webapp/tickets.html', {'ticket_list':user.ticket_set.order_by('-event_date'), 'user': user})

    

