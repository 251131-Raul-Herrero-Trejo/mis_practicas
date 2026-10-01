def mostrar_encabezado_escuela():
    print("==============================================")
    print("UNIVERSIDAD TECNOLOGICA DE XICOTEPEC DE JUAREZ")
    print("           REPORTE DE CALIFICACIONES          ")
    print("==============================================")


def obtener_nota_minima_aprobatoria():
    return 6.0

def evaluar_rendimiento(nota_final):
    if nota_final < 7:
        return "Reprobado"
    elif 7<= nota_final <= 9.4:
        return "Aprobado"
    else:
        return "Excelente"        

def calcular_promedio_ponderado(nota_examanes, nota_tareas):
    promedio = (nota_examanes*0.70)+(nota_tareas*0.30)
    return round (promedio, 1)

def generar_boleta(nombre_alumno, nota_examanes, nota_tareas):
    mostrar_encabezado_escuela()

    nota_final = calcular_promedio_ponderado(nota_examanes, nota_tareas)
    nota_minima = obtener_nota_minima_aprobatoria()
    rendimiento = evaluar_rendimiento(nota_final)
    extraordinario = "Si" if nota_final < nota_minima else "No"

    print(f"Nombre del alumno: {nombre_alumno}")
    print(f"Nota final       : {nota_final}")
    print(f"Rendimiento      : {rendimiento}")
    print(f"¿Requiere Extra? : {extraordinario}")
    
generar_boleta("Carlos Garrido", 9.0, 10.0)
generar_boleta("Francisco Capultitla", 6.0, 9.0)
generar_boleta("Alfredo Olivas", 4.0, 7.0)


