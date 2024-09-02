import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sliders")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuentes
font = pygame.font.Font(None, 36)

# Sliders
sliders = []
slider_colors = [
    pygame.Color('lightskyblue3'),
    pygame.Color('dodgerblue2'),
    pygame.Color('mediumseagreen'),
    pygame.Color('orchid'),
    pygame.Color('gold'),
    pygame.Color('tomato')
]

slider_values = [0] * 6
slider_active = [False] * 6

y_spacing = 50
for i in range(6):
    slider = pygame.Rect(50, 100 + i * y_spacing, 400, 10)
    sliders.append(slider)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, slider in enumerate(sliders):
                if slider.collidepoint(event.pos):
                    slider_active[i] = True
        elif event.type == pygame.MOUSEBUTTONUP:
            for i in range(6):
                slider_active[i] = False
        elif event.type == pygame.MOUSEMOTION:
            for i, slider in enumerate(sliders):
                if slider_active[i]:
                    slider_values[i] = min(max(0, event.pos[0] - slider.x), slider.width)

    angles = [round((slider_value / slider.width) * 360) for slider_value in slider_values]

    screen.fill(WHITE)

    # Dibuja los sliders
    for i, slider in enumerate(sliders):
        pygame.draw.rect(screen, slider_colors[i], slider)
        pygame.draw.circle(screen, slider_colors[i], (slider.x + slider_values[i], slider.y + 5), 10)
        text = font.render(str(angles[i]) + "°", True, BLACK)
        screen.blit(text, (slider.x + slider_values[i], slider.y - 30))

    pygame.display.flip()

# Finalizar Pygame
pygame.quit()
sys.exit()
