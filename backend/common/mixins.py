from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.http import HttpResponseRedirect
from django.urls import reverse

# UD4.2d - Mixin para el contexto de creación y actualización

class CreateUpdateContextMixin:
    titulo_creacion = None
    titulo_actualizacion = None
    url_borrado = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo_creacion'] = self.titulo_creacion
        context['titulo_actualizacion'] = self.titulo_actualizacion
        context['url_borrado'] = self.url_borrado

        return context



# UD4.2f - Mixin para comprobar dependencias al eliminar

class DeleteDependencyMixin:

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            messages.error(
                self.request,
                "Existen dependencias para el objeto {}. Elimine antes dichas dependencias".format(self.object)
            )
            return HttpResponseRedirect(reverse('home'))


# UD4.2g - Mixin para validar el importe total de los cobros
class CobroMixin:

    def form_valid(self, form):
        factura = form.instance.factura
        importe = form.instance.importe

        total_cobros = 0

        for cobro in factura.cobros.all():
            if cobro.pk != form.instance.pk:
                total_cobros += cobro.importe

        if total_cobros + importe > factura.total:
            messages.error(
                self.request,
                "La suma de los cobros no puede superar el total de la factura."
            )
            return super().form_invalid(form)

        return super().form_valid(form)



# UD4.2h - Mixin para validar horarios y fechas del proyecto
class CoreValidationMixin:
    """Mixin que valida los horarios laborales y las fechas de inicio y fin."""

    def form_valid(self, form):
        datos = form.cleaned_data

        # Validación de HorarioLaboral
        if 'hora_inicio' in datos and 'hora_fin' in datos:
            if datos['hora_fin'] <= datos['hora_inicio']:
                messages.error(
                    self.request,
                    "La hora de fin debe ser posterior a la hora de inicio."
                )
                return super().form_invalid(form)

        # Validación de Reserva y BloqueoAgenda
        if 'fecha_inicio' in datos and 'fecha_fin' in datos:
            if datos['fecha_fin'] <= datos['fecha_inicio']:
                messages.error(
                    self.request,
                    "La fecha de fin debe ser posterior a la fecha de inicio."
                )
                return super().form_invalid(form)

        return super().form_valid(form)
