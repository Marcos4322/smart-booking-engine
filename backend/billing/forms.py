from django import forms
from .models import Cliente, Factura, Cobro

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, HTML


# UD4.3a - Formulario del modelo Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos', 'nif', 'email']

    # UD4.4c - Configuración del helper y layout
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4d - Layout del formulario Cliente
        self.helper.layout = Layout(
            Div(
                Div(Field('nombre'), css_class="col-3"),
                Div(Field('apellidos'), css_class="col-6"),
                Div(Field('nif'), css_class="col-3"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Field('email'),
            ),
        )

# UD4.3a - Formulario del modelo Factura
class FacturaForm(forms.ModelForm):

    class Meta:
        model = Factura
        fields = ['cliente', 'numero_factura', 'concepto', 'fecha', 'total']

    # UD4.3b - Validación del total de la factura
    def clean(self):
        cleaned_data = super().clean()
        total = cleaned_data.get('total')

        if total is not None and total <= 0:
            self.add_error('total', 'El importe debe ser mayor que 0.')

        return cleaned_data

    # UD4.4c - Configuración del helper y layout
    def __init__(self, *args, **kwargs):
        super(FacturaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4d - Layout del formulario Factura
        self.helper.layout = Layout(
            Div(
                Field('cliente'),
            ),
            HTML('<hr>'),
            Div(
                Div(Field('numero_factura'), css_class="col-4"),
                Div(Field('fecha'), css_class="col-4"),
                Div(Field('total'), css_class="col-4"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Field('concepto'),
            ),
        )

# UD4.3a - Formulario del modelo Cobro
class CobroForm(forms.ModelForm):

    class Meta:
        model = Cobro
        fields = ['factura', 'fecha', 'importe']

    # UD4.3b - Validación del importe del cobro
    def clean(self):
        cleaned_data = super().clean()
        importe = cleaned_data.get('importe')

        if importe is not None and importe <= 0:
            self.add_error('importe', 'El importe debe ser mayor que 0.')

        return cleaned_data

    # UD4.4c - Configuración del helper y layout
    def __init__(self, *args, **kwargs):
        super(CobroForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4d - Layout del formulario Cobro
        self.helper.layout = Layout(
            Div(
                Field('factura'),
            ),
            HTML('<hr>'),
            Div(
                Div(Field('fecha'), css_class="col-6"),
                Div(Field('importe'), css_class="col-6"),
                css_class="row"
            ),
        )