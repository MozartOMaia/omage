from django.shortcuts import render
from django.http import HttpResponse
from .models import Card

# Create your views here.
def index(request):
    cards_list = Card.objects.all()
    context = {'cards_list':cards_list}
    return render(request, 'omage/index.html', context)