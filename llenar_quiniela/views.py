# views.py
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import EquiposPartidoForm
from .models import Prediccion, Fotos_quiniela
from tabla_general.models import Cartas, Num_quiniela
from llenar_quiniela.models import imagenes_cartas
import os


def ingresar_resultado(request):
    # Obtener todos los registros de la base de datos
    registros = Fotos_quiniela.objects.all()
    #print(registros)
    reg_car = Cartas.objects.all()
    reg_im_car = imagenes_cartas.objects.all()
    datos_procesados = []
    datos_procesados2 = []
    reg_q = Num_quiniela.objects.all()
    for r in reg_q:
        numero_jornada = int(r.num_jor)
    nombre_campo = f'j{numero_jornada}'
    #print(nombre_campo)
    for registro in reg_car:
        datos_procesados.append({
            'nombre': registro.nombre,
            'carta': getattr(registro, nombre_campo),
        })
    for registro in registros:
        print(type(nombre_campo))
        datos_procesados2.append({
            'jornada': getattr(registro, nombre_campo),
        })
    #print(datos_procesados2)
    if request.method == 'POST':
        jor = request.POST['cartas']
        jor = jor.split(' ')
        if len(jor) == 3:
            if jor[0] == 'Luis':
                nom = 'Luis Angel'
            else:
                nom = 'Juan Luis'
            car = jor[2]
        else:
            nom = jor[0]
            car = jor[1]
        #print(jor, car)
    else:
        nom = 'Nadie'
        car = 'NC'
    foto_url = []
    for registro in reg_im_car:
        print(type(car), car)
        foto_url.append({
            'foto': getattr(registro, car),
        })
    #print(datos_procesados2)
    #print(foto_url)
    if car == 'DQ':
        consejo = 'DOBLE QUINIELA (DQ): Puedes llenar la quiniela como si fueran 2 (una es la azul otra es la roja). Puedes repetir las predicciones que creas necesarias o puedes hacerlas completamente diferentes, tu eliges'
    elif car == 'IQ':
        consejo = 'INTERCAMBIO DE QUINIELA (IQ): Rellena tu quiniela de forma normal. Solo recuerda que al final de la jornada, puedes robarle los puntos a quien tu quieras (siempre y cuando no le hayan robado ya a esa persona) debes a visar a Choco a quien le quieres robar (tienes 3 dias para hacer el robo). Los puntos que tu haces, se los queda la otra persona'
    elif car == 'J':
        consejo = 'JUGADOR GOL (J): Rellena tu quiniela de forma normal. Cuando pases la foto de tu quiniela por el grupo, debes mandarla con el nombre de un jugador que creas que va a echar gol esa semana, si atinas, tiene 2 puntos extra. Recuerda que puede ser de cualquier equipo, siempre y cuando no repitas un jugador de un equipo que ya hayas elegido. Por ejemplo, si ya escogiste a Gignac de los Tigres, ya no podrás elegir más jugadores de Tigres'
    elif car == 'M':
        consejo = 'MULTIPLICADOR (M): Rellena tu quiniela de manera normal, solo tienes que señalar de alguna manera, un juego que creas muy seguro que puedes atinar, un juego que tu creas que haya un 100 por ciento de probabilidad que suceda, si lo atinas, tienes 2 puntos extra'
    elif car == 'MA':
        consejo = 'MARCADOR (MA): Rellena la quiniela con los marcadores con los que crees que va a terminar el juego, si atinas el resultado, tienes +1 como normalmente sucede, pero si además atinas el marcador, tienes un +1 adicional. Hay límite de puntos atinados por marcador hasta un total de +3'
    elif car == 'NC':
        consejo = 'NO CARTA (NC): Si por alguna razón no tienes carta, llena tu quiniela de manera normal'
    elif car == 'OD':
        consejo = 'OPCION DOBLE (OD): Rellena tu quiniela como se muestra en la imagen. Tienes la posibilidad de seleccionar 2 juegos en los que puedes poner 2 opciones (Local y Empate, Local y Visita o Empate y Visita). Selecciona 2 juegos que tengas algo de dudas sobre quien va a ganar'
    elif car == 'OT':
        consejo = 'OPCION TRIPLE (OT): Rellena tu quiniela como se muestra en la imagen. Tienes la posibilidad de seleccionar 2 juegos en los que puedes poner las 3 opciones (Local, Empate y Visita). Selecciona 2 juegos que tengas algo de dudas sobre quien va a ganar y asegura esos resultados'
    elif car == 'RC':
        consejo = 'ROBO DE CARTA (RC): Roba la carta a alguien de tus oponentes, la que mas te apetezca. Pregunta a Choco cual es la disponibilidad, porque si alguien ya mando su quiniela y uso su carta, ya no se la puedes robar. Una vez que hayas avisado y quedado de acuerdo con Choco, el te actualiza la pagina para que llenes tu quiniela o directamente si ya sabes como funciona la nueva carta que tienes, puedes llenar tu quiniela'
    #expl_cartas = []
    #expl_cartas.append({
        
    #})
    return render(request, 'llenar_quiniela/llenar_quiniela copy.html', {'imagenes': registros, 'cartas': datos_procesados, 'carta_seleccionada': nom, 'foto_url': foto_url, 'consejo': consejo, 'jor': datos_procesados2})



