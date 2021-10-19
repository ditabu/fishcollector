from django.shortcuts import render

# Create your views here.
# Add the following import
from django.http import HttpResponse

class Fish: #Note that parens are optional if not inheriting from another class
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

fishes = [
    Fish('McFlurry', 'beta', 'red long tail', 2),
    Fish('Sachi', 'angel fish', 'fierce angel', 1),
    Fish('Puff Daddy', 'puffer fish', 'bad boy fo life', 2)
]
# Define the home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

#Add a new view
def fishes_index(request):
    return render(request, 'fishes/index.html', {'fishes': fishes})

