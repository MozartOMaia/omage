from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'omage'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('novo_card/', views.cadastrar_card, name='cadastrar_card'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
