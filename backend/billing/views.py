from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from common.mixins import CreateUpdateContextMixin
from billing.models import Cliente, Factura, Cobro

# UD3.8.b - Listado de clientes con paginación

class ClienteListView(ListView):
    model = Cliente
    template_name = 'billing/cliente_list.html'
    paginate_by = 5


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'billing/cliente_detail.html'


class FacturaListView(ListView):
    model = Factura
    template_name = 'billing/factura_list.html'
    paginate_by = 5


class FacturaDetailView(DetailView):
    model = Factura
    template_name = 'billing/factura_detail.html'


class CobroListView(ListView):
    model = Cobro
    template_name = 'billing/cobro_list.html'
    paginate_by = 5


class CobroDetailView(DetailView):
    model = Cobro
    template_name = 'billing/cobro_detail.html'


# UD4.2a - Vistas de creación y actualización de Cliente
# UD4.2d - Aplicación del Mixin de contexto a las vistas de Cliente
class ClienteCreateView(CreateUpdateContextMixin, CreateView):
    model = Cliente
    template_name = 'base_create_update.html'
    success_url = 'cliente_update'

    titulo_creacion = 'Crear cliente'
    titulo_actualizacion = None
    url_borrado = None


class ClienteUpdateView(CreateUpdateContextMixin, UpdateView):
    model = Cliente
    template_name = 'base_create_update.html'
    success_url = 'cliente_update'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar cliente'
    url_borrado = 'cliente_delete'

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'base_confirm_delete.html'
    success_url = 'cliente_list'


# UD4.2a - Vistas de creación y actualización de Factura
# UD4.2d - Aplicación del Mixin de contexto a las vistas de Factura
class FacturaCreateView(CreateUpdateContextMixin, CreateView):
    model = Factura
    template_name = 'base_create_update.html'
    success_url = 'factura_update'

    titulo_creacion = 'Crear factura'
    titulo_actualizacion = None
    url_borrado = None


class FacturaUpdateView(CreateUpdateContextMixin, UpdateView):
    model = Factura
    template_name = 'base_create_update.html'
    success_url = 'factura_update'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar factura'
    url_borrado = 'factura_delete'


class FacturaDeleteView(DeleteView):
    model = Factura
    template_name = 'base_confirm_delete.html'
    success_url = 'factura_list'


# UD4.2a - Vistas de creación y actualización de Cobro
# UD4.2d - Aplicación del Mixin de contexto a las vistas de Cobro
class CobroCreateView(CreateUpdateContextMixin, CreateView):
    model = Cobro
    template_name = 'base_create_update.html'
    success_url = 'cobro_update'

    titulo_creacion = 'Crear cobro'
    titulo_actualizacion = None
    url_borrado = None


class CobroUpdateView(CreateUpdateContextMixin, UpdateView):
    model = Cobro
    template_name = 'base_create_update.html'
    success_url = 'cobro_update'

    titulo_creacion = None
    titulo_actualizacion = 'Actualizar cobro'
    url_borrado = 'cobro_delete'


class CobroDeleteView(DeleteView):
    model = Cobro
    template_name = 'base_confirm_delete.html'
    success_url = 'cobro_list'