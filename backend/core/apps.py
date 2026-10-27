from django.apps import AppConfig



# UD3.4d - Configuración de la aplicación principal de BookFlow
class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = 'Gestión de reservas'  # UD3.4d - Nombre visible de la aplicación en el administrador