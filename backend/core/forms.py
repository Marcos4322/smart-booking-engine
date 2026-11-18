from django import forms
from .models import Profesional, Servicio, HorarioLaboral, Reserva, BloqueoAgenda

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, HTML


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

    # UD4.4c - Configuración del helper y layout
    def __init__(self, *args, **kwargs):
        super(ProfesionalForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4e - Layout del formulario Profesional
        self.helper.layout = Layout(
            Div(
                Div(Field('nombre'), css_class="col-6"),
                Div(Field('apellidos'), css_class="col-6"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('email'), css_class="col-6"),
                Div(Field('telefono'), css_class="col-6"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Field('activo'),
            ),
        )


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

    # UD4.4c - Configuración del helper y layout
    def __init__(self, *args, **kwargs):
        super(ServicioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4e - Layout del formulario Servicio
        self.helper.layout = Layout(
            Div(
                Field('nombre'),
                Field('descripcion'),
            ),
            HTML('<hr>'),
            Div(
                Div(Field('profesionales'), css_class="col-6"),
                Div(Field('duracion'), css_class="col-3"),
                Div(Field('precio'), css_class="col-3"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Field('activo'),
            ),
        )


# UD4.3a - Formulario del modelo HorarioLaboral
class HorarioLaboralForm(forms.ModelForm):

    class Meta:
        model = HorarioLaboral
        fields = ['profesional', 'dia_semana', 'hora_inicio', 'hora_fin']

    # UD4.4c - Configuración del helper y layout
    def __init__(self, *args, **kwargs):
        super(HorarioLaboralForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4e - Layout del formulario HorarioLaboral
        self.helper.layout = Layout(
            Div(
                Field('profesional'),
            ),
            HTML('<hr>'),
            Div(
                Div(Field('dia_semana'), css_class="col-4"),
                Div(Field('hora_inicio'), css_class="col-4"),
                Div(Field('hora_fin'), css_class="col-4"),
                css_class="row"
            ),
        )


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

    # UD4.4c - Configuración del helper y layout
    def __init__(self, *args, **kwargs):
        super(ReservaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4e - Layout del formulario Reserva
        self.helper.layout = Layout(
            Div(
                Div(Field('cliente'), css_class="col-6"),
                Div(Field('profesional'), css_class="col-6"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Field('servicio'),
            ),
            HTML('<hr>'),
            Div(
                Div(Field('fecha_inicio'), css_class="col-6"),
                Div(Field('fecha_fin'), css_class="col-6"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('estado'), css_class="col-6"),
                Div(Field('validada'), css_class="col-6"),
                css_class="row"
            ),
        )


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

    # UD4.4c - Configuración del helper y layout
    def __init__(self, *args, **kwargs):
        super(BloqueoAgendaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4e - Layout del formulario BloqueoAgenda
        self.helper.layout = Layout(
            Div(
                Field('profesional'),
            ),
            HTML('<hr>'),
            Div(
                Div(Field('fecha_inicio'), css_class="col-6"),
                Div(Field('fecha_fin'), css_class="col-6"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Field('motivo'),
            ),
        )