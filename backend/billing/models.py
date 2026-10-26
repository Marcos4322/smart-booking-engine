from django.db import models
from django.utils.timezone import now

# UD3.3a - Definición de modelos para la app Billing

# Representa la entidad Cliente para facturación
class Cliente(models.Model):
    # # UD3.3c - Restricción única en nif y email
    nombre = models.CharField(max_length=256, verbose_name="Nombre")
    apellidos = models.CharField(max_length=512, verbose_name="Apellidos")
    nif = models.CharField(max_length=20, unique=True, verbose_name="NIF")
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    # # UD3.3b - Representación textual del modelo Cliente
    def __str__(self):
        return f"{self.nombre} {self.apellidos} ({self.nif})"


# Representa el documento mercantil de facturación
class Factura(models.Model):
    # # UD3.3c - Restricción única en numero_factura
    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.PROTECT, 
        related_name="facturas", 
        verbose_name="Cliente"
    )
    numero_factura = models.CharField(max_length=20, unique=True, verbose_name="N.º factura")
    concepto = models.TextField(verbose_name="Concepto")
    fecha = models.DateField(default=now, verbose_name="Fecha")
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Total (€)")

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"

    # # UD3.3b - Representación textual del modelo Factura
    def __str__(self):
        return f"{str(self.cliente)} - {self.numero_factura}"


# Registra los cobros asociados a cada factura
class Cobro(models.Model):
    factura = models.ForeignKey(
        Factura, 
        on_delete=models.PROTECT, 
        related_name="cobros", 
        verbose_name="Factura"
    )
    fecha = models.DateField(default=now, verbose_name="Fecha de cobro")
    importe = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Importe (€)")

    class Meta:
        verbose_name = "Cobro"
        verbose_name_plural = "Cobros"

    # # UD3.3b - Representación textual del modelo Cobro
    def __str__(self):
        return f"{self.factura.numero_factura} - {str(self.importe)}"