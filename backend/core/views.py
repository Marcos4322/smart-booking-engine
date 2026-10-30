from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import (
    Profesional,
    Servicio,
    HorarioLaboral,
    Reserva,
    BloqueoAgenda
)

# UD3.7a - Vistas del modelo Profesional
# UD3.8.b - Listado de clientes con paginación

class ProfesionalListView(ListView):
    model = Profesional
    template_name = 'core/profesional_list.html'
    paginate_by = 5


class ProfesionalDetailView(DetailView):
    model = Profesional
    template_name = 'core/profesional_detail.html'


# UD3.7a - Vistas del modelo Servicio
class ServicioListView(ListView):
    model = Servicio
    template_name = 'core/servicio_list.html'
    paginate_by = 5


class ServicioDetailView(DetailView):
    model = Servicio
    template_name = 'core/servicio_detail.html'


# UD3.7a - Vistas del modelo HorarioLaboral
class HorarioLaboralListView(ListView):
    model = HorarioLaboral
    template_name = 'core/horariolaboral_list.html'
    paginate_by = 5


class HorarioLaboralDetailView(DetailView):
    model = HorarioLaboral
    template_name = 'core/horariolaboral_detail.html'


# UD3.7a - Vistas del modelo Reserva
class ReservaListView(ListView):
    model = Reserva
    template_name = 'core/reserva_list.html'
    paginate_by = 5


class ReservaDetailView(DetailView):
    model = Reserva
    template_name = 'core/reserva_detail.html'


# UD3.7a - Vistas del modelo BloqueoAgenda
class BloqueoAgendaListView(ListView):
    model = BloqueoAgenda
    template_name = 'core/bloqueoagenda_list.html'
    paginate_by = 5


class BloqueoAgendaDetailView(DetailView):
    model = BloqueoAgenda
    template_name = 'core/bloqueoagenda_detail.html'

