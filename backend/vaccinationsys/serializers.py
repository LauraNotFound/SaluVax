from rest_framework import serializers
from vaccinationsys.models import Lote, Rol, Usuario, Vacuna, Paciente, Vial

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = ['id', 'nombre']

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'nombre']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombres', 'apellidos', 'dni', 'username', 'password', 'rol']

class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = ['id', 'dosis_ml', 'fecha_inyeccion', 'vial', 'paciente', 'medico']

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'nombres', 'apellidos', 'dni', 'direccion', 'celular', 'fecha_nacimiento']

class VialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vial
        fields = ['id', 'nombre', 'kit', 'enfermedad', 'fecha_caducidad', 'lote']
