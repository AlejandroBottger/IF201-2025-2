def socio_mayor_mensualidad(arreglo):
    return max(arreglo, key=lambda s: s.mensualidad)

def socio_menor_mensualidad(arreglo):
    return min(arreglo, key=lambda s: s.mensualidad)

def promedio_por_plan(arreglo):
    dicc = {}
    for s in arreglo:
        dicc.setdefault(s.plan, []).append(s.mensualidad)
    return {p: sum(val) / len(val) for p, val in dicc.items()}

def plan_promedio_mas_bajo(promedios):
    return min(promedios, key=promedios.get)
