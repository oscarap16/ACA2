from django.shortcuts import render
from django.db.models import Count, Sum
from .models import Clientes, Pedidos, Productos, Pagos, DetallePedidos


def index(request):
    # ==========================
    # 1. Filtros (GET)
    # ==========================
    ciudad = (request.GET.get("ciudad") or "").strip()
    categoria = (request.GET.get("categoria") or "").strip()

    # ==========================
    # 2. QuerySets base
    # ==========================
    clientes_qs = Clientes.objects.all()
    pedidos_qs = Pedidos.objects.all()
    productos_qs = Productos.objects.all()
    pagos_qs = Pagos.objects.all()
    detalle_qs = DetallePedidos.objects.all()

    # ==========================
    # 3. Filtro global por CIUDAD
    # ==========================
    if ciudad:
        # Clientes de la ciudad
        cliente_ids = list(
            Clientes.objects
            .filter(ciudad=ciudad)
            .values_list("cliente_id", flat=True)
        )

        clientes_qs = clientes_qs.filter(ciudad=ciudad)
        pedidos_qs = pedidos_qs.filter(cliente_id__in=cliente_ids)

        # Pedidos filtrados (para pagos y detalle)
        pedido_ids = list(
            pedidos_qs.values_list("pedido_id", flat=True)
        )

        pagos_qs = pagos_qs.filter(pedido_id__in=pedido_ids)
        detalle_qs = detalle_qs.filter(pedido_id__in=pedido_ids)

    # ==========================
    # 4. Filtro por CATEGORIA
    # ==========================
    if categoria:
        productos_qs = productos_qs.filter(categoria=categoria)

    # ==========================
    # 5. Muestras para tablas
    # ==========================
    clientes = clientes_qs[:5]
    pedidos = pedidos_qs[:5]
    productos = productos_qs[:5]
    pagos = pagos_qs[:5]
    detalle_pedidos = detalle_qs[:5]

    # ==========================
    # 6. GRAFICOS
    # ==========================

    # Clientes por ciudad
    clientes_por_ciudad = list(
        clientes_qs
        .values("ciudad")
        .annotate(total=Count("cliente_id"))
        .order_by("-total")
    )

    # Pedidos por estado
    pedidos_por_estado = list(
        pedidos_qs
        .values("estado")
        .annotate(total=Count("pedido_id"))
        .order_by("-total")
    )

    # Productos por categoría
    productos_por_categoria = list(
        productos_qs
        .values("categoria")
        .annotate(total=Count("producto_id"))
        .order_by("-total")
    )

    # Pagos por método (Chart.js y Highcharts)
    pagos_por_metodo = list(
        pagos_qs
        .values("metodo_pago")
        .annotate(total=Count("pago_id"))
        .order_by("-total")
    )

    # ==========================
    # 7. KPIs
    # ==========================
    total_clientes = clientes_qs.count()
    total_pedidos = pedidos_qs.count()
    suma_subtotal = pedidos_qs.aggregate(s=Sum("subtotal"))["s"] or 0
    suma_envio = pedidos_qs.aggregate(s=Sum("costo_envio"))["s"] or 0

    # ==========================
    # 8. Opciones de filtros
    # ==========================
    ciudades_disponibles = list(
        Clientes.objects
        .values_list("ciudad", flat=True)
        .distinct()
        .order_by("ciudad")
    )

    categorias_disponibles = list(
        Productos.objects
        .values_list("categoria", flat=True)
        .distinct()
        .order_by("categoria")
    )

    # ==========================
    # 9. Contexto
    # ==========================
    context = {
        # tablas
        "clientes": clientes,
        "pedidos": pedidos,
        "productos": productos,
        "pagos": pagos,
        "detalle_pedidos": detalle_pedidos,

        # graficos
        "clientes_por_ciudad": clientes_por_ciudad,
        "pedidos_por_estado": pedidos_por_estado,
        "productos_por_categoria": productos_por_categoria,
        "pagos_por_metodo": pagos_por_metodo,

        # kpis
        "total_clientes": total_clientes,
        "total_pedidos": total_pedidos,
        "suma_subtotal": suma_subtotal,
        "suma_envio": suma_envio,

        # filtros
        "ciudad_seleccionada": ciudad,
        "categoria_seleccionada": categoria,
        "ciudades_disponibles": ciudades_disponibles,
        "categorias_disponibles": categorias_disponibles,
    }

    return render(request, "index.html", context)







