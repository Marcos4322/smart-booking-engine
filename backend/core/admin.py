from django.contrib import admin

# UD3.4c - Importación de los cinco modelos de la app core
from .models import Profesional, Servicio, HorarioLaboral, Reserva, BloqueoAgenda


# UD3.4c - Configuración del administrador de profesionales
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email', 'telefono', 'activo')  # UD3.4a - Datos principales del profesional
    list_display_links = ('nombre', 'apellidos')  # UD3.4a - Campos para abrir el detalle del profesional
    list_filter = ('activo',)  # UD3.4a - Filtra por estado activo
    search_fields = ('nombre', 'apellidos', 'email', 'telefono')  # UD3.4a - Busca por datos de contacto
    preserve_filters = True  # UD3.4a - Conserva los filtros al entrar y volver al listado


# UD3.4c - Configuración del administrador de servicios
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'duracion', 'precio', 'activo')  # UD3.4a - Datos principales del servicio
    list_display_links = ('nombre',)  # UD3.4a - Permite abrir el detalle desde el nombre
    list_filter = ('activo', 'profesionales')  # UD3.4a - Filtra por estado y profesional asociado
    search_fields = (
        'nombre',
        'descripcion',
        'profesionales__nombre',
        'profesionales__apellidos',
    )  # UD3.4a - Busca por servicio, descripción o profesional
    preserve_filters = True  # UD3.4a - Conserva los filtros al entrar y volver al listado


# UD3.4c - Configuración del administrador de horarios laborales
class HorarioLaboralAdmin(admin.ModelAdmin):
    list_display = ('profesional', 'dia_semana', 'hora_inicio', 'hora_fin')  # UD3.4a - Datos principales del horario
    list_display_links = ('profesional', 'dia_semana')  # UD3.4a - Campos para abrir el detalle del horario
    list_filter = ('dia_semana', 'profesional')  # UD3.4a - Filtra por día y profesional
    search_fields = (
        'profesional__nombre',
        'profesional__apellidos',
    )  # UD3.4a - Busca por nombre o apellidos del profesional
    preserve_filters = True  # UD3.4a - Conserva los filtros al entrar y volver al listado


# UD3.4c - Configuración del administrador de reservas
class ReservaAdmin(admin.ModelAdmin):
    list_display = (
        'cliente',
        'profesional',
        'servicio',
        'fecha_inicio',
        'fecha_fin',
        'estado',
        'validada',
    )  # UD3.4a - Muestra los participantes, el horario y el estado de la reserva
    list_display_links = ('cliente', 'fecha_inicio')  # UD3.4a - Campos para abrir el detalle de la reserva
    list_filter = (
        'estado',
        'validada',
        'profesional',
        'servicio',
    )  # UD3.4a - Filtra por estado, validación, profesional y servicio
    search_fields = (
        'cliente__nombre',
        'cliente__apellidos',
        'cliente__nif',
        'profesional__nombre',
        'profesional__apellidos',
        'servicio__nombre',
    )  # UD3.4a - Busca por cliente, profesional o servicio
    preserve_filters = True  # UD3.4a - Conserva los filtros al entrar y volver al listado


# UD3.4c - Configuración del administrador de bloqueos de agenda
class BloqueoAgendaAdmin(admin.ModelAdmin):
    list_display = ('profesional', 'fecha_inicio', 'fecha_fin', 'motivo')  # UD3.4a - Datos principales del bloqueo
    list_display_links = ('profesional', 'fecha_inicio')  # UD3.4a - Campos para abrir el detalle del bloqueo
    list_filter = ('profesional',)  # UD3.4a - Filtra los bloqueos por profesional
    search_fields = (
        'profesional__nombre',
        'profesional__apellidos',
        'motivo',
    )  # UD3.4a - Busca por profesional o motivo del bloqueo
    preserve_filters = True  # UD3.4a - Conserva los filtros al entrar y volver al listado


# UD3.4c - Registro de los cinco modelos en el administrador
admin.site.register(Profesional, ProfesionalAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(HorarioLaboral, HorarioLaboralAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(BloqueoAgenda, BloqueoAgendaAdmin)
