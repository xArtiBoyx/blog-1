from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserForm, ProfileForm
from .models import Profile
from django.contrib.auth import get_user_model
from main.models import Post

User = get_user_model()


@login_required
def profile(request):
    prof = Profile.objects.get(user=request.user.id)
    posts = Post.objects.filter(author=request.user)
    return render(request, 'account/profile.html', {'prof': prof, 'posts': posts})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_prof = profile_form.save(commit=False)
            new_prof.user = new_user
            new_prof.save()
            new_user.profile = new_prof
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user, 'profile_form': profile_form})
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
    return render(request, 'account/register.html', {'user_form': user_form, 'profile_form': profile_form})


def register_done(request):
    return render(request, 'account/register_done.html')

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
