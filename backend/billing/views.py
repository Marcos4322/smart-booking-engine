
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from common.mixins import CreateUpdateContextMixin, DeleteDependencyMixin, CobroMixin
from billing.models import Cliente, Factura, Cobro
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ClienteForm, FacturaForm, CobroForm
from django.urls import reverse_lazy

# UD3.8.b - Listado de clientes con paginación

class ClienteListView(ListView):
    model = Cliente
    template_name = 'billing/cliente_list.html'
    paginate_by = 5

    # UD4.2i - Ordenación del listado de clientes
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', None)

        if ordering == 'asc':
            queryset = queryset.order_by('id')
        elif ordering == 'desc':
            queryset = queryset.order_by('-id')

        return queryset


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'billing/cliente_detail.html'


class FacturaListView(ListView):
    model = Factura
    template_name = 'billing/factura_list.html'
    paginate_by = 5

    # UD4.2i - Ordenación del listado de facturas
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', None)

        if ordering == 'asc':
            queryset = queryset.order_by('id')
        elif ordering == 'desc':
            queryset = queryset.order_by('-id')

        return queryset


class FacturaDetailView(DetailView):
    model = Factura
    template_name = 'billing/factura_detail.html'


class CobroListView(ListView):
    model = Cobro
    template_name = 'billing/cobro_list.html'
    paginate_by = 5

    # UD4.2i - Ordenación del listado de cobros
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', None)

        if ordering == 'asc':
            queryset = queryset.order_by('id')
        elif ordering == 'desc':
            queryset = queryset.order_by('-id')

        return queryset


class CobroDetailView(DetailView):
    model = Cobro
    template_name = 'billing/cobro_detail.html'


# UD4.2a - Vistas de creación y actualización de Cliente
# UD4.2d - Aplicación del Mixin de contexto a las vistas de Cliente
# UD4.4a - Mensajes de éxito en las vistas de creación y actualización
class ClienteCreateView(SuccessMessageMixin, CreateUpdateContextMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'common/base_create_update.html'

    titulo_creacion = 'Crear cliente'
    titulo_actualizacion = None
    url_borrado = None

    # UD4.4a - Mensaje de éxito con la representación textual del cliente
    def get_success_message(self, cleaned_data):
        return "Cliente '{}' creado correctamente".format(str(self.object))

    # UD4.2a - Redirección al formulario de actualización del cliente creado
    def get_success_url(self):
        return reverse_lazy('cliente_update', kwargs={'pk': self.object.pk})


class ClienteUpdateView(SuccessMessageMixin, CreateUpdateContextMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'common/base_create_update.html'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar cliente'
    url_borrado = 'cliente_delete'

    # UD4.4a - Mensaje de éxito con la representación textual del cliente
    def get_success_message(self, cleaned_data):
        return "Cliente '{}' actualizado correctamente".format(str(self.object))

    # UD4.2a - Redirección al formulario de actualización del cliente
    def get_success_url(self):
        return reverse_lazy('cliente_update', kwargs={'pk': self.object.pk})


# UD4.2e - Variables de contexto para eliminar Cliente
# UD4.2f - Comprobación de dependencias de Cliente
class ClienteDeleteView(DeleteDependencyMixin, DeleteView):
    model = Cliente
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')

    titulo = 'Eliminar cliente'
    mensaje_confirmación = '¿Está seguro de que desea eliminar este cliente?'


# UD4.2a - Vistas de creación y actualización de Factura
# UD4.2d - Aplicación del Mixin de contexto a las vistas de Factura
# UD4.4a - Mensajes de éxito en las vistas de creación y actualización
class FacturaCreateView(SuccessMessageMixin, CreateUpdateContextMixin, CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'common/base_create_update.html'

    titulo_creacion = 'Crear factura'
    titulo_actualizacion = None
    url_borrado = None

    # UD4.4a - Mensaje de éxito con la representación textual del factura
    def get_success_message(self, cleaned_data):
        return "Factura '{}' creada correctamente".format(str(self.object))

    # UD4.2a - Redirección al formulario de actualización de la factura creada
    def get_success_url(self):
        return reverse_lazy('factura_update', kwargs={'pk': self.object.pk})


class FacturaUpdateView(SuccessMessageMixin, CreateUpdateContextMixin, UpdateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'common/base_create_update.html'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar factura'
    url_borrado = 'factura_delete'

    # UD4.4a - Mensaje de éxito con la representación textual del factura
    def get_success_message(self, cleaned_data):
        return "Factura '{}' actualizada correctamente".format(str(self.object))

    # UD4.2a - Redirección al formulario de actualización de la factura
    def get_success_url(self):
        return reverse_lazy('factura_update', kwargs={'pk': self.object.pk})


# UD4.2e - Variables de contexto para eliminar Factura
# UD4.2f - Comprobación de dependencias de Factura
class FacturaDeleteView(DeleteDependencyMixin, DeleteView):
    model = Factura
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('factura_list')

    titulo = 'Eliminar factura'
    mensaje_confirmación = '¿Está seguro de que desea eliminar esta factura?'


# UD4.2a - Vistas de creación y actualización de Cobro
# UD4.2d - Aplicación del Mixin de contexto a las vistas de Cobro
# UD4.4a - Mensajes de éxito en las vistas de creación y actualización
class CobroCreateView(SuccessMessageMixin, CobroMixin, CreateUpdateContextMixin, CreateView):
    model = Cobro
    form_class = CobroForm
    template_name = 'common/base_create_update.html'

    titulo_creacion = 'Crear cobro'
    titulo_actualizacion = None
    url_borrado = None

    # UD4.4a - Mensaje de éxito con la representación textual del cobro
    def get_success_message(self, cleaned_data):
        return "Cobro '{}' creado correctamente".format(str(self.object))

    # UD4.2a - Redirección al formulario de actualización del cobro creado
    def get_success_url(self):
        return reverse_lazy('cobro_update', kwargs={'pk': self.object.pk})


class CobroUpdateView(SuccessMessageMixin, CobroMixin, CreateUpdateContextMixin, UpdateView):
    model = Cobro
    form_class = CobroForm
    template_name = 'common/base_create_update.html'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar cobro'
    url_borrado = 'cobro_delete'

    # UD4.4a - Mensaje de éxito con la representación textual del cobro
    def get_success_message(self, cleaned_data):
        return "Cobro '{}' actualizado correctamente".format(str(self.object))

    # UD4.2a - Redirección al formulario de actualización del cobro
    def get_success_url(self):
        return reverse_lazy('cobro_update', kwargs={'pk': self.object.pk})


# UD4.2e - Variables de contexto para eliminar Cobro
class CobroDeleteView(DeleteView):
    model = Cobro
    template_name = 'common/base_confirm_delete.html'
    success_url = reverse_lazy('cobro_list')

    titulo = 'Eliminar cobro'
    mensaje_confirmación = '¿Está seguro de que desea eliminar este cobro?'
