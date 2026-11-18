
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from common.mixins import CreateUpdateContextMixin, CoreValidationMixin
from .forms import ProfesionalForm, ServicioForm, HorarioLaboralForm, ReservaForm, BloqueoAgendaForm
from django.urls import reverse_lazy

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
    form_class = ProfesionalForm
    template_name = 'common/base_create_update.html'

    titulo_creacion = 'Crear profesional'
    titulo_actualizacion = None
    url_borrado = None

    # UD4.4a - Mensaje de éxito con la representación textual del profesional
    def get_success_message(self, cleaned_data):
        return "Profesional '{}' creado correctamente".format(str(self.object))

    # UD4.2a - Redirección al formulario de actualización del profesional creado
    def get_success_url(self):
        return reverse_lazy('profesional_update', kwargs={'pk': self.object.pk})


class ProfesionalUpdateView(SuccessMessageMixin, CreateUpdateContextMixin, UpdateView):
    model = Profesional
    form_class = ProfesionalForm
    template_name = 'common/base_create_update.html'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar profesional'
    url_borrado = 'profesional_delete'

    # UD4.4a - Mensaje de éxito con la representación textual del profesional
    def get_success_message(self, cleaned_data):
        return "Profesional '{}' actualizado correctamente".format(str(self.object))

    # UD4.2a - Redirección al formulario de actualización del profesional
    def get_success_url(self):
        return reverse_lazy('profesional_update', kwargs={'pk': self.object.pk})


# UD4.2e - Variables de contexto para eliminar Profesional

class ProfesionalDeleteView(DeleteView):
    model = Profesional
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('profesional_list')

    titulo = 'Eliminar profesional'
    mensaje_confirmación = '¿Está seguro de que desea eliminar este profesional?'


# UD4.2a - Vistas de creación, actualización y eliminación de Servicio
# UD4.2d - Aplicación del Mixin de contexto a Servicio
# UD4.4a - Mensajes de éxito

