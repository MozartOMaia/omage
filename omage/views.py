from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Card
from django.views import generic
from django.utils import timezone
from django.urls import reverse

from .models import Card

# Create your views here.
# def index(request):
#     cards_list = Card.objects.all()
#     context = {'cards_list':cards_list}
#     return render(request, 'omage/index.html', context)

class IndexView(generic.ListView):
    template_name = 'omage/index.html'
    context_object_name = 'cards_list'
    def get_queryset(self):
        return Card.objects.all()

def cadastrar_card(request):
    if request.method == 'GET':
        return render(request, 'omage/new_card.html')
    if request.method == 'POST':
        texto_card = request.POST['texto_card']
        assinatura = request.POST['assinatura']
        img_card = request.FILES.get('img_card')
        pub_data = timezone.now()
        novo_card = Card(texto=texto_card, assinatura=assinatura, pub_date=pub_data, image=img_card)
        novo_card.save()
        lista_cards = Card.objects.all()
        context = {'cards_list': lista_cards}
        return HttpResponseRedirect(reverse('omage:index')) #render(request, 'omage/index.html', context)
        