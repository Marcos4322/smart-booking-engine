from datetime import date, timedelta
from django.db.models import F
from billing.models import Cliente, Factura, Cobro


# UD3.6 - Funciones para realizar consultas y operaciones

def get_clientes_all():
    """1. Devuelve un queryset con todos los clientes."""
    return Cliente.objects.all()

def get_factura_first_3():
    """2. Devuelve un queryset con las 3 primeras facturas."""
    return Factura.objects.all()[:3]

def get_factura_0():
    """3. Devuelve un queryset con las facturas de importe 0."""
    return Factura.objects.filter(total=0)

def get_cliente_not_0612():
    """4. Devuelve un queryset con todos los clientes, excluyendo aquellos cuyo DNI empiece por '74'."""
    return Cliente.objects.exclude(nif__startswith="74")

def get_cliente_dni_apellido():
    """5. Devuelve un queryset de los clientes cuyo DNI sea '92436593F' y que en los apellidos contenga 'Pérez'."""
    return Cliente.objects.filter(nif='92436593F', apellidos__icontains="Pérez")

def get_cli_id_lt_2_num_fact_des():
    """6. Devuelve un queryset de las facturas cuyo id sea menor a 2, ordenadas por número de factura descendente."""
    return Factura.objects.filter(id__lt=2).order_by('-numero_factura')

def get_cli_id_gt_2():
    """7. Devuelve un queryset de los clientes cuyo id sea mayor a 2."""
    return Cliente.objects.filter(id__gt=2)

def get_fact_des_nom_des():
    """8. Devuelve un queryset con las facturas que contienen en el concepto 'PHP', ordenadas por número de factura ascendente."""
    return Factura.objects.filter(concepto__icontains="PHP").order_by('numero_factura')

def get_fact_not_1():
    """9. Devuelve un queryset con todas las facturas, excluyendo aquellas cuyo número de factura acabe en '1'."""
    return Factura.objects.exclude(numero_factura__endswith="1")

def get_cobro_python_id2():
    """10. Devuelve el primer objeto (no queryset) de Cobro cuya factura asociada contenga 'python' y cuyo id acabe en '2'."""
    return Cobro.objects.filter(factura__concepto__icontains="python", id__regex=r'2$').first()

def get_cobro_fact6_not_manu():
    """11. Devuelve un queryset con cobros cuya factura contenga '06'. Excluye al cliente cuyo nombre contenga 'Manu'."""
    return Cobro.objects.filter(factura__numero_factura__icontains="06").exclude(factura__cliente__nombre__icontains="Manu")

def get_fact_gt_5():
    """12. Devuelve un queryset de las facturas con un importe mayor o igual a 5."""
    return Factura.objects.filter(total__gte=5)

def get_cobro_5_10():
    """13. Devuelve un queryset de los cobros con un importe entre 5 y 10."""
    return Cobro.objects.filter(importe__gte=5, importe__lte=10)

def create_cliente():
    """14. Crea un cliente con nombre 'Nuevo', apellidos 'apellido1 apellido2', y un NIF válido."""
    cliente, created = Cliente.objects.get_or_create(
        nif="88888888X",
        defaults={
            "nombre": "Nuevo",
            "apellidos": "apellido1 apellido2",
            "email": "nuevo.cliente@bookflow.com"
        }
    )
    if not created:
        cliente.nombre = "Nuevo"
        cliente.apellidos = "apellido1 apellido2"
        cliente.save()
    return cliente

def create_factura():
    """15. Crea una nueva factura para el cliente del ejercicio anterior, fecha ayer e importe 100."""
    cliente = create_cliente()
    ayer = date.today() - timedelta(days=1)
    import time
    num_fact = f"FAC-{int(time.time())}"
    return Factura.objects.create(
        cliente=cliente,
        numero_factura=num_fact,
        concepto="Factura de prueba ORM",
        fecha=ayer,
        total=100.00
    )

def update_last_factura():
    """16. Modifica el concepto de la última factura para concatenar el texto '(última)'."""
    factura = Factura.objects.last()
    if factura:
        if "(última)" not in factura.concepto:
            factura.concepto += " (última)"
            factura.save()
        return factura
    return None

def update_cobro_fact2_x2():
    """17. Modifica los importes de los cobros de facturas cuyo número acabe en '2', multiplicándolos por 2."""
    return Cobro.objects.filter(factura__numero_factura__endswith="2").update(importe=F('importe') * 2)

def update_cobro_fact1_cligonz_div2():
    """18. Modifica los importes de cobros de facturas cuyo número acabe en '1' y cliente contenga 'González', dividiéndolos por 2."""
    return Cobro.objects.filter(factura__numero_factura__endswith="1", factura__cliente__apellidos__icontains="González").update(importe=F('importe') / 2)

def delete_cobro_fact_lt_1():
    """19. Eliminar los cobros cuyas facturas tengan un importe menor a 1."""
    return Cobro.objects.filter(factura__total__lt=1).delete()

def delete_cobro_cli_pablo():
    """20. Elimina los cobros de las facturas cuyo cliente contenga 'Pablo' en el nombre."""
    return Cobro.objects.filter(factura__cliente__nombre__icontains="Pablo").delete()