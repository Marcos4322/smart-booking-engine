from django.urls import path
from .views import LoginFormView
from django.contrib.auth.views import LogoutView


# UD5.2.b - URL para mostrar el formulario de inicio de sesión
urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),

    # UD5.2.c - URL para cerrar la sesión
    path('logout/', LogoutView.as_view(), name='logout'),
]