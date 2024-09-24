from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import LoginForm, UserForm, ProfileForm, ProjectForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password , check_password
from .models import Profile, Project
from django.contrib.auth.decorators import login_required
from django import forms

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Account created successfully!')
            Profile.objects.create(user=user)
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'main/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, "Login successful.")
                return redirect('profile')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    projects = Project.objects.filter(profile=profile)
    education = profile.education.split('\n')
    experience = profile.experience.split('\n')
    print(experience)
    return render(request, 'main/profile.html', {'profile': profile, 'projects': projects, 'education': education, 'experience': experience})

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = Profile.objects.get(user=request.user)
            project.save()
            messages.success(request, 'Project added successfully!')
            return redirect('profile')
    else:
        form = ProjectForm()
    return render(request, 'main/add_project.html', {'form': form})

@login_required
def edit_info(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'main/edit_profile.html', {'form': form})

def select_project(request):
    profile = Profile.objects.get(user=request.user)
    projects = Project.objects.filter(profile=profile)
    if request.method == 'POST':
        project = Project.objects.get(id=request.POST['project_id'])
        return redirect('edit_project', project.id)
    else:
        return render(request, 'main/select_project.html', {'projects': projects})

def edit_project(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('profile')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'main/edit_project.html', {'form': form, 'project': project})

@login_required
def delete_project(request, project_id):
    project = Project.objects.get(id=project_id)
    project.delete()
    messages.success(request, 'Project deleted successfully!')
    return redirect('profile')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = { 'username': forms.TextInput(attrs={'class': 'form-control'}), 'email': forms.EmailInput(attrs={'class': 'form-control'}) }

@login_required
def setting(request):
    user = request.user
    
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Settings updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'There was an error updating your settings.')
    else:
        form = UserEditForm(instance=user)

    return render(request, 'main/setting.html', {'form': form})

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Old Password', 'class': 'form-control'}))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter New Password', 'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm New Password', 'class': 'form-control'}))

@login_required
def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']
            
            if check_password(old_password, user.password):
                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    user = authenticate(username=user.username, password=new_password)
                    if user is not None:
                        auth_login(request, user)
                        messages.success(request, 'Password changed successfully and you are still logged in!')
                        return redirect('profile')
                    else:
                        messages.error(request, 'Something went wrong. Please log in again.')
                else:
                    messages.error(request, 'New password and confirm password do not match.')
            else:
                messages.error(request, 'Old password is incorrect.')
    else:
        form = ChangePasswordForm()

    return render(request, 'main/change_pass.html', {'form': form})

def view_profile(request):
    email = request.GET.get('email')
    if not email:
        messages.error(request, "Please enter an email to search for a profile.")
        return render(request, 'main/profile_not_found.html')
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return render(request, 'main/profile_not_found.html')
        return redirect('profile')
    
    profile = get_object_or_404(Profile, user=user)
    projects = Project.objects.filter(profile=profile)
    education = profile.education.split('\n') if profile.education else []
    experience = profile.experience.split('\n') if profile.experience else []
    
    return render(request, 'main/profile.html', {'profile': profile, 'projects': projects, 'education': education, 'experience': experience})