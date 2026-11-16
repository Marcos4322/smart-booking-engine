from django import forms
from .models import Cliente, Factura, Cobro


# UD4.3a - Formulario del modelo Cliente
class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos', 'nif', 'email']

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