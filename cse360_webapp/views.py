from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from forms import MyRegistrationForm
from django.contrib.auth.decorators import login_required


def login(request):
    session_lin = request.session.get('lin','nlin')
   # if session_lin is 'nlin':
    if session_lin == 'lin':
        return HttpResponseRedirect('/home/')
    c = {}
    c.update(csrf(request))    
    request.session['lin'] = 'nlin' #Set session login status = false
    return render_to_response('cse360_webapp/login.html', c,)
    
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        request.session['lin'] = 'lin'
        return HttpResponseRedirect('/home/')
    else:
        request.session['lin'] = 'nlin'
        return HttpResponseRedirect('/accounts/invalid')
@login_required
def loggedin(request):
    return render_to_response('cse360_webapp/loggedin.html', 
                              {'full_name': request.user.username},)

def invalid_login(request):
    return render_to_response('cse360_webapp/invalid_login.html')

@login_required
def logout(request):
    auth.logout(request)
    request.session['lin'] = 'nlin'
    return render_to_response('cse360_webapp/logout.html')

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
        
    else:
        form = MyRegistrationForm()
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('cse360_webapp/register.html', args)



def register_success(request):
    return render_to_response('cse360_webapp/register_success.html')
    
