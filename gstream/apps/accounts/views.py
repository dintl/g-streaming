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
            login_user = authenticate(username=request.POST.get('username'), password=request.POST.get('password1'))
            login(request, login_user)
            
            #The next lines require an admin to approve the user and add the first + last name
            user.first_name = form.cleaned_data['first_name'] 
            user.last_name = form.cleaned_data['last_name'] 
            user.is_active = False
            user.save()
            
            profile = models.Profile(user=user,
                                     country=form.cleaned_data['country'],
                                     bio=form.cleaned_data['bio']
                                    )
            profile.save()
             
            return HttpResponseRedirect('/')
    else:
        
        # neither POST nor GET with key
        form = forms.RegistrationForm() 
    
    return render_to_response('accounts/account_register.html',
                             {'form': form},
                               context_instance=RequestContext(request))
    

