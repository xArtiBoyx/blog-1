from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html')


def second_view(request):
    return render(request, 'main/second.html')
