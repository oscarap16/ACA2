from django.db import models

class Clientes(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=30, blank=True, null=True)
    correo = models.CharField(max_length=30, blank=True, null=True)
    ciudad = models.CharField(max_length=20, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    valor_total_cliente = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = "clientes"


class Pedidos(models.Model):
    pedido_id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name="pedidos")
    fecha_pedido = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    cantidad_items = models.IntegerField(blank=True, null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    costo_envio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = "pedidos"


class Productos(models.Model):
    producto_id = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)

    class Meta:
        db_table = "productos"


class DetallePedidos(models.Model):
    detalle_id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE, related_name="detalles")
    producto = models.ForeignKey(Productos, on_delete=models.DO_NOTHING, related_name="detalles")
    cantidad = models.IntegerField(blank=True, null=True)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_agregado = models.DateField(blank=True, null=True)

    class Meta:
        db_table = "detalle_pedidos"


class Pagos(models.Model):
    pago_id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE, related_name="pagos")
    fecha_pago = models.DateField(blank=True, null=True)
    metodo_pago = models.CharField(max_length=40, blank=True, null=True)
    cuotas = models.IntegerField(blank=True, null=True)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    comision = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = "pagos"

