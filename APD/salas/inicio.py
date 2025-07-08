import pygame

def inicio_juego(cantidad_incial_jugadores):
    pygame.init()
    # VARIABLES
    ANCHO_VENTANA = 800
    ALTO_VENTANA = 800
    COLOR_BLANCO = (255, 255, 255)
    COLOR_FONDO = (120, 55, 12)

    fuente_bienvenido = pygame.font.Font("APD/archivos/Golden Age.ttf",60)
    bienvenido = fuente_bienvenido.render("BIENVENIDO", True, COLOR_BLANCO)
    ingreso_rect = pygame.Rect(100, 200, 150, 40)

    fuente_subtitulo = pygame.font.Font("APD/archivos/Golden Age Shad.ttf", 30)
    subtitulo_juego = fuente_subtitulo.render("Sala de Escape de Programacion", True, COLOR_BLANCO)

    fuente_contador = pygame.font.Font("APD/archivos/Golden Age Shad.ttf", 70)
    contador = cantidad_incial_jugadores

    pregunta_jugadores = fuente_subtitulo.render("Cuantos jugadores son?", True, COLOR_BLANCO)

    flecha_arriba = pygame.image.load("APD/archivos/flecha_arriba.svg")
    flecha_arriba = pygame.transform.scale(flecha_arriba, (200,200))
    flecha_rect = flecha_arriba.get_rect(topleft=(460, 225))  # Posición en pantalla

    flecha_abajo = pygame.image.load("APD/archivos/flecha_abajo.svg")
    flecha_abajo = pygame.transform.scale(flecha_abajo, (200,200))
    flecha_rect2 = flecha_abajo.get_rect(topleft=(125, 225))  # Posición en pantalla

    fuente_jugar = pygame.font.Font("APD/archivos/Golden Age Shad.ttf", 40)
    texto_jugar = fuente_jugar.render("Jugar", True, COLOR_FONDO)

    # VENTANA
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Sala de Escape de Programación")

    # BUCLE DEL JUEGO
    flag_juego = True
    while flag_juego:
        lista_eventos = pygame.event.get()


        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_juego = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    ingreso_nombre = ingreso_nombre[0:-1]
                else:
                    ingreso_nombre += evento.unicode

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if flecha_rect.collidepoint(evento.pos) and contador < 10:
                    contador += 1
                if flecha_rect2.collidepoint(evento.pos) and contador > 1:
                    contador -=1
                if evento.button == 1:
                    if marco_jugar.collidepoint(evento.pos):
                        cantidad_incial_jugadores = contador
                        flag_juego = False



        pantalla.fill(COLOR_FONDO)

        # MUESTRO EL MARCO DEL INICIO CON SU TEXTO
        marco_bienvenido = pygame.draw.rect(pantalla, COLOR_BLANCO, pygame.Rect(70, 45, 690, 150), 10, 20, 20, 20, 20)
        pantalla.blit(bienvenido, (250, 75))
        pantalla.blit(subtitulo_juego, (105, 135))

        # MUESTRO LAS FLECHAS
        pantalla.blit(flecha_arriba,(450, 360))
        pantalla.blit(flecha_abajo, (270, 360))

        # PREGUNTA CANTIDAD DE JUGADORES
        pantalla.blit(pregunta_jugadores, (170, 300))

        # MUESTRO EL CONTADOR DE JUGADORES
        cantidad_inicial = fuente_contador.render(f"{contador}", True, COLOR_BLANCO)
        if contador < 10:
            pantalla.blit(cantidad_inicial, (375, 375))
        else:
            pantalla.blit(cantidad_inicial, (360, 375))

        # BOTON DE JUGAR
        marco_jugar = pygame.draw.rect(pantalla, COLOR_BLANCO, pygame.Rect(290, 470, 215, 70))
        pantalla.blit(texto_jugar, (315, 490))

        pygame.display.flip()
    pygame.quit()
    return cantidad_incial_jugadores