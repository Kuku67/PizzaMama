from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza
# Create your views here.
def index(request):
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, 'menu/index.html', {
        'pizzas' : pizzas
    })