from django.contrib import admin

# UD3.4b - Importación de los modelos de facturación
from .models import Cliente, Factura, Cobro


# UD3.4b - Configuración del administrador de clientes
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'nif', 'email')  # UD3.4a - Columnas visibles en el listado
    list_display_links = ('nombre', 'apellidos', 'nif', 'email')  # UD3.4a - Campos que permiten abrir el detalle
    list_filter = ('nif',)  # UD3.4a - Filtro por NIF
    search_fields = ('nombre', 'apellidos', 'nif', 'email')  # UD3.4a - Campos incluidos en la búsqueda
    preserve_filters = True  # UD3.4a - Conserva los filtros al entrar y volver al listado


# UD3.4b - Configuración del administrador de facturas
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('numero_factura', 'fecha', 'total')  # UD3.4a - Columnas visibles en el listado
    list_display_links = ('numero_factura', 'fecha', 'total')  # UD3.4a - Campos que permiten abrir el detalle
    list_filter = ('cliente',)  # UD3.4a - Filtra las facturas por cliente
    search_fields = (
        'numero_factura',
        'cliente__nombre',
        'cliente__apellidos',
    )  # UD3.4a - Busca por número de factura y nombre o apellidos del cliente
    preserve_filters = True  # UD3.4a - Conserva los filtros al entrar y volver al listado


# UD3.4b - Configuración del administrador de cobros
class CobroAdmin(admin.ModelAdmin):
    list_display = ('factura', 'fecha', 'importe')  # UD3.4a - Columnas visibles en el listado
    list_display_links = ('factura', 'fecha', 'importe')  # UD3.4a - Campos que permiten abrir el detalle
    list_filter = ('factura__cliente',)  # UD3.4a - Filtra los cobros por el cliente de la factura
    search_fields = (
        'factura__numero_factura',
        'factura__cliente__nombre',
        'factura__cliente__apellidos',
    )  # UD3.4a - Busca por factura y por nombre o apellidos del cliente
    preserve_filters = True  # UD3.4a - Conserva los filtros al entrar y volver al listado


# UD3.4b - Registro de los modelos en el administrador
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Factura, FacturaAdmin)
admin.site.register(Cobro, CobroAdmin)

