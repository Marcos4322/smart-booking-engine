from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from common.mixins import CreateUpdateContextMixin

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


# UD4.2a - Vistas de creación, actualización y eliminación de Profesional
# UD4.2d - Aplicación del Mixin de contexto a Profesional
class ProfesionalCreateView(CreateUpdateContextMixin, CreateView):
    model = Profesional
    template_name = 'base_create_update.html'
    success_url = 'profesional_list'

    titulo_creacion = 'Crear profesional'
    titulo_actualizacion = None
    url_borrado = None


class ProfesionalUpdateView(CreateUpdateContextMixin, UpdateView):
    model = Profesional
    template_name = 'base_create_update.html'
    success_url = 'profesional_list'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar profesional'
    url_borrado = 'profesional_delete'


class ProfesionalDeleteView(DeleteView):
    model = Profesional
    template_name = 'base_confirm_delete.html'
    success_url = 'profesional_list'


# UD4.2a - Vistas de creación, actualización y eliminación de Servicio
# UD4.2d - Aplicación del Mixin de contexto a Servicio
class ServicioCreateView(CreateUpdateContextMixin, CreateView):
    model = Servicio
    template_name = 'base_create_update.html'
    success_url = 'servicio_list'

    titulo_creacion = 'Crear servicio'
    titulo_actualizacion = None
    url_borrado = None


class ServicioUpdateView(CreateUpdateContextMixin, UpdateView):
    model = Servicio
    template_name = 'base_create_update.html'
    success_url = 'servicio_list'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar servicio'
    url_borrado = 'servicio_delete'


class ServicioDeleteView(DeleteView):
    model = Servicio
    template_name = 'base_confirm_delete.html'
    success_url = 'servicio_list'


# UD4.2a - Vistas de creación, actualización y eliminación de HorarioLaboral
# UD4.2d - Aplicación del Mixin de contexto a HorarioLaboral
class HorarioLaboralCreateView(CreateUpdateContextMixin, CreateView):
    model = HorarioLaboral
    template_name = 'base_create_update.html'
    success_url = 'horariolaboral_list'

    titulo_creacion = 'Crear horario laboral'
    titulo_actualizacion = None
    url_borrado = None


class HorarioLaboralUpdateView(CreateUpdateContextMixin, UpdateView):
    model = HorarioLaboral
    template_name = 'base_create_update.html'
    success_url = 'horariolaboral_list'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar horario laboral'
    url_borrado = 'horariolaboral_delete'


class HorarioLaboralDeleteView(DeleteView):
    model = HorarioLaboral
    template_name = 'base_confirm_delete.html'
    success_url = 'horariolaboral_list'


# UD4.2a - Vistas de creación, actualización y eliminación de Reserva
# UD4.2d - Aplicación del Mixin de contexto a Reserva
class ReservaCreateView(CreateUpdateContextMixin, CreateView):
    model = Reserva
    template_name = 'base_create_update.html'
    success_url = 'reserva_list'

    titulo_creacion = 'Crear reserva'
    titulo_actualizacion = None
    url_borrado = None


class ReservaUpdateView(CreateUpdateContextMixin, UpdateView):
    model = Reserva
    template_name = 'base_create_update.html'
    success_url = 'reserva_list'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar reserva'
    url_borrado = 'reserva_delete'


class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = 'base_confirm_delete.html'
    success_url = 'reserva_list'


# UD4.2a - Vistas de creación, actualización y eliminación de BloqueoAgenda
# UD4.2d - Aplicación del Mixin de contexto a BloqueoAgenda
class BloqueoAgendaCreateView(CreateUpdateContextMixin, CreateView):
    model = BloqueoAgenda
    template_name = 'base_create_update.html'
    success_url = 'bloqueoagenda_list'

    titulo_creacion = 'Crear bloqueo de agenda'
    titulo_actualizacion = None
    url_borrado = None


class BloqueoAgendaUpdateView(CreateUpdateContextMixin, UpdateView):
    model = BloqueoAgenda
    template_name = 'base_create_update.html'
    success_url = 'bloqueoagenda_list'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar bloqueo de agenda'
    url_borrado = 'bloqueoagenda_delete'


class BloqueoAgendaDeleteView(DeleteView):
    model = BloqueoAgenda
    template_name = 'base_confirm_delete.html'
    success_url = 'bloqueoagenda_list'