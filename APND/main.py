from archivos.datos import *

def sala_de_escape():
    MAX_JUGADORES = 10
    lista_jugadores = [] # LISTA DONDE SE INTRODUCIRAN LOS JUGADORES
    tabla_general = [] # LISTA PARA EL RESUMEN DONDE MUESTRA A TODOS LOS JUGADORES
    tabla_salas = [] # LISTA PARA EL RESUMEN DONDE MUESTRA LOS PRIMEROS 3 Y SU CANTIDAD DE SALAS PASADAS
    lista_no_pasaron_sala1 = [] # LISTA PARA EL RESUMEN DONDE MUESTRA LOS QUE NO PASARON LA SALA 1
    cant_jugadores = int(input("Cantidad de jugadores(1-10): "))
    while cant_jugadores <= 0 or cant_jugadores > MAX_JUGADORES:
        cant_jugadores = input("Cantidad inválida. Ingrese una cantidad de jugadores entre 1 y 10: ")

    for jugador in range(cant_jugadores):
        tabla_jugador = [] # SE GUARDA EL NOMBRE CON CADA UNO DE LOS PUNTAJES INDIVIDUALMENTE
        tabla_sala_jugador = [] # SE GUARDA EL NOMBRE CON LA SALA EN LA QUE FINALIZÓ SU RECORRIDO
        lista_jugadores, jugador = ingreso_individual(lista_jugadores)
        nombre, puntaje_por_sala,cant_salas, no_paso_primera = escape(jugador)

        if no_paso_primera == True:
            lista_no_pasaron_sala1.append(nombre)
        
        # TABLA GENERAL
        tabla_jugador.append(nombre)
        tabla_jugador.append(puntaje_por_sala)
        tabla_general.append(tabla_jugador)

        # TABLA POR SALAS
        tabla_sala_jugador.append(nombre)
        tabla_sala_jugador.append(cant_salas)
        tabla_salas.append(tabla_sala_jugador)

        # TABLA NO LOGRARON PASAR LA PRIMERA SALA

    mostrar_mayor_puntajes(tabla_general)
    mostrar_por_sala(tabla_salas)
    mostrar_no_pasaron_primera(lista_no_pasaron_sala1)


sala_de_escape()