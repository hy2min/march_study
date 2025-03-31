from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'name': 'kevin',
        'age': 21,
        'color':['red', 'black', 'blue'],
        'num': 1
    }
    
    return render(request, 'articles/index.html', {'context':context})