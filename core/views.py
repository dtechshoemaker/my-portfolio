from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def detail(request, pk):
    pass

def about(request):
    pass

def contact(request):
    pass