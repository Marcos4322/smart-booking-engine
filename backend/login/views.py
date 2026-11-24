from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect


# UD5.2.a - Vista para iniciar sesión
# Fuente: vídeo del profesor UD5.2
class LoginFormView(LoginView):

    template_name = 'login.html'

    # UD5.2.b - Comprobar si el usuario ya ha iniciado sesión
    # Fuente: vídeo del profesor
    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect('panel')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'

        return context