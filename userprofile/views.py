from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from forms import UserProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm()
        
    args = {'user': user}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('userprofile/user_image_upload.html', args)   

