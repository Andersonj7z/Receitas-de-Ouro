from django.shortcuts import render, get_object_or_404
from .models import Receita

# Create your views here.

def home(request):
    receitas = Receita.objects.all()
    return render(request, 'home/principal.html', {'receitas': receitas})

def ver_receitas(request, id):
   receita = get_object_or_404(Receita, pk=id)
   return render(request, 'home/receitas.html', {'receita': receita})