from django.contrib.auth.models import User
from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect

from . import forms
from . import models

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import mail_managers

def register(request):
    
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'], 
                                            form.cleaned_data['email'],
                                            form.cleaned_data['password1'])

            
            #To log in the user automatically uncomment the following two lines
            #login_user = authenticate(username=request.POST.get('username'), password=request.POST.get('password1'))
            #login(request, login_user)
            
            #The next lines require an admin to approve the user and add the first + last name
            user.first_name = form.cleaned_data['first_name'] 
            user.last_name = form.cleaned_data['last_name'] 
            user.is_active = False
            user.save()
            
            profile = models.Profile(user=user,
                                              country=form.cleaned_data['country'],
                                              )
            profile.save()
             
            mail_managers('G-Streaming New User "%s" requires approval' % user.username,
                      """
Dear G-Streaming Admin,

A new user has registered for your website. This user needs your approval to log in.

To allow the user to log in you can follow these steps:

1) Go to the new Django User: http://www.g-streaming.net/admin/auth/user/%s/
2) Click the active checkbox on the user settings
3) Click save
4) The user will be automatically notified their account has been activated


You may also view the new user's profile at:
http://www.g-streaming.net/admin/accounts/profile/%s/
                                              

""" % (user.id, profile.id), 
                     fail_silently=False)
            
            return HttpResponseRedirect('/accounts/approval-pending/')
    else:
        
        # neither POST nor GET with key
        form = forms.RegistrationForm() 
    
    return render_to_response('accounts/account_register.html',
                             {'form': form},
                               context_instance=RequestContext(request))
    

def approval_pending(request):
    
    return render_to_response('accounts/account_approval_pending.html',
                               context_instance=RequestContext(request))