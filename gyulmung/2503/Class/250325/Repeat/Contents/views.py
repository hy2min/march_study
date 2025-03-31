from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': 'kevin',
        'age': 21,
        'color': ['red', 'yellow', 'black']
    }
    return render(request, "Contents/index.html", {'context':context})