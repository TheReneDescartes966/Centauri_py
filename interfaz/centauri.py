import pygame
import sys
import serial
import time

# Inicializar Pygame

#arduino_port = '/dev/ttyACM0'  # Ajusta el puerto serie según tu configuración
#baud_rate = 9600

#ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Espera a que se establezca la conexión serial

command = "0.0,0.0,0.0,0.0,0.0,0.0,0.0,0,\n"
print(command)
#print(ser.write(command.encode()))
#ser.write(command.encode()) 

pygame.init()

# Configuración de la ventana
width, height = 545, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Combined")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuentes
font = pygame.font.Font(None, 36)
background = pygame.image.load("Captura de pantalla 2023-11-02 224412.png").convert()



# Botón
button = pygame.Rect(130, 500, 90, 50)
button_color = pygame.Color('forestgreen')

# Boton reset
button2 = pygame.Rect(250, 500, 90, 50)
button2_color = pygame.Color('red')

#boton gripper
button3 = pygame.Rect(185, 430, 100, 50)
button3_color = pygame.Color('red')

# Sliders
sliders = []
slider_colors = [
    pygame.Color('lightskyblue3'),
    pygame.Color('dodgerblue2'),
    pygame.Color('mediumseagreen'),
    pygame.Color('orchid'),
    pygame.Color('Lime'),
    pygame.Color('tomato')
]
gripper = 0
slider_values = [0] * 6
slider_active = [False] *6

y_spacing = 60
for i in range(6):
    slider = pygame.Rect(50, 100 + i * y_spacing, 360, 10)
    sliders.append(slider)


# Bucle principal
running = True
button3_pressed = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if button.collidepoint(mouse_pos):
                # Aquí puedes manejar la entrada de datos, por ejemplo, guardarla en una variable
                print(slider_values)
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
                #print(ser.write(command.encode()))
                #ser.write(command.encode())
            elif button2.collidepoint(mouse_pos):
                slider_values[0] = 0
                slider_values[1] = 0
                slider_values[2] = 0
                slider_values[3] = 0
                slider_values[4] = 0
                slider_values[5] = 0
                print("todos a cero")
                pygame.draw.circle(screen, slider_colors[i], (slider.x + int(slider_centered_position), slider.y + 5), 10)
                print(slider_values)
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
                #print(ser.write(command.encode()))
                #ser.write(command.encode())
            elif button3.collidepoint(event.pos):
                if button3_pressed:
                    print("0")
                    button3_pressed = False
                else:
                    print("1")
                    button3_pressed = True
                
            for i, slider in enumerate(sliders):

                if slider.collidepoint(event.pos):
                    slider_active[i] = True

                                        
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
           
                
                        
    screen.blit(background, [0, 0])


    # Dibuja el botón
    pygame.draw.rect(screen, button_color, button)
    button_text = font.render("Enviar", True, WHITE)
    screen.blit(button_text, (135, 513))

    pygame.draw.rect(screen, button2_color, button2)
    button2_text = font.render("Reset", True, WHITE)
    screen.blit(button2_text, (260, 513))
    
    
    pygame.draw.rect(screen, button3_color, button3)
    button3_text = font.render("Gripper", True, WHITE)
    screen.blit(button3_text, (191, 440))
    
    ## Dibuja los sliders5
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
