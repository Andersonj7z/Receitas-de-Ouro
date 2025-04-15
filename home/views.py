from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/principal.html')

def ver_receitas(request):
    return render(request, 'home/receitas.html')