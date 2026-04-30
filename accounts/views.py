"""

# Render : will load a html page
# Redirect : will redirect user to a specific html page based on completed activity

"""

from django.shortcuts import render, redirect

'''
>>> django inbuilt auth functions that return true or false based on the process :
-login = returns True if the user is currently logged in
-logout = returns True if the user successfully logs out
-authenticate = returns True if the user provides correct credentials for a login process
'''

from django.contrib.auth import  login, logout , authenticate

'''
>>> return true or false if the user is logged in or not and allow execution of the function based on the result
'''

from django.contrib.auth.decorators import login_required

'''
>>> messages alerts : notifications
'''
from django.contrib import messages

''' 
>>> Require the custom form views for the password reset process
'''
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView

'''
>>> only load views when required
'''
from django.urls import reverse_lazy

'''
>>> import form files from your apss forms.py
'''
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm

# Create your views here.
## Registration process / sign-ups
def register_view(request):
    # Check if user is already logged 
    # Django always maintains our user object 
    if request.user.is_authenticated:
        # If user is already authenticated take them to dashboard
        return redirect('media_assets:dashboard') 

        # check the type of request method
        # When submitting a form we use POST method
        # When viewing a form we use GET method

    if request.method == 'POST':
        # Create the form reference from frm forms.py
        form = UserRegistrationForm(request.POST)
        # If all form inputs are filled we save details to the db
        # Form.is_valid checks if all form fields are filled correctly

        if form.is_valid():
            user = form.save() # Save() submits details to our db
            login(request, user) # Saving our login state for that user
            messages.success(request, f'Welcome {user.username}, your account was created successfully')

            # Redirect use to our dashboard
            return redirect('media_assets:dashboard')
    else:
        form = UserRegistrationForm() # default get process
        
    return render(request, 'accounts/register.html', {'form': form}) # render the form to our template



# Login process
def login_view(request):
    # Check if user is already logged in
    if request.user.is_authenticated:
        return redirect('media_assets:dashboard')

    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        # check if fields are filled correctly
        if form.is_valid():

            # pick up username and password entries
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Use django method authenticate from django to login user
            user = authenticate(request, username=username, password=password) # Query db for thr user
            if user is not None:
                login(request, user) # Login user
                messages.success(request, f'Welcome back {user.username}')
                return redirect('media_assets:dashboard')

    else:
        form = UserLoginForm(request)
    return render(request, 'accounts/login.html', {'form': form})

# Logout process
# Ensure the user is logged is logged in by use of the decoratormethod
@login_required # The function defined below will only be executed if the user is logged in
def logout_view(request):
    logout(request) # Logout user
    messages.info(request, f'You have been logged out successfully!!')
    return redirect('accounts:login')

# Profile update process
@login_required
def profile_view(request):
    if request.method == 'POST':
        # request, POST - will pick text date
        # request, FILES - will pick media data
        # instance - will update the current logged in user details.
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)

        # check if all fields are filled correctly
        if form.is_valid():
            form.save()
            messages.success(request, f'Your profile has been updated successfully!!')
            return redirect('accounts:profile')
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'accounts/profile.html', {'form': form})

    # view for our password reset process
    # django inbuilt configs for the process
class CustomPasswordResetView(PasswordResetView):
    # Interface change
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    # reverse lazy will ensure view is added when needed
    success_url = reverse_lazy('accounts:password_reset_done')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    # inteface change
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')