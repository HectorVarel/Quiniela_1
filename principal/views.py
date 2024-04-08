from django.shortcuts import render, HttpResponse
from tabla_general.models import Jornadas


# Create your views here.

def principal(request):
    jornadas = Jornadas.objects.all().order_by('-suma_j').first()
    #print(jornadas)

    return render(request, 'principal/principal copy.html', {'jornadas': jornadas, 'page':'principal'})
