from django.shortcuts import render, redirect
# Add the following import
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Fish, Toy
from .forms import FeedingForm

# Create your views here.
# Add the following import


class FishCreate(CreateView):
    model = Fish
    fields = ['name', 'breed', 'description', 'age']

class FishUpdate(UpdateView):
    model = Fish
    # Let's disallow the renaming of a fish by excluding the name field!
    fields = ['breed', 'description', 'age']

class FishDelete(DeleteView):
    model = Fish
    success_url = '/fishes/'


# Define the home view
def home(request):
      return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#Add a new view
def fishes_index(request):
    fishes = Fish.objects.all()
    return render(request, 'fishes/index.html', {'fishes': fishes})

def fishes_detail(request, fish_id):
    fish = Fish.objects.get(id=fish_id)
    feeding_form = FeedingForm()
    return render(request, 'fishes/detail.html', { 
        'fish': fish, 'feeding_form': feeding_form 
    })

def add_feeding(request, fish_id):
      # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
  # validate the form
    if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.fish_id = fish_id
        new_feeding.save()
    return redirect('detail', fish_id=fish_id)

class ToyList(ListView):
      model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'