import pygame

def resumen(color_fondo, lista_jugadores, lista_por_sala, no_pasaron_primera_lista):
    pygame.init()

    ANCHO_VENTANA = 800
    ALTO_VENTANA = 900
    fuente = pygame.font.Font("APD/archivos/Golden Age.ttf", 30)

    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Sala de Escape de Programación")

    flag_juego = True
    while flag_juego:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_juego = False

        pantalla.fill(color_fondo)

        ordenados = sorted(lista_jugadores.items(), key=lambda x: x[1][-1], reverse=True)

        y = 50
        for jugador, valores in ordenados:
            texto = f"{jugador}{' - '.join(str(v) for v in valores)}"
            render = fuente.render(texto, True, (255,255,255))
            pantalla.blit(render, (40, y))
            y += 50

        ordenados_lista = sorted(lista_por_sala.items(), key=lambda x: int(x[1].split()[-1]), reverse=True)
        top3 = ordenados_lista[0:3]

        y_lista_salas = 600
        for jugador in top3:
            texto_sala = f"{jugador}"
            render_sala = fuente.render(texto_sala, True, (255, 255, 255))
            pantalla.blit(render_sala, (40, y_lista_salas))
            y_lista_salas += 50

        jugador_no_paso = 600
        for jugador in no_pasaron_primera_lista:
            render_jugador = fuente.render(jugador, True, (255,255,255))
            pantalla.blit(render_jugador, (400, jugador_no_paso))
            jugador_no_paso += 50

        mejor_puntaje_fuente = pygame.font.Font("APD/archivos/Golden Age.ttf", 30)
        mejor_puntaje_texto = mejor_puntaje_fuente.render("Llegaron mas lejos", True, (255,255,255))
        no_pasaron_primera = mejor_puntaje_fuente.render("No superaron la sala 1", True, (255,255,255))
        pantalla.blit(mejor_puntaje_texto, (40, 560))
        pantalla.blit(no_pasaron_primera, (400 ,560))

        pygame.display.flip()