from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileEdit, UserForm, ProfileForm
from .models import Profile
from django.contrib.auth import get_user_model


User = get_user_model()


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


def profile(request):
    prof = Profile.objects.get(user=request.user.id)
    return render(request, 'account/profile.html', {'prof': prof})


# def profile_update(request, pk):
#     prof = Profile.objects.get(pk=pk)
#     user = User.objects.get(id=prof.user.id)
#     if request.method == 'POST':
#         form = ProfileEdit(request.POST, instance=prof)
#         if form.is_valid():
#             new_form = form.save(commit=False)
#             user.first_name = form.cleaned_data['first_name']
#             user.last_name = form.cleaned_data['last_name']
#             user.email = form.cleaned_data['email']
#             new_form.save()
#             user.save()
#             return redirect(profile)
#     else:
#         form = ProfileEdit(instance=prof)
#         return render(request, 'account/profile_form.html', {'form': form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(instance=request.user, data=request.POST)
        profile_form = ProfileForm(instance=request.user.profile, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(profile)
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'account/profile_form.html', {'user_form': user_form, 'profile_form': profile_form})
