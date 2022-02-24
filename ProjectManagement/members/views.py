from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm,EditProfileForm1,PasswordChangingForm

class PasswordsChangeView(PasswordChangeView):
    form_class=PasswordChangingForm
    #form_class=PasswordChangeForm
    template_name='registration/change-password.html'
    success_url=reverse_lazy('members:password_success')

class UserRegisterView(generic.CreateView):
    form_class=SignUpForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class=EditProfileForm1
    template_name="registration/edit_profile.html"
    success_url=reverse_lazy('ProjectManagementApp:home')

    def get_object(self):
        return self.request.user

def password_success(request):
    return render(request,'registration/password_success.html',{})