class ServicioCreateView(SuccessMessageMixin, CreateUpdateContextMixin, CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'common/base_create_update.html'

    titulo_creacion = 'Crear servicio'
    titulo_actualizacion = None
    url_borrado = None

    # UD4.4a - Mensaje de éxito con la representación textual del servicio
    def get_success_message(self, cleaned_data):
        return "Servicio '{}' creado correctamente".format(str(self.object))

    # UD4.2a - Redirección al formulario de actualización del servicio creado
    def get_success_url(self):
        return reverse_lazy('servicio_update', kwargs={'pk': self.object.pk})


class ServicioUpdateView(SuccessMessageMixin, CreateUpdateContextMixin, UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'common/base_create_update.html'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar servicio'
    url_borrado = 'servicio_delete'

    # UD4.4a - Mensaje de éxito con la representación textual del servicio
    def get_success_message(self, cleaned_data):
        return "Servicio '{}' actualizado correctamente".format(str(self.object))

    # UD4.2a - Redirección al formulario de actualización del servicio
    def get_success_url(self):
        return reverse_lazy('servicio_update', kwargs={'pk': self.object.pk})


# UD4.2e - Variables de contexto para eliminar Servicio

class ServicioDeleteView(DeleteView):
    model = Servicio
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('servicio_list')

    titulo = 'Eliminar servicio'
    mensaje_confirmación = '¿Está seguro de que desea eliminar este servicio?'


# UD4.2a - Vistas de creación, actualización y eliminación de HorarioLaboral
# UD4.2d - Aplicación del Mixin de contexto a HorarioLaboral
# UD4.4a - Mensajes de éxito

class HorarioLaboralCreateView(CoreValidationMixin, SuccessMessageMixin, CreateUpdateContextMixin, CreateView):
    model = HorarioLaboral
    form_class = HorarioLaboralForm
    template_name = 'common/base_create_update.html'

    titulo_creacion = 'Crear horario laboral'
    titulo_actualizacion = None
    url_borrado = None

    # UD4.4a - Mensaje de éxito con la representación textual del horario laboral
    def get_success_message(self, cleaned_data):
        return "Horario laboral '{}' creado correctamente".format(str(self.object))

    # UD4.2a - Redirección al formulario de actualización del horario laboral creado
    def get_success_url(self):
        return reverse_lazy('horariolaboral_update', kwargs={'pk': self.object.pk})


class HorarioLaboralUpdateView(CoreValidationMixin, SuccessMessageMixin, CreateUpdateContextMixin, UpdateView):
    model = HorarioLaboral
    form_class = HorarioLaboralForm
    template_name = 'common/base_create_update.html'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar horario laboral'
    url_borrado = 'horariolaboral_delete'

    # UD4.4a - Mensaje de éxito con la representación textual del horario laboral
    def get_success_message(self, cleaned_data):
        return "Horario laboral '{}' actualizado correctamente".format(str(self.object))

    # UD4.2a - Redirección al formulario de actualización del horario laboral
    def get_success_url(self):
        return reverse_lazy('horariolaboral_update', kwargs={'pk': self.object.pk})


# UD4.2e - Variables de contexto para eliminar HorarioLaboral

class HorarioLaboralDeleteView(DeleteView):
    model = HorarioLaboral
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('horariolaboral_list')

    titulo = 'Eliminar horario laboral'
    mensaje_confirmación = '¿Está seguro de que desea eliminar este horario laboral?'


# UD4.2a - Vistas de creación, actualización y eliminación de Reserva
# UD4.2d - Aplicación del Mixin de contexto a Reserva
# UD4.4a - Mensajes de éxito

class ReservaCreateView(CoreValidationMixin, SuccessMessageMixin, CreateUpdateContextMixin, CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'common/base_create_update.html'

    titulo_creacion = 'Crear reserva'
    titulo_actualizacion = None
    url_borrado = None

    # UD4.4a - Mensaje de éxito con la representación textual de la reserva
    def get_success_message(self, cleaned_data):
        return "Reserva '{}' creada correctamente".format(str(self.object))

    # UD4.2a - Redirección al formulario de actualización de la reserva creada
    def get_success_url(self):
        return reverse_lazy('reserva_update', kwargs={'pk': self.object.pk})


class ReservaUpdateView(CoreValidationMixin, SuccessMessageMixin, CreateUpdateContextMixin, UpdateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'common/base_create_update.html'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar reserva'
    url_borrado = 'reserva_delete'

    # UD4.4a - Mensaje de éxito con la representación textual de la reserva
    def get_success_message(self, cleaned_data):
        return "Reserva '{}' actualizada correctamente".format(str(self.object))

    # UD4.2a - Redirección al formulario de actualización de la reserva
    def get_success_url(self):
        return reverse_lazy('reserva_update', kwargs={'pk': self.object.pk})


# UD4.2e - Variables de contexto para eliminar Reserva

class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('reserva_list')

    titulo = 'Eliminar reserva'
    mensaje_confirmación = '¿Está seguro de que desea eliminar esta reserva?'


# UD4.2a - Vistas de creación, actualización y eliminación de BloqueoAgenda
# UD4.2d - Aplicación del Mixin de contexto a BloqueoAgenda
# UD4.4a - Mensajes de éxito

class BloqueoAgendaCreateView(CoreValidationMixin, SuccessMessageMixin, CreateUpdateContextMixin, CreateView):
    model = BloqueoAgenda
    form_class = BloqueoAgendaForm
    template_name = 'common/base_create_update.html'

    titulo_creacion = 'Crear bloqueo de agenda'
    titulo_actualizacion = None
    url_borrado = None

    # UD4.4a - Mensaje de éxito con la representación textual del bloqueo de agenda
    def get_success_message(self, cleaned_data):
        return "Bloqueo de agenda '{}' creado correctamente".format(str(self.object))

    # UD4.2a - Redirección al formulario de actualización del bloqueo de agenda creado
    def get_success_url(self):
        return reverse_lazy('bloqueoagenda_update', kwargs={'pk': self.object.pk})


class BloqueoAgendaUpdateView(CoreValidationMixin, SuccessMessageMixin, CreateUpdateContextMixin, UpdateView):
    model = BloqueoAgenda
    form_class = BloqueoAgendaForm
    template_name = 'common/base_create_update.html'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar bloqueo de agenda'
    url_borrado = 'bloqueoagenda_delete'

    # UD4.4a - Mensaje de éxito con la representación textual del bloqueo de agenda
    def get_success_message(self, cleaned_data):
        return "Bloqueo de agenda '{}' actualizado correctamente".format(str(self.object))

    # UD4.2a - Redirección al formulario de actualización del bloqueo de agenda
    def get_success_url(self):
        return reverse_lazy('bloqueoagenda_update', kwargs={'pk': self.object.pk})


# UD4.2e - Variables de contexto para eliminar BloqueoAgenda

class BloqueoAgendaDeleteView(DeleteView):
    model = BloqueoAgenda
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('bloqueoagenda_list')

    titulo = 'Eliminar bloqueo de agenda'
    mensaje_confirmación = '¿Está seguro de que desea eliminar este bloqueo de agenda?'
