from django.shortcuts import render

from django.views.generic import UpdateView

from .forms import UserRegistrationForm, ProfileEdit


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


def profile(request):
    return render(request, 'account/profile.html')


class ProfileUpdate(UpdateView):
    model = profile
    form_class = ProfileEdit
    success_url = '/profile/'
