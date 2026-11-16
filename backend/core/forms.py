
from django import forms
from .models import Profesional, Servicio, HorarioLaboral, Reserva, BloqueoAgenda


# UD4.3a - Formulario del modelo Profesional
# UD4.3c - Validación del teléfono
class ProfesionalForm(forms.ModelForm):

    class Meta:
        model = Profesional
        fields = ['nombre', 'apellidos', 'email', 'telefono', 'activo']

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')

        if telefono and len(telefono) < 9:
            raise forms.ValidationError(
                'El teléfono debe tener al menos 9 caracteres.'
            )

        return telefono


# UD4.3a - Formulario del modelo Servicio
# UD4.3c - Validación del precio
class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = ['profesionales', 'nombre', 'descripcion', 'duracion', 'precio', 'activo']

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')

        if precio is not None and precio <= 0:
            raise forms.ValidationError(
                'El precio debe ser mayor que 0.'
            )

        return precio


# UD4.3a - Formulario del modelo HorarioLaboral
class HorarioLaboralForm(forms.ModelForm):

    class Meta:
        model = HorarioLaboral
        fields = ['profesional', 'dia_semana', 'hora_inicio', 'hora_fin']


# UD4.3a - Formulario del modelo Reserva
class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = [
            'cliente',
            'profesional',
            'servicio',
            'fecha_inicio',
            'fecha_fin',
            'estado',
            'validada'
        ]


# UD4.3a - Formulario del modelo BloqueoAgenda
# UD4.3c - Validación del profesional activo
class BloqueoAgendaForm(forms.ModelForm):

    class Meta:
        model = BloqueoAgenda
        fields = ['profesional', 'fecha_inicio', 'fecha_fin', 'motivo']

    def clean_profesional(self):
        profesional = self.cleaned_data.get('profesional')

        if profesional and not profesional.activo:
            raise forms.ValidationError(
                'No se pueden crear bloqueos para profesionales inactivos.'
            )

        return profesional