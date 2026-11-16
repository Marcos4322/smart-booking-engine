from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from common.mixins import CreateUpdateContextMixin, CoreValidationMixin

from .models import (
    Profesional,
    Servicio,
    HorarioLaboral,
    Reserva,
    BloqueoAgenda
)


# UD3.7a - Vistas del modelo Profesional
# UD3.8.b - Listado con paginación

class ProfesionalListView(ListView):
    model = Profesional
    template_name = 'core/profesional_list.html'
    paginate_by = 5

    # UD4.2i - Ordenación del listado de profesionales
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', None)

        if ordering == 'asc':
            queryset = queryset.order_by('id')
        elif ordering == 'desc':
            queryset = queryset.order_by('-id')

        return queryset

class ProfesionalDetailView(DetailView):
    model = Profesional
    template_name = 'core/profesional_detail.html'


# UD3.7a - Vistas del modelo Servicio

class ServicioListView(ListView):
    model = Servicio
    template_name = 'core/servicio_list.html'
    paginate_by = 5

    # UD4.2i - Ordenación del listado de Servicios
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', None)

        if ordering == 'asc':
            queryset = queryset.order_by('id')
        elif ordering == 'desc':
            queryset = queryset.order_by('-id')

        return queryset


class ServicioDetailView(DetailView):
    model = Servicio
    template_name = 'core/servicio_detail.html'


# UD3.7a - Vistas del modelo HorarioLaboral

class HorarioLaboralListView(ListView):
    model = HorarioLaboral
    template_name = 'core/horariolaboral_list.html'
    paginate_by = 5

    # UD4.2i - Ordenación del listado de HorarioLaboral
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', None)

        if ordering == 'asc':
            queryset = queryset.order_by('id')
        elif ordering == 'desc':
            queryset = queryset.order_by('-id')

        return queryset

class HorarioLaboralDetailView(DetailView):
    model = HorarioLaboral
    template_name = 'core/horariolaboral_detail.html'


# UD3.7a - Vistas del modelo Reserva

class ReservaListView(ListView):
    model = Reserva
    template_name = 'core/reserva_list.html'
    paginate_by = 5

    # UD4.2i - Ordenación del listado de reservas
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', None)

        if ordering == 'asc':
            queryset = queryset.order_by('id')
        elif ordering == 'desc':
            queryset = queryset.order_by('-id')

        return queryset

class ReservaDetailView(DetailView):
    model = Reserva
    template_name = 'core/reserva_detail.html'


# UD3.7a - Vistas del modelo BloqueoAgenda

class BloqueoAgendaListView(ListView):
    model = BloqueoAgenda
    template_name = 'core/bloqueoagenda_list.html'
    paginate_by = 5

    # UD4.2i - Ordenación del listado de BloqueoAgenda
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', None)

        if ordering == 'asc':
            queryset = queryset.order_by('id')
        elif ordering == 'desc':
            queryset = queryset.order_by('-id')

        return queryset

class BloqueoAgendaDetailView(DetailView):
    model = BloqueoAgenda
    template_name = 'core/bloqueoagenda_detail.html'


# UD4.2a - Vistas de creación, actualización y eliminación de Profesional
# UD4.2d - Aplicación del Mixin de contexto a Profesional
# UD4.4a - Mensajes de éxito

class ProfesionalCreateView(SuccessMessageMixin, CreateUpdateContextMixin, CreateView):
    model = Profesional
    template_name = 'base_create_update.html'
    success_url = 'profesional_list'

    titulo_creacion = 'Crear profesional'
    titulo_actualizacion = None
    url_borrado = None

    success_message = "Profesional creado correctamente"


class ProfesionalUpdateView(SuccessMessageMixin, CreateUpdateContextMixin, UpdateView):
    model = Profesional
    template_name = 'base_create_update.html'
    success_url = 'profesional_list'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar profesional'
    url_borrado = 'profesional_delete'

    success_message = "Profesional actualizado correctamente"


# UD4.2e - Variables de contexto para eliminar Profesional

class ProfesionalDeleteView(DeleteView):
    model = Profesional
    template_name = 'base_confirm_delete.html'
    success_url = 'profesional_list'

    titulo = 'Eliminar profesional'
    mensaje_confirmación = '¿Está seguro de que desea eliminar este profesional?'


# UD4.2a - Vistas de creación, actualización y eliminación de Servicio
# UD4.2d - Aplicación del Mixin de contexto a Servicio
# UD4.4a - Mensajes de éxito

class ServicioCreateView(SuccessMessageMixin, CreateUpdateContextMixin, CreateView):
    model = Servicio
    template_name = 'base_create_update.html'
    success_url = 'servicio_list'

    titulo_creacion = 'Crear servicio'
    titulo_actualizacion = None
    url_borrado = None

    success_message = "Servicio creado correctamente"


