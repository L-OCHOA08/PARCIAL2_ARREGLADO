import pygame

def ingreso_individual(color_fondo, i):
    pygame.init()
    ANCHO_VENTANA = 800
    ALTO_VENTANA = 800
    COLOR_BLANCO = (255, 255, 255)
    pos_nombre = 380
    # VENTANA
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Sala de Escape de Programación")
    # INGRESO DEL NOMBRE
    ingreso_rect = pygame.Rect(100, 200, 150, 40)
    ingreso_font = pygame.font.Font("archivos/Golden Age Shad.ttf", 30)
    ingreso_font_titulo = pygame.font.Font("archivos/Golden Age.ttf", 40)
    ingreso = ""
    # BOTON DE JUGAR
    jugar_rect = pygame.Rect(275, 300, 250, 80)
    jugar_font = pygame.font.Font("archivos/Golden Age Shad.ttf", 40)
    flag_juego = True
    while flag_juego:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag_juego = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    escribiendo = False
                elif evento.key == pygame.K_BACKSPACE:
                    ingreso = ingreso[:-1]
                    pos_nombre += 10
                else:
                    ingreso += evento.unicode
                    pos_nombre -= 10
            if evento.type == pygame.MOUSEBUTTONDOWN and len(ingreso) > 0:
                if jugar_rect.collidepoint(evento.pos):
                    return ingreso
                

        pantalla.fill(color_fondo)
        texto = ingreso_font_titulo.render(f"Ingrese su nombre jugador {i+1}:", True, COLOR_BLANCO)
        input_nombre = ingreso_font.render(f"{ingreso}", True, COLOR_BLANCO)
        pantalla.blit(texto, (125, 150))
        pantalla.blit(input_nombre, (pos_nombre, 195))
        if len(ingreso) > 0:
            boton_jugar = pygame.draw.rect(pantalla, COLOR_BLANCO, jugar_rect)
            jugar_texto = jugar_font.render("Jugar", True, color_fondo)
            pantalla.blit(jugar_texto, (320, 325))
        pygame.display.flip()

    pygame.quit()