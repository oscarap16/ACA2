from django.shortcuts import render
from django.db.models import Count, Sum

from .models import Clientes, Pedidos, Productos, Pagos, DetallePedidos


def index(request):
    # =========================
    # 1) LEER FILTROS (GET)
    # =========================
    ciudad = request.GET.get("ciudad", "").strip()
    categoria = request.GET.get("categoria", "").strip()

    # =========================
    # 2) LISTAS PARA LOS SELECTS
    # =========================
    ciudades = (
        Clientes.objects.values_list("ciudad", flat=True)
        .distinct()
        .order_by("ciudad")
    )

    categorias = (
        Productos.objects.values_list("categoria", flat=True)
        .distinct()
        .order_by("categoria")
    )

    # =========================
    # 3) QUERY BASE (APLICAR FILTRO GLOBAL DE CIUDAD)
    # =========================
    clientes_qs = Clientes.objects.all()

    if ciudad:
        clientes_qs = clientes_qs.filter(ciudad=ciudad)

    # IDs de clientes filtrados (sirven para filtrar pedidos)
    clientes_ids = list(clientes_qs.values_list("cliente_id", flat=True))

    pedidos_qs = Pedidos.objects.all()
    if ciudad:
        pedidos_qs = pedidos_qs.filter(cliente_id__in=clientes_ids)

    # IDs de pedidos filtrados (sirven para filtrar detalle y productos)
    pedidos_ids = list(pedidos_qs.values_list("pedido_id", flat=True))

    # =========================
    # 4) TABLAS (MUESTRA)
    # =========================
    clientes = clientes_qs[:10]
    pedidos = pedidos_qs[:10]
    productos = Productos.objects.all()[:10]
    pagos = Pagos.objects.all()[:10]
    detalle_pedidos = DetallePedidos.objects.all()[:10]

    # =========================
    # 5) KPIs (RESPETAN CIUDAD)
    # =========================
    total_clientes = clientes_qs.count()
    total_pedidos = pedidos_qs.count()
    suma_subtotal = pedidos_qs.aggregate(s=Sum("subtotal"))["s"] or 0
    suma_envio = pedidos_qs.aggregate(s=Sum("costo_envio"))["s"] or 0

    # =========================
    # 6) GRAFICO 1: CLIENTES POR CIUDAD
    # (cuando hay filtro de ciudad, igual te lo deja para comparar;
    #  si prefieres que muestre solo 1 barra, lo ajustamos)
    # =========================
    clientes_por_ciudad = list(
        Clientes.objects.values("ciudad")
        .annotate(total=Count("cliente_id"))
        .order_by("-total")
    )

    # =========================
    # 7) GRAFICO 2: PEDIDOS POR ESTADO (RESPETA CIUDAD)
    # =========================
    pedidos_por_estado = list(
        pedidos_qs.values("estado")
        .annotate(total=Count("pedido_id"))
        .order_by("-total")
    )

    # =========================
    # 8) GRAFICO 3: PRODUCTOS POR CATEGORIA (RESPETA CIUDAD + FILTRO CATEGORIA)
    #
    # Idea:
    # - Si hay ciudad: tomamos pedidos de esos clientes -> detalles -> productos usados
    # - Si además hay "categoria": filtramos esa categoría
    # =========================
    productos_qs = Productos.objects.all()

    if categoria:
        productos_qs = productos_qs.filter(categoria=categoria)

    if ciudad:
        # Detalles que pertenecen a pedidos de la ciudad
        detalle_qs = DetallePedidos.objects.filter(pedido_id__in=pedidos_ids)
        producto_ids_usados = list(detalle_qs.values_list("producto_id", flat=True).distinct())
        productos_qs = productos_qs.filter(producto_id__in=producto_ids_usados)

    productos_por_categoria = list(
        productos_qs.values("categoria")
        .annotate(total=Count("producto_id"))
        .order_by("-total")
    )

    # =========================
    # 9) CONTEXT
    # =========================
    context = {
        # filtros seleccionados
        "ciudad_seleccionada": ciudad,
        "categoria_seleccionada": categoria,

        # opciones de selects
        "ciudades": ciudades,
        "categorias": categorias,

        # tablas
        "clientes": clientes,
        "pedidos": pedidos,
        "productos": productos,
        "pagos": pagos,
        "detalle_pedidos": detalle_pedidos,

        # KPIs
        "total_clientes": total_clientes,
        "total_pedidos": total_pedidos,
        "suma_subtotal": suma_subtotal,
        "suma_envio": suma_envio,

        # graficos
        "clientes_por_ciudad": clientes_por_ciudad,
        "pedidos_por_estado": pedidos_por_estado,
        "productos_por_categoria": productos_por_categoria,
    }

    return render(request, "index.html", context)




