from django.shortcuts import render
# Add the following import
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fish

# Create your views here.
# Add the following import
from django.http import HttpResponse

class FishCreate(CreateView):
    model = Fish
    fields = '__all__'
    success_url = '/fishes/'

class FishUpdate(UpdateView):
    model = Fish
    # Let's disallow the renaming of a fish by excluding the name field!
    fields = ['breed', 'description', 'age']

class FishDelete(DeleteView):
    model = Fish
    success_url = 'fishes/'


# Define the home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

#Add a new view
def fishes_index(request):
    fishes = Fish.objects.all()
    return render(request, 'fishes/index.html', {'fishes': fishes})

def fishes_detail(request, fish_id):
    fish = Fish.objects.get(id=fish_id)
    return render(request, 'fishes/detail.html', { 'fish': fish })