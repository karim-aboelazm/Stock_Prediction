from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirectBase
from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .form import SignUpForm,UserForm,ProfileForm,FollowedStockForm
from django.urls import reverse
from django.shortcuts import redirect
from .models import Profile,UserFollowedStocks
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm 
from django.utils.translation import ugettext as _

class UserRegisterView(generic.CreateView):
        form_class = SignUpForm
        template_name = 'registration/register.html'
        success_url = reverse_lazy('login')

@login_required
def profile(request):
    profile = Profile.objects.get(user = request.user)
    if request.method=='POST':
        form = FollowedStockForm(request.POST or None)
        if form.is_valid():
            form.save() 
        return redirect('accounts:profile')
    else:
        follow_stock = UserFollowedStocks.objects.all()
        return  render(request, 'profile.html', {'profile':profile,
                                                 'follow_stock':follow_stock})


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == "POST":
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            my_profile = profileform.save(commit = False)
            my_profile.user = request.user
            my_profile.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    return render(request,'edit-profile.html',{'userform':userform,
                                               'profileform':profileform})


def dell(request,id):
    item = UserFollowedStocks.objects.get(id=id)
    item.delete()
    return redirect('accounts:profile')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Your password was successfully updated!'))
            return redirect('accounts:change_password')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change.html', {'form': form})