class ServicioUpdateView(SuccessMessageMixin, CreateUpdateContextMixin, UpdateView):
    model = Servicio
    template_name = 'base_create_update.html'
    success_url = 'servicio_list'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar servicio'
    url_borrado = 'servicio_delete'

    success_message = "Servicio actualizado correctamente"


# UD4.2e - Variables de contexto para eliminar Servicio

class ServicioDeleteView(DeleteView):
    model = Servicio
    template_name = 'base_confirm_delete.html'
    success_url = 'servicio_list'

    titulo = 'Eliminar servicio'
    mensaje_confirmación = '¿Está seguro de que desea eliminar este servicio?'


# UD4.2a - Vistas de creación, actualización y eliminación de HorarioLaboral
# UD4.2d - Aplicación del Mixin de contexto a HorarioLaboral
# UD4.4a - Mensajes de éxito

class HorarioLaboralCreateView(CoreValidationMixin, SuccessMessageMixin, CreateUpdateContextMixin, CreateView):
    model = HorarioLaboral
    template_name = 'base_create_update.html'
    success_url = 'horariolaboral_list'

    titulo_creacion = 'Crear horario laboral'
    titulo_actualizacion = None
    url_borrado = None

    success_message = "Horario laboral creado correctamente"



class HorarioLaboralUpdateView(CoreValidationMixin, SuccessMessageMixin, CreateUpdateContextMixin, UpdateView):
    model = HorarioLaboral
    template_name = 'base_create_update.html'
    success_url = 'horariolaboral_list'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar horario laboral'
    url_borrado = 'horariolaboral_delete'

    success_message = "Horario laboral actualizado correctamente"


# UD4.2e - Variables de contexto para eliminar HorarioLaboral

class HorarioLaboralDeleteView(DeleteView):
    model = HorarioLaboral
    template_name = 'base_confirm_delete.html'
    success_url = 'horariolaboral_list'

    titulo = 'Eliminar horario laboral'
    mensaje_confirmación = '¿Está seguro de que desea eliminar este horario laboral?'


# UD4.2a - Vistas de creación, actualización y eliminación de Reserva
# UD4.2d - Aplicación del Mixin de contexto a Reserva
# UD4.4a - Mensajes de éxito

class ReservaCreateView(CoreValidationMixin, SuccessMessageMixin, CreateUpdateContextMixin, CreateView):
    model = Reserva
    template_name = 'base_create_update.html'
    success_url = 'reserva_list'

    titulo_creacion = 'Crear reserva'
    titulo_actualizacion = None
    url_borrado = None

    success_message = "Reserva creada correctamente"



class ReservaUpdateView(CoreValidationMixin, SuccessMessageMixin, CreateUpdateContextMixin, UpdateView):
    model = Reserva
    template_name = 'base_create_update.html'
    success_url = 'reserva_list'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar reserva'
    url_borrado = 'reserva_delete'

    success_message = "Reserva actualizada correctamente"


# UD4.2e - Variables de contexto para eliminar Reserva

class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = 'base_confirm_delete.html'
    success_url = 'reserva_list'

    titulo = 'Eliminar reserva'
    mensaje_confirmación = '¿Está seguro de que desea eliminar esta reserva?'


# UD4.2a - Vistas de creación, actualización y eliminación de BloqueoAgenda
# UD4.2d - Aplicación del Mixin de contexto a BloqueoAgenda
# UD4.4a - Mensajes de éxito

class BloqueoAgendaCreateView(CoreValidationMixin, SuccessMessageMixin, CreateUpdateContextMixin, CreateView):
    model = BloqueoAgenda
    template_name = 'base_create_update.html'
    success_url = 'bloqueoagenda_list'

    titulo_creacion = 'Crear bloqueo de agenda'
    titulo_actualizacion = None
    url_borrado = None

    success_message = "Bloqueo de agenda creado correctamente"



class BloqueoAgendaUpdateView(CoreValidationMixin, SuccessMessageMixin, CreateUpdateContextMixin, UpdateView):
    model = BloqueoAgenda
    template_name = 'base_create_update.html'
    success_url = 'bloqueoagenda_list'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar bloqueo de agenda'
    url_borrado = 'bloqueoagenda_delete'

    success_message = "Bloqueo de agenda actualizado correctamente"


# UD4.2e - Variables de contexto para eliminar BloqueoAgenda

class BloqueoAgendaDeleteView(DeleteView):
    model = BloqueoAgenda
    template_name = 'base_confirm_delete.html'
    success_url = 'bloqueoagenda_list'

    titulo = 'Eliminar bloqueo de agenda'
    mensaje_confirmación = '¿Está seguro de que desea eliminar este bloqueo de agenda?'