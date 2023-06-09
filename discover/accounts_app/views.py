from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import (
    authenticate,
    login
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from accounts_app.models import (
    Profile
)
from accounts_app.forms import (
    LoginForm,
    UserRegistrationForm,
    UserEditForm,
    ProfileEditForm
)


@login_required
def dashboard(request):
    title = 'discover'
    
    context = {
        'title': title
    }
    
    return render(
        request,
        'account/dashboard.html',
        context
    )
    
    
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            
            Profile.objects.create(user=new_user)
            
            context = {
                'new_user': new_user
            }
            
            return render(
                request,
                'account/register_done.html',
                context
            )
    else:
        user_form = UserRegistrationForm()
    
    context = {
        'user_form': user_form
    }
    
    return render(
        request,
        'account/register.html',
        context
    )
    
    
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(
            instance=request.user,
            data=request.POST
        )
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Error updating your profile")

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    
    return render(
        request,
        'account/edit.html',
        context
    )