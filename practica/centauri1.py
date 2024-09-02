import serial
import time
import pygame
import sys

arduino_port = '/dev/ttyACM0'  # Ajusta el puerto serie según tu configuración
baud_rate = 9600

ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Espera a que se establezca la conexión serial

command = "0.0,0.0,0.0,0.0,0.0,0.0,0.0,0,\n"
print(command)
print(ser.write(command.encode()))
ser.write(command.encode()) 

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Combined")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuentes
font = pygame.font.Font(None, 36)
background = pygame.image.load("robot-2937861_1280.jpg").convert()

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
slider_active = [False] *6

y_spacing = 50
for i in range(6):
    slider = pygame.Rect(50, 250 + i * y_spacing, 360, 10)
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
                elif input_boxX.collidepoint(event.pos):
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
                        
        elif event.type == pygame.MOUSEBUTTONUP:
            for i in range(6):
                slider_active[i] = False
    
        #elif event.type == pygame.MOUSEMOTION:
        #    for i, slider in enumerate(sliders):
        #        if slider_active[i]:
        #            slider_values[i] = min(max(0, event.pos[0] - slider.x), slider.width)
        elif event.type == pygame.MOUSEMOTION:
            for i, slider in enumerate(sliders):
                if slider_active[i]:
                    # Calcula la posición relativa dentro del control deslizante entre -90 y 90.
                    relative_position = (event.pos[0] - slider.x) / slider.width
                    # Convierte la posición relativa a un valor entre -90 y 90.
                    slider_values[i] = -90 + 180 * relative_position
                    # Asegúrate de que el valor esté dentro del rango permitido.
                    slider_values[i] = min(90, max(-90, slider_values[i]))



                    
        elif event.type == pygame.KEYDOWN:
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
            print(slider_values)
            values = [0,0,0,0,0,0]
            #values = slider_values
            values[0]=slider_values[0]*45
            values[1]=slider_values[1]*170
            values[2]=slider_values[2]*90
            values[3]=slider_values[3]*8.889
            values[4]=slider_values[4]*-40
            values[5]=slider_values[5]*8.334
            command = str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) + "," + str(values[4]) + "," + str(values[5]) + "," + "0.0,0,\n"
            print(command)
            print(ser.write(command.encode()))
            ser.write(command.encode())
            #values = [0,0,0,0,0,0]
            
            
                        
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
    
    ## Dibuja los sliders
    #for i, slider in enumerate(sliders):
    #    pygame.draw.rect(screen, slider_colors[i], slider)
    #    pygame.draw.circle(screen, slider_colors[i], (slider.x + slider_values[i], slider.y + 5), 10)
    #    text = font.render(str(round((slider_values[i] / slider.width) * 360)) + "°", True, BLACK)
    #    screen.blit(text, (slider.x + slider_values[i], slider.y - 30))
    for i, slider in enumerate(sliders):
        
        pygame.draw.rect(screen, slider_colors[i], slider)

        # Calcula la posición en el control deslizante centrado entre -90 y 90.
        slider_centered_position = (slider_values[i] + 90) / 180 * slider.width

        # Dibuja el control deslizante centrado.
        pygame.draw.circle(screen, slider_colors[i], (slider.x + int(slider_centered_position), slider.y + 5), 10)

        # Convierte el valor del control deslizante centrado a grados.
        degrees = round((slider_values[i] / 180) * 180)
        text = font.render(str(degrees) + "°", True, BLACK)

        # Alinea el texto al centro del control deslizante.
        text_rect = text.get_rect(center=(slider.x + int(slider_centered_position), slider.y - 30))

        screen.blit(text, text_rect)


    pygame.display.flip()

# Finalizar Pygame
pygame.quit()
sys.exit()
