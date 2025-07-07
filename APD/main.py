from salas.inicio import iniciar_juego
from salas.preparacion import ingreso_individual
from salas.juego import *
from salas.resumen import resumen

def juego():
    lista_jugadores = {}
    lista_por_sala = {}

    COLORES_SALAS = [[161, 147, 250], [37, 77, 112], [45, 79, 43], [82, 29, 68]]
    NIVEL_SALAS = ["1", "2", "3", "4"]

    TEXTO_PREGUNTA = [["Cual es el valor de", "len([10, 20, 30, 40])?"], ['Que imprime print("Hola"[1])?', ""], ["a = [2, 4, 6, 8]", "Cual es el valor de a[-2]?"], ["Cual es el resultado de", "5 > 3 and 2 < 4? True o False"]]

    POS_PREGUNTAS = [[220, 125, 222, 155],[130, 135, 0, 0],[120, 125, 122, 155],[120, 125, 122, 155]]

    RESPUESTA_CORRECTA = ["4", "o", "6", "true"]
    
    no_pasaron_primera = list()
    cantidad_incial_jugadores = 1
    cantidad_incial_jugadores = iniciar_juego(cantidad_incial_jugadores)
    
    for jugador in range(cantidad_incial_jugadores):
        completo = "No completo"
        info_jugador = []
        sala_finalizo = 0
        sigue = True
        puntaje_por_sala = [0,0,0,0]
        puntaje = 0
        nombre_jugador = ingreso_individual((120, 55, 12), jugador)
        i = 0
        while sigue and i < len(NIVEL_SALAS):
            resultado = sala(COLORES_SALAS[i], NIVEL_SALAS[i], TEXTO_PREGUNTA[i], POS_PREGUNTAS[i], RESPUESTA_CORRECTA[i])
            puntaje = resultado[0]
            sigue = resultado[1]
            if sigue == True:
                sala_finalizo += 1
                puntaje_por_sala[i] += puntaje
                i += 1

    if sala_finalizo > 1 and sala_finalizo <= 3:
        completo = "No completo"
    elif sala_finalizo == 4:
        completo = "Completo"
    else:
        completo = "No completo"
        no_pasaron_primera.append(nombre_jugador)
            

    lista_por_sala[f'{nombre_jugador}: '] = f'Sala: {sala_finalizo}'


    puntaje = puntaje_por_sala[0] + puntaje_por_sala[1] + puntaje_por_sala[2] + puntaje_por_sala[3]

    info_jugador.extend(puntaje_por_sala[:4])
    info_jugador.append(f"Total: {puntaje}")
    info_jugador.append(completo)

    lista_jugadores[f'{nombre_jugador}: '] = info_jugador
    resumen((120, 55, 12),lista_jugadores, lista_por_sala, no_pasaron_primera)

juego()