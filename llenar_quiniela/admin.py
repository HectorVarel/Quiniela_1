from django.contrib import admin
from .models import EquiposPartidos, Prediccion, Fotos_quiniela, imagenes_cartas
# Register your models here.

admin.site.register(EquiposPartidos)
admin.site.register(Prediccion)
admin.site.register(Fotos_quiniela)
admin.site.register(imagenes_cartas)