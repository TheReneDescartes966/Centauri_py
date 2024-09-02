import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cabina de Entrada de Datos")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
background = pygame.image.load("robot-2937861_1280.jpg").convert()

# Fuentes
font = pygame.font.Font(None, 36)

# Entradas de texto
input_boxX = pygame.Rect(50, 100, 90, 50) 
input_boxY = pygame.Rect(170, 100, 90, 50) 
input_boxZ = pygame.Rect(290, 100, 90, 50) 

textX = ""
textY = ""
textZ = ""
color_active = pygame.Color('lightskyblue3')
color_inactive = pygame.Color('dodgerblue2')
colorX = color_inactive
colorY = color_inactive
colorZ = color_inactive

# Botón
button = pygame.Rect(400, 100, 90, 50)
button_color = pygame.Color('forestgreen')

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_boxX.collidepoint(event.pos):
                colorX = color_active
                colorY = color_inactive
                colorZ = color_inactive

            elif input_boxY.collidepoint(event.pos):
                colorX = color_inactive
                colorY = color_active
                colorZ = color_inactive

            elif input_boxZ.collidepoint(event.pos):
                colorX = color_inactive
                colorY = color_inactive
                colorZ = color_active

            else:
                colorX = color_inactive
                colorY = color_inactive
                colorZ = color_inactive

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Aquí puedes manejar la entrada de datos, por ejemplo, guardarla en una variable
                print(textX)
                print(textY)
                print(textZ)
                textX = ""
                textY = ""
                textZ = ""

            elif event.key == pygame.K_BACKSPACE:
                if colorX == color_active:
                    textX = textX[:-1]
                elif colorY == color_active:
                    textY = textY[:-1]
                elif colorZ == color_active:
                    textZ = textZ[:-1]

            else:
                if colorX == color_active:
                    textX += event.unicode
                elif colorY == color_active:
                    textY += event.unicode
                elif colorZ == color_active:
                    textZ += event.unicode

    screen.blit(background, [-400, -200])

    # Dibuja la caja de entrada X
    pygame.draw.rect(screen, colorX, input_boxX, 2)
    txt_surface = font.render(textX, True, colorX)
    width = max(90, txt_surface.get_width()+10)
    input_boxX.w = width
    screen.blit(txt_surface, (input_boxX.x+5, input_boxX.y+5))

    # Dibuja la caja de entrada Y
    pygame.draw.rect(screen, colorY, input_boxY, 2)
    txt_surface = font.render(textY, True, colorY)
    width = max(90, txt_surface.get_width()+10)
    input_boxY.w = width
    screen.blit(txt_surface, (input_boxY.x+5, input_boxY.y+5))

    # Dibuja la caja de entrada Z
    pygame.draw.rect(screen, colorZ, input_boxZ, 2)
    txt_surface = font.render(textZ, True, colorZ)
    width = max(90, txt_surface.get_width()+10)
    input_boxZ.w = width
    screen.blit(txt_surface, (input_boxZ.x+5, input_boxZ.y+5))

    # Dibuja el botón
    pygame.draw.rect(screen, button_color, button)
    button_text = font.render("Enviar", True, WHITE)
    screen.blit(button_text, (405, 110))

    iconx = font.render("X", True, BLACK)
    screen.blit(iconx, (85, 160))

    icony = font.render("Y", True, BLACK)
    screen.blit(icony, (205, 160))

    iconz = font.render("Z", True, BLACK)
    screen.blit(iconz, (325, 160))
    pygame.display.flip()

# Finalizar Pygame
pygame.quit()
sys.exit()