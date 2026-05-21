
datos_sesiones = [
    [101, 220, 10],
    [102, 50, 2],
    [103, 150, 7],
    [104, 200, 9],
    [105, 70, 4],
    [106, 90, 2],
    [107, 300, 12]
]

def clasificar_compromiso(duracion, clics):
    """
    Calcula el nivel de compromiso según las reglas:
    - ALTO: Duración > 180s Y Clics > 8
    - BAJO: Duración < 60s O Clics < 3
    - MEDIO: Todo lo demás
    """

    if duracion > 180 and clics > 8:
        return "Alto"
    # Regla para BAJO
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


def generar_informe(sesiones):
    """Genera el reporte final con ID y Clasificación"""
    
    print("=" * 60)
    print("          INFORME DE COMPROMISO DE SESIONES          ")
    print("=" * 60)
    print(f"{'ID CLIENTE':<12} | {'DURACIÓN':<10} | {'CLICS':<6} | {'NIVEL':<10}")
    print("-" * 60)
    
    for sesion in sesiones:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]
        
        nivel = clasificar_compromiso(duracion, clics)
        
        print(f"{id_cliente:<12} | {duracion:<10} | {clics:<6} | {nivel:<10}")
    
    print("=" * 60)
    print("✅ Análisis completado según los requisitos.")
    print("=" * 60)


if __name__ == "__main__":
    generar_informe(datos_sesiones)