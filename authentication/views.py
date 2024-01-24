from django.shortcuts import render, redirect, get_object_or_404
from . import forms, models
from django.contrib.auth import login
from django.conf import settings



def signup_page(request):
    message = ""
    form = forms.signupForm()
    if request.method == 'POST':
        form = forms.signupForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            print('about to authenticate user')
            #login(request,user)
            return redirect('login')
        if not form.is_valid():
            message = form.errors #.as_text()
    return render(request,'authentication/signup.html',{'form':form,"message":message})

def get_profile(request,username):
    profile = get_object_or_404(models.User, username=username)

    context = {
        'first_name': profile.first_name,
        'last_name': profile.last_name,
        'profile_photo': profile.profile_photo,
    }
    return render(request, 'authentication/profile.html', context=context)

def change_profile_photo(request, username):
    profile = get_object_or_404(models.User, username=username)
    if request.user  == profile:
        if request.method == 'POST':
            form = forms.ProfilePhotoForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('profile-page', username=username)  # Redirect to the profile page

        else:
            form = forms.ProfilePhotoForm(instance=profile)
    else:
        return redirect('profile-page')

    return render(request, 'authentication/edit_profile_photo.html', {'form': form})