# from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from vaccinationsys.models import Lote, Rol, Usuario, Vacuna, Paciente, Vial
from vaccinationsys.serializers import (
    LoteSerializer, RolSerializer, UsuarioSerializer, 
    VacunaSerializer, PacienteSerializer, VialSerializer
)


class LoteListCreateView(ListCreateAPIView):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer

class LoteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer




class RolListCreateView(ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class RolDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer



class UsuarioListCreateView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer



class VacunaListCreateView(ListCreateAPIView):
    queryset = Vacuna.objects.all()
    serializer_class = VacunaSerializer

class VacunaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Vacuna.objects.all()
    serializer_class = VacunaSerializer



class PacienteListCreateView(ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer



class VialListCreateView(ListCreateAPIView):
    queryset = Vial.objects.all()
    serializer_class = VialSerializer

class VialDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Vial.objects.all()
    serializer_class = VialSerializer
