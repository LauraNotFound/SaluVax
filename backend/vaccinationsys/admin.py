from django.contrib import admin

from .models import Lote, Vial, Paciente, Rol, Usuario, Vacuna

# Register your models here.
admin.site.register(Lote)
admin.site.register(Vial)
admin.site.register(Paciente)
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Vacuna)
