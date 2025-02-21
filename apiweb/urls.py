from django.http import HttpResponse
from django.urls import path
from django.contrib import admin
from games.views import IniciarBatallaView, MovimientoView

def home(request):
    return HttpResponse('Api web está corrriendo...')

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/iniciar-batalla', IniciarBatallaView.as_view()),
    path('api/movimiento/<int:game_id>', MovimientoView.as_view()),
]
