from django.shortcuts import render
from django.views.generic import ListView, DetailView
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
