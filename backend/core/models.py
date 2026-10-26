from django.db import models

# UD3.3a - Definición de los 5 modelos principales de la app Core

# Modelo Profesional
class Profesional(models.Model):
    # # UD3.3c - Restricción única en email
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellidos = models.CharField(max_length=150, verbose_name="Apellidos")
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono", null=True, blank=True)
    activo = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Profesional"
        verbose_name_plural = "Profesionales"
        ordering = ["apellidos", "nombre"]

    # # UD3.3b - Representación textual del modelo Profesional
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


# Modelo Servicio
class Servicio(models.Model):
    profesionales = models.ManyToManyField(
        Profesional,
        related_name="servicios",
        verbose_name="Profesionales"
    )
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción", blank=True)
    duracion = models.PositiveIntegerField(verbose_name="Duración (minutos)")
    precio = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio (€)")
    activo = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["nombre"]

    # # UD3.3b - Representación textual del modelo Servicio
    def __str__(self):
        return f"{self.nombre} ({str(self.precio)}€)"


# Modelo HorarioLaboral
class HorarioLaboral(models.Model):
    DIAS_SEMANA = [
        (0, "Lunes"),
        (1, "Martes"),
        (2, "Miércoles"),
        (3, "Jueves"),
        (4, "Viernes"),
        (5, "Sábado"),
        (6, "Domingo"),
    ]

    profesional = models.ForeignKey(
        Profesional,
        on_delete=models.CASCADE,
        related_name="horarios",
        verbose_name="Profesional"
    )
    dia_semana = models.IntegerField(choices=DIAS_SEMANA, verbose_name="Día de la semana")
    hora_inicio = models.TimeField(verbose_name="Hora de inicio")
    hora_fin = models.TimeField(verbose_name="Hora de fin")

    class Meta:
        verbose_name = "Horario laboral"
        verbose_name_plural = "Horarios laborales"
        ordering = ["dia_semana", "hora_inicio"]
        # # UD3.3c - Restricción de clave única compuesta para evitar solapamientos
        unique_together = [("profesional", "dia_semana", "hora_inicio", "hora_fin")]

    # # UD3.3b - Representación textual del modelo HorarioLaboral
    def __str__(self):
        return f"{str(self.profesional)} - {self.get_dia_semana_display()} ({str(self.hora_inicio)} - {str(self.hora_fin)})"


# Modelo Reserva
class Reserva(models.Model):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("confirmada", "Confirmada"),
        ("completada", "Completada"),
        ("cancelada", "Cancelada"),
    ]

    # Enlace directo con el modelo Cliente de billing
    cliente = models.ForeignKey(
        'billing.Cliente',
        on_delete=models.PROTECT,
        related_name="reservas",
        verbose_name="Cliente"
    )
    profesional = models.ForeignKey(
        Profesional,
        on_delete=models.PROTECT,
        related_name="reservas",
        verbose_name="Profesional"
    )
    servicio = models.ForeignKey(
        Servicio,
        on_delete=models.PROTECT,
        related_name="reservas",
        verbose_name="Servicio"
    )
    fecha_inicio = models.DateTimeField(verbose_name="Inicio de la reserva")
    fecha_fin = models.DateTimeField(verbose_name="Fin de la reserva")
    estado = models.CharField(max_length=20, choices=ESTADOS, default="pendiente", verbose_name="Estado")
    
    # # UD3.3c - Restricción de clave única en token_qr
    token_qr = models.PositiveIntegerField(
        unique=True,
        blank=True,
        null=True,
        editable=False,
        verbose_name="ID de validación QR"
    )
    validada = models.BooleanField(default=False, verbose_name="Reserva validada")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["-fecha_inicio"]

    # # UD3.3b - Representación textual del modelo Reserva
    def __str__(self):
        return f"{str(self.cliente)} - {str(self.fecha_inicio)}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.token_qr:
            self.token_qr = self.id
            super().save(update_fields=['token_qr'])


# Modelo BloqueoAgenda
class BloqueoAgenda(models.Model):
    profesional = models.ForeignKey(
        Profesional,
        on_delete=models.CASCADE,
        related_name="bloqueos",
        verbose_name="Profesional"
    )
    fecha_inicio = models.DateTimeField(verbose_name="Inicio del bloqueo")
    fecha_fin = models.DateTimeField(verbose_name="Fin del bloqueo")
    motivo = models.CharField(max_length=200, verbose_name="Motivo")

    class Meta:
        verbose_name = "Bloqueo de agenda"
        verbose_name_plural = "Bloqueos de agenda"
        ordering = ["fecha_inicio"]

    # # UD3.3b - Representación textual del modelo BloqueoAgenda
    def __str__(self):
        return f"{str(self.profesional)} - {self.motivo} ({str(self.fecha_inicio)})"