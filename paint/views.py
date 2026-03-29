from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def quote(request):
    return render(request, 'query.html')

def thank_you(request):
    return render(request, 'thank.html')
