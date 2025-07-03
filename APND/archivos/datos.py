import random
import csv

def ingreso_individual(lista_jugadores):
    nombre_jugador = input(f"Ingrese su nombre: ").strip()
    while len(nombre_jugador) < 1:
        nombre_jugador = input(f"Ingrese un nombre válido: ")
    lista_jugadores.append(nombre_jugador)
    return lista_jugadores, nombre_jugador

def salas():
    print(f'Bienvenido a "Sala de Escape de Programación".\nEsto consta de 4 niveles. Tenés que responder la pregunta correctamente para avanzar, tenés solo 2 intentos por sala y un tiempo de 1 minuto.')
    preparado = False
    while preparado == False:
        pregunta_preparado = input("Estas listo(S/N)?").upper()
        if pregunta_preparado == 'N':
            print("Preparate bien y cuando quieras comenzamos!")
            pregunta_preparado = input("Estas listo(S/N)?").upper()
        else:
            print("Comencemos!")
            preparado = True

def cargar_respuestas(csv_path, nivel):
    respuestas = list()
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for _ in range(nivel):
            linea = next(reader)
            opciones = linea[1:]
            respuestas.clear()
            respuestas.extend(opciones)
        random.shuffle(respuestas)

    for res in enumerate(respuestas, 1):
        print(res)
    return respuestas

def cargar_preguntas(csv_path, nivel):
    preguntas = list()
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        nivel = next(reader)
        preg = nivel[1:]
        preguntas.clear()
        preguntas.extend(preg)
    return preguntas

def buscar_respuesta_correcta(respuestas, respuesta_correcta):
    encontrado = False
    i = 0
    while not encontrado and i < len(respuestas):
        if respuesta_correcta == respuestas[i]:
            respuesta_correcta = i+1
            encontrado = True
        else:
            i += 1
    return respuesta_correcta

def validar_respuesta(opcion_correcta):
    intentos = 2
    respuesta_correcta = False
    respuesta = int(input('Ingrese su respuesta(1-4): '))
    while intentos != 0 and not respuesta_correcta:
        if respuesta != opcion_correcta:
            intentos -= 1
            if intentos == 0:
                print("PERDISTE! VUELVE A INTENTARLO")
                respuesta_correcta = False
            else:
                print("INCORRECTO!")
                print(f"Te queda {intentos} intento")
                respuesta = int(input('Ingrese su respuesta(1-4): '))
        else:
            print("Opcion Correcta!\nAvanzando a la siguiente sala...")
            respuesta_correcta = True
    return respuesta_correcta

def jugar_nivel(nivel, respuesta):
    preguntas = cargar_preguntas('APND/archivos/preguntas.csv', nivel)
    print(f"----- Sala {nivel} -----")
    print(f"Pregunta: '{preguntas}'")
    respuestas = cargar_respuestas('APND/archivos/respuestas.csv', nivel)
    respuesta_correcta = buscar_respuesta_correcta(respuestas, respuesta)
    sigue = validar_respuesta(respuesta_correcta)
    return sigue


def escape(jugador):

    salas()

    cant_salas = 1
    no_paso_primera = False
    puntaje_por_sala = [0, 0, 0, 0, 0]
    completo = 'No Completó'
    print(f"Tu puntaje actual es: {puntaje_por_sala[4]}")
    print("-----Primera Sala-----")
    print("Pregunta: '¿Qué tipos de datos primitivos existen en Python?'")
    respuestas = cargar_respuestas('APND/archivos/respuestas.csv', 1)
    respuesta_correcta = buscar_respuesta_correcta(respuestas, "int / float / str / boolean")
    sigue = validar_respuesta(respuesta_correcta)


    if sigue == True:
        puntaje_por_sala[0] += 15
        puntaje_por_sala[4] += 15
        respuestas_correctas = ["int / float / str / boolean", "if x > 5: print('Mayor')", "Indicar que un directorio debe tratarse como un paquete de Python.", "copy() realiza una copia referencial al original y deepcopy() realiza una copia independiente"]
        i = 2
        while sigue and i <= 4:
            cant_salas += 1
            sigue = jugar_nivel(i, respuestas_correctas[i-1])
            if sigue:
                puntaje_por_sala[i-1] += 15
                puntaje_por_sala[4] += 15
                i += 1

            if i == 5:
                no_paso_primera = False
                completo = 'Completó'
            elif cant_salas >= 2 and cant_salas <= 3:
                no_paso_primera = False
                completo = 'No Completó'
    else:
        no_paso_primera = True

    print(f"Tu puntaje final es: {puntaje_por_sala[4]}")
    print("----- TABLA -----")
    print(f"{'Jugador':10} {'Sala 1':10} {'Sala 2':10} {'Sala 3':10} {'Sala 4':10} {'Total':10} {'Completo/No Completo':40}")
    print(f"{str(jugador):8} {puntaje_por_sala[0]:8} {puntaje_por_sala[1]:10} {puntaje_por_sala[2]:10} {puntaje_por_sala[3]:10} {puntaje_por_sala[4]:10} {completo:40}")
    return jugador, puntaje_por_sala,cant_salas, no_paso_primera


def mostrar_mayor_puntajes(tabla):
    print("----- TABLA GENERAL -----")
    print(f"{'Jugador':10} {'Sala 1':10} {'Sala 2':10} {'Sala 3':10} {'Sala 4':10} {'Total':10}")
    for jugador in tabla:
        nombre = jugador[0]
        datos = jugador[1]
        print(f"{nombre:<10} " + ' '.join(f"{str(dato):<10}" for dato in datos))


def mostrar_por_sala(tabla):
    tabla.sort(key=lambda x: x[1], reverse=True)
    print("----- TABLA POR SALAS -----")
    print(f"{'Jugador':10} {'Sala a la que llegó':10}")
    for jugador, sala in tabla:
        print(f"{jugador:10} {sala:<1}")

def mostrar_no_pasaron_primera(tabla):
    print("JUGADORES QUE NO PASARON LA PRIMERA SALA:")
    for jugador in tabla:
        print(jugador)