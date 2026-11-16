from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from common.mixins import CreateUpdateContextMixin, DeleteDependencyMixin, CobroMixin
from billing.models import Cliente, Factura, Cobro
from django.contrib import messages
from .forms import ClienteForm, FacturaForm, CobroForm

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
class ClienteCreateView(CreateUpdateContextMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'base_create_update.html'
    success_url = 'cliente_update'

    titulo_creacion = 'Crear cliente'
    titulo_actualizacion = None
    url_borrado = None

    success_message = "Cliente creado correctamente"

class ClienteUpdateView(CreateUpdateContextMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'base_create_update.html'
    success_url = 'cliente_update'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar cliente'
    url_borrado = 'cliente_delete'


    success_message = "Cliente actualizado correctamente"

# UD4.2e - Variables de contexto para eliminar Cliente
# UD4.2f - Comprobación de dependencias de Cliente
class ClienteDeleteView(DeleteDependencyMixin, DeleteView):
    model = Cliente
    template_name = 'common/base_confirm_delete.html'
    success_url = 'cliente_list'

    titulo = 'Eliminar cliente'
    mensaje_confirmación = '¿Está seguro de que desea eliminar este cliente?'


# UD4.2a - Vistas de creación y actualización de Factura
# UD4.2d - Aplicación del Mixin de contexto a las vistas de Factura
# UD4.4a - Mensajes de éxito en las vistas de creación y actualización
class FacturaCreateView(CreateUpdateContextMixin, CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'base_create_update.html'
    success_url = 'factura_update'

    titulo_creacion = 'Crear factura'
    titulo_actualizacion = None
    url_borrado = None

    success_message = "Factura creada correctamente"


class FacturaUpdateView(CreateUpdateContextMixin, UpdateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'base_create_update.html'
    success_url = 'factura_update'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar factura'
    url_borrado = 'factura_delete'

    success_message = "Factura actualizada correctamente"

# UD4.2e - Variables de contexto para eliminar Factura
# UD4.2f - Comprobación de dependencias de Factura
class FacturaDeleteView(DeleteDependencyMixin,DeleteView):
    model = Factura
    template_name = 'common/base_confirm_delete.html'
    success_url = 'factura_list'

    titulo = 'Eliminar factura'
    mensaje_confirmación = '¿Está seguro de que desea eliminar esta factura?'


# UD4.2a - Vistas de creación y actualización de Cobro
# UD4.2d - Aplicación del Mixin de contexto a las vistas de Cobro
# UD4.4a - Mensajes de éxito en las vistas de creación y actualización
class CobroCreateView(CobroMixin, CreateUpdateContextMixin, CreateView):
    model = Cobro
    form_class = CobroForm
    template_name = 'base_create_update.html'
    success_url = 'cobro_update'

    titulo_creacion = 'Crear cobro'
    titulo_actualizacion = None
    url_borrado = None

    success_message = "Cobro creado correctamente"


class CobroUpdateView(CobroMixin, CreateUpdateContextMixin, UpdateView):
    model = Cobro
    form_class = CobroForm
    template_name = 'base_create_update.html'
    success_url = 'cobro_update'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar cobro'
    url_borrado = 'cobro_delete'

    success_message = "Cobro actualizado correctamente"


# UD4.2e - Variables de contexto para eliminar Cobro
class CobroDeleteView(DeleteView):
    model = Cobro
    template_name = 'base_confirm_delete.html'
    success_url = 'cobro_list'

    titulo = 'Eliminar cobro'
    mensaje_confirmación = '¿Está seguro de que desea eliminar este cobro?'