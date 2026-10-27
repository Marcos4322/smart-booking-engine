from django.apps import AppConfig


# UD3.4d - Configuración de la aplicación de facturación
class BillingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'billing'
    verbose_name = 'Facturación y cobros'  # UD3.4d - Nombre visible de la aplicación en el administrador