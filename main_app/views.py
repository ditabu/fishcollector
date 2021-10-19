from django.shortcuts import render
from .models import Fish

# Create your views here.
# Add the following import
from django.http import HttpResponse


# Define the home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

#Add a new view
def fishes_index(request):
    fishes = Fish.objects.all()
    return render(request, 'fishes/index.html', {'fishes': fishes})

