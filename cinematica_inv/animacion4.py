import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from denavit import denavit
from drawrobot3d4 import drawrobot3d4
import time
def animacion4(mat_q,mat_q1,mat_q2,mat_q3,mat_q4,mat_q5,mat_q6,mat_q7,mat_q8,mat_q9,mat_q10,mat_q11,mat_q12,mat_q13,teta,d,a,alfa):
    # Parámetros Denavit-Hartenberg del robot
    
    # Vector de posicion (x, y, z) del sistema de coordenadas de referencia
    x0, y0, z0 = 0, 0, 0
    # Se dibuja el sistema de coordenadas de referencia
    

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    p, = ax.plot([x0], [y0], [z0], 'r', linewidth=2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # Se asigna una rejilla a los ejes
    ax.grid(True)
    # Se establecen los límites de los ejes
    ax.set_xlim3d([-1, 1])
    ax.set_ylim3d([-1, 1])
    ax.set_zlim3d([0, 1.5])
    # Mantiene el gráfico actual
    plt.ion()
    plt.show()
    # Número de columnas de la matriz
    n = mat_q.shape[1]
    # Se dibuja la disposición del robot correspondiente a cada columna
    for i in range(n):
        # Variables articulares del brazo robot
        teta[0] = mat_q[0,i]
        teta[1] = mat_q[1,i]+np.pi/2
        teta[2] = mat_q[2,i]+np.pi/2
        teta[3] = mat_q[3,i]
        teta[4] = mat_q[4,i]
        teta[5] = mat_q[5,i]
        d[0]= 0.17
        d[3]= 0.22
        d[5]= 0.1052
        a[1]= 0.22
        alfa[0] = np.pi/2
        alfa[2] = np.pi/2
        alfa[3] = -np.pi/2
        alfa[4] = np.pi/2
        #drawrobot3d4(teta, d, a, alfa)
        #input()
        # Matrices de transformación del primer sistema al correspondiente
        A01 = denavit(teta[0], d[0], a[0], alfa[0])
        A12 = denavit(teta[1], d[1], a[1], alfa[1])
        A23 = denavit(teta[2], d[2], a[2], alfa[2])
        A34 = denavit(teta[3], d[3], a[3], alfa[3])
        A45 = denavit(teta[4], d[4], a[4], alfa[4])
        A56 = denavit(teta[5], d[5], a[5], alfa[5])
        # Matrices de transformación del primer sistema al correspondiente
        A02 = np.dot(A01, A12)
        A03 = np.dot(A02, A23)
        A04 = np.dot(A03, A34)
        A05 = np.dot(A04, A45)
        A06 = np.dot(A05, A56)
        # Vector de posicion (x, y, z) de cada sistema de coordenadas
        x0, y0, z0 = 0, 0, 0
        x1, y1, z1 = A01[0, 3], A01[1, 3], A01[2, 3]
        x2, y2, z2 = A02[0, 3], A02[1, 3], A02[2, 3]
        x3, y3, z3 = A03[0, 3], A03[1, 3], A03[2, 3]
        x4, y4, z4 = A04[0, 3], A04[1, 3], A04[2, 3]
        x5, y5, z5 = A05[0, 3], A05[1, 3], A05[2, 3]
        x6, y6, z6 = A06[0, 3], A06[1, 3], A06[2, 3]
        # Se dibuja el robot
        x = [x0, x1, x2, x3, x4, x5, x6]
        y = [y0, y1, y2, y3, y4, y5, y6]
        z = [z0, z1, z2, z3, z4, z5, z6]
        print("T06: ")
        print(A06)

        print("X: ",x6,"Y: ",y6,"Z: ", z6)

        plt.plot(x6,y6,z6 ,marker=".", color="black")

        

    
        ax.grid(True)
    # Se establecen los límites de los ejes
   
        p.set_data(x, y)
        p.set_3d_properties(z)
      #  ax.scatter(x, y, z)
        # Se fuerza a Python a actualizar la pantalla
        plt.pause(0.1)

    for i in range(n):
        # Variables articulares del brazo robot
        teta[0] = mat_q1[0,i]
        teta[1] = mat_q1[1,i]+np.pi/2
        teta[2] = mat_q1[2,i]+np.pi/2
        teta[3] = mat_q1[3,i]
        teta[4] = mat_q1[4,i]
        teta[5] = mat_q1[5,i]
        d[0]= 0.17
        d[3]= 0.22
        d[5]= 0.1052
        a[1]= 0.22
        alfa[0] = np.pi/2
        alfa[2] = np.pi/2
        alfa[3] = -np.pi/2
        alfa[4] = np.pi/2




        #drawrobot3d4(teta, d, a, alfa)
        #input()
        # Matrices de transformación del primer sistema al correspondiente
        A01 = denavit(teta[0], d[0], a[0], alfa[0])
        A12 = denavit(teta[1], d[1], a[1], alfa[1])
        A23 = denavit(teta[2], d[2], a[2], alfa[2])
        A34 = denavit(teta[3], d[3], a[3], alfa[3])
        A45 = denavit(teta[4], d[4], a[4], alfa[4])
        A56 = denavit(teta[5], d[5], a[5], alfa[5])
        # Matrices de transformación del primer sistema al correspondiente
        A02 = np.dot(A01, A12)
        A03 = np.dot(A02, A23)
        A04 = np.dot(A03, A34)
        A05 = np.dot(A04, A45)
        A06 = np.dot(A05, A56)
        # Vector de posicion (x, y, z) de cada sistema de coordenadas
        x0, y0, z0 = 0, 0, 0
        x1, y1, z1 = A01[0, 3], A01[1, 3], A01[2, 3]
        x2, y2, z2 = A02[0, 3], A02[1, 3], A02[2, 3]
        x3, y3, z3 = A03[0, 3], A03[1, 3], A03[2, 3]
        x4, y4, z4 = A04[0, 3], A04[1, 3], A04[2, 3]
        x5, y5, z5 = A05[0, 3], A05[1, 3], A05[2, 3]
        x6, y6, z6 = A06[0, 3], A06[1, 3], A06[2, 3]
        # Se dibuja el robot
        x = [x0, x1, x2, x3, x4, x5, x6]
        y = [y0, y1, y2, y3, y4, y5, y6]
        z = [z0, z1, z2, z3, z4, z5, z6]
        print("T06: ")
        print(A06)

        print("X: ",x6,"Y: ",y6,"Z: ", z6)

        plt.plot(x6,y6,z6 ,marker=".", color="black")

    
        ax.grid(True)
    # Se establecen los límites de los ejes
   
        p.set_data(x, y)
        p.set_3d_properties(z)
      #  ax.scatter(x, y, z)
        # Se fuerza a Python a actualizar la pantalla
        plt.pause(0.1)

    for i in range(n):
        # Variables articulares del brazo robot
        teta[0] = mat_q2[0,i]
        teta[1] = mat_q2[1,i]+np.pi/2
        teta[2] = mat_q2[2,i]+np.pi/2
        teta[3] = mat_q2[3,i]
        teta[4] = mat_q2[4,i]
        teta[5] = mat_q2[5,i]
        d[0]= 0.17
        d[3]= 0.22
        d[5]= 0.1052
        a[1]= 0.22
        alfa[0] = np.pi/2
        alfa[2] = np.pi/2
        alfa[3] = -np.pi/2
        alfa[4] = np.pi/2




        #drawrobot3d4(teta, d, a, alfa)
        #input()
        # Matrices de transformación del primer sistema al correspondiente
        A01 = denavit(teta[0], d[0], a[0], alfa[0])
        A12 = denavit(teta[1], d[1], a[1], alfa[1])
        A23 = denavit(teta[2], d[2], a[2], alfa[2])
        A34 = denavit(teta[3], d[3], a[3], alfa[3])
        A45 = denavit(teta[4], d[4], a[4], alfa[4])
        A56 = denavit(teta[5], d[5], a[5], alfa[5])
        # Matrices de transformación del primer sistema al correspondiente
        A02 = np.dot(A01, A12)
        A03 = np.dot(A02, A23)
        A04 = np.dot(A03, A34)
        A05 = np.dot(A04, A45)
        A06 = np.dot(A05, A56)
        # Vector de posicion (x, y, z) de cada sistema de coordenadas
        x0, y0, z0 = 0, 0, 0
        x1, y1, z1 = A01[0, 3], A01[1, 3], A01[2, 3]
        x2, y2, z2 = A02[0, 3], A02[1, 3], A02[2, 3]
        x3, y3, z3 = A03[0, 3], A03[1, 3], A03[2, 3]
        x4, y4, z4 = A04[0, 3], A04[1, 3], A04[2, 3]
        x5, y5, z5 = A05[0, 3], A05[1, 3], A05[2, 3]
        x6, y6, z6 = A06[0, 3], A06[1, 3], A06[2, 3]
        # Se dibuja el robot
        x = [x0, x1, x2, x3, x4, x5, x6]
        y = [y0, y1, y2, y3, y4, y5, y6]
        z = [z0, z1, z2, z3, z4, z5, z6]
        print("T06: ")
        print(A06)

        print("X: ",x6,"Y: ",y6,"Z: ", z6)

        plt.plot(x6,y6,z6 ,marker=".", color="black")

    
        ax.grid(True)
    # Se establecen los límites de los ejes
   
        p.set_data(x, y)
        p.set_3d_properties(z)
      #  ax.scatter(x, y, z)
        # Se fuerza a Python a actualizar la pantalla
        plt.pause(0.1)

    for i in range(n):
        # Variables articulares del brazo robot
        teta[0] = mat_q3[0,i]
        teta[1] = mat_q3[1,i]+np.pi/2
        teta[2] = mat_q3[2,i]+np.pi/2
        teta[3] = mat_q3[3,i]
        teta[4] = mat_q3[4,i]
        teta[5] = mat_q3[5,i]
        d[0]= 0.17
        d[3]= 0.22
        d[5]= 0.1052
        a[1]= 0.22
        alfa[0] = np.pi/2
        alfa[2] = np.pi/2
        alfa[3] = -np.pi/2
        alfa[4] = np.pi/2




        #drawrobot3d4(teta, d, a, alfa)
        #input()
        # Matrices de transformación del primer sistema al correspondiente
        A01 = denavit(teta[0], d[0], a[0], alfa[0])
        A12 = denavit(teta[1], d[1], a[1], alfa[1])
        A23 = denavit(teta[2], d[2], a[2], alfa[2])
        A34 = denavit(teta[3], d[3], a[3], alfa[3])
        A45 = denavit(teta[4], d[4], a[4], alfa[4])
        A56 = denavit(teta[5], d[5], a[5], alfa[5])
        # Matrices de transformación del primer sistema al correspondiente
        A02 = np.dot(A01, A12)
        A03 = np.dot(A02, A23)
        A04 = np.dot(A03, A34)
        A05 = np.dot(A04, A45)
        A06 = np.dot(A05, A56)
        # Vector de posicion (x, y, z) de cada sistema de coordenadas
        x0, y0, z0 = 0, 0, 0
        x1, y1, z1 = A01[0, 3], A01[1, 3], A01[2, 3]
        x2, y2, z2 = A02[0, 3], A02[1, 3], A02[2, 3]
        x3, y3, z3 = A03[0, 3], A03[1, 3], A03[2, 3]
        x4, y4, z4 = A04[0, 3], A04[1, 3], A04[2, 3]
        x5, y5, z5 = A05[0, 3], A05[1, 3], A05[2, 3]
        x6, y6, z6 = A06[0, 3], A06[1, 3], A06[2, 3]
        # Se dibuja el robot
        x = [x0, x1, x2, x3, x4, x5, x6]
        y = [y0, y1, y2, y3, y4, y5, y6]
        z = [z0, z1, z2, z3, z4, z5, z6]
        print("T06: ")
        print(A06)

        print("X: ",x6,"Y: ",y6,"Z: ", z6)
  

    
        ax.grid(True)
    # Se establecen los límites de los ejes
   
        p.set_data(x, y)
        p.set_3d_properties(z)
      #  ax.scatter(x, y, z)
        # Se fuerza a Python a actualizar la pantalla
        plt.pause(0.1)

    for i in range(n):
        # Variables articulares del brazo robot
        teta[0] = mat_q4[0,i]
        teta[1] = mat_q4[1,i]+np.pi/2
        teta[2] = mat_q4[2,i]+np.pi/2
        teta[3] = mat_q4[3,i]
        teta[4] = mat_q4[4,i]
        teta[5] = mat_q4[5,i]
        d[0]= 0.17
        d[3]= 0.22
        d[5]= 0.1052
        a[1]= 0.22
        alfa[0] = np.pi/2
        alfa[2] = np.pi/2
        alfa[3] = -np.pi/2
        alfa[4] = np.pi/2




        #drawrobot3d4(teta, d, a, alfa)
        #input()
        # Matrices de transformación del primer sistema al correspondiente
        A01 = denavit(teta[0], d[0], a[0], alfa[0])
        A12 = denavit(teta[1], d[1], a[1], alfa[1])
        A23 = denavit(teta[2], d[2], a[2], alfa[2])
        A34 = denavit(teta[3], d[3], a[3], alfa[3])
        A45 = denavit(teta[4], d[4], a[4], alfa[4])
        A56 = denavit(teta[5], d[5], a[5], alfa[5])
        # Matrices de transformación del primer sistema al correspondiente
        A02 = np.dot(A01, A12)
        A03 = np.dot(A02, A23)
        A04 = np.dot(A03, A34)
        A05 = np.dot(A04, A45)
        A06 = np.dot(A05, A56)
        # Vector de posicion (x, y, z) de cada sistema de coordenadas
        x0, y0, z0 = 0, 0, 0
        x1, y1, z1 = A01[0, 3], A01[1, 3], A01[2, 3]
        x2, y2, z2 = A02[0, 3], A02[1, 3], A02[2, 3]
        x3, y3, z3 = A03[0, 3], A03[1, 3], A03[2, 3]
        x4, y4, z4 = A04[0, 3], A04[1, 3], A04[2, 3]
        x5, y5, z5 = A05[0, 3], A05[1, 3], A05[2, 3]
        x6, y6, z6 = A06[0, 3], A06[1, 3], A06[2, 3]
        # Se dibuja el robot
        x = [x0, x1, x2, x3, x4, x5, x6]
        y = [y0, y1, y2, y3, y4, y5, y6]
        z = [z0, z1, z2, z3, z4, z5, z6]
        print("T06: ")
        print(A06)

        print("X: ",x6,"Y: ",y6,"Z: ", z6)

        plt.plot(x6,y6,z6 ,marker=".", color="black")

        

    
        ax.grid(True)
    # Se establecen los límites de los ejes
   
        p.set_data(x, y)
        p.set_3d_properties(z)
      #  ax.scatter(x, y, z)
        # Se fuerza a Python a actualizar la pantalla
        plt.pause(0.1)
    5    
    for i in range(n):
        # Variables articulares del brazo robot
        teta[0] = mat_q5[0,i]
        teta[1] = mat_q5[1,i]+np.pi/2
        teta[2] = mat_q5[2,i]+np.pi/2
        teta[3] = mat_q5[3,i]
        teta[4] = mat_q5[4,i]
        teta[5] = mat_q5[5,i]
        d[0]= 0.17
        d[3]= 0.22
        d[5]= 0.1052
        a[1]= 0.22
        alfa[0] = np.pi/2
        alfa[2] = np.pi/2
        alfa[3] = -np.pi/2
        alfa[4] = np.pi/2




        #drawrobot3d4(teta, d, a, alfa)
        #input()
        # Matrices de transformación del primer sistema al correspondiente
        A01 = denavit(teta[0], d[0], a[0], alfa[0])
        A12 = denavit(teta[1], d[1], a[1], alfa[1])
        A23 = denavit(teta[2], d[2], a[2], alfa[2])
        A34 = denavit(teta[3], d[3], a[3], alfa[3])
        A45 = denavit(teta[4], d[4], a[4], alfa[4])
        A56 = denavit(teta[5], d[5], a[5], alfa[5])
        # Matrices de transformación del primer sistema al correspondiente
        A02 = np.dot(A01, A12)
        A03 = np.dot(A02, A23)
        A04 = np.dot(A03, A34)
        A05 = np.dot(A04, A45)
        A06 = np.dot(A05, A56)
        # Vector de posicion (x, y, z) de cada sistema de coordenadas
        x0, y0, z0 = 0, 0, 0
        x1, y1, z1 = A01[0, 3], A01[1, 3], A01[2, 3]
        x2, y2, z2 = A02[0, 3], A02[1, 3], A02[2, 3]
        x3, y3, z3 = A03[0, 3], A03[1, 3], A03[2, 3]
        x4, y4, z4 = A04[0, 3], A04[1, 3], A04[2, 3]
        x5, y5, z5 = A05[0, 3], A05[1, 3], A05[2, 3]
        x6, y6, z6 = A06[0, 3], A06[1, 3], A06[2, 3]
        # Se dibuja el robot
        x = [x0, x1, x2, x3, x4, x5, x6]
        y = [y0, y1, y2, y3, y4, y5, y6]
        z = [z0, z1, z2, z3, z4, z5, z6]
        print("T06: ")
        print(A06)

        print("X: ",x6,"Y: ",y6,"Z: ", z6)

        plt.plot(x6,y6,z6 ,marker=".", color="black")

        

    
        ax.grid(True)
    # Se establecen los límites de los ejes
   
        p.set_data(x, y)
        p.set_3d_properties(z)
      #  ax.scatter(x, y, z)
        # Se fuerza a Python a actualizar la pantalla
        plt.pause(0.1)

    for i in range(n):
        # Variables articulares del brazo robot
        teta[0] = mat_q6[0,i]
        teta[1] = mat_q6[1,i]+np.pi/2
        teta[2] = mat_q6[2,i]+np.pi/2
        teta[3] = mat_q6[3,i]
        teta[4] = mat_q6[4,i]
        teta[5] = mat_q6[5,i]
        d[0]= 0.17
        d[3]= 0.22
        d[5]= 0.1052
        a[1]= 0.22
        alfa[0] = np.pi/2
        alfa[2] = np.pi/2
        alfa[3] = -np.pi/2
        alfa[4] = np.pi/2




        #drawrobot3d4(teta, d, a, alfa)
        #input()
        # Matrices de transformación del primer sistema al correspondiente
        A01 = denavit(teta[0], d[0], a[0], alfa[0])
        A12 = denavit(teta[1], d[1], a[1], alfa[1])
        A23 = denavit(teta[2], d[2], a[2], alfa[2])
        A34 = denavit(teta[3], d[3], a[3], alfa[3])
        A45 = denavit(teta[4], d[4], a[4], alfa[4])
        A56 = denavit(teta[5], d[5], a[5], alfa[5])
        # Matrices de transformación del primer sistema al correspondiente
        A02 = np.dot(A01, A12)
        A03 = np.dot(A02, A23)
        A04 = np.dot(A03, A34)
        A05 = np.dot(A04, A45)
        A06 = np.dot(A05, A56)
        # Vector de posicion (x, y, z) de cada sistema de coordenadas
        x0, y0, z0 = 0, 0, 0
        x1, y1, z1 = A01[0, 3], A01[1, 3], A01[2, 3]
        x2, y2, z2 = A02[0, 3], A02[1, 3], A02[2, 3]
        x3, y3, z3 = A03[0, 3], A03[1, 3], A03[2, 3]
        x4, y4, z4 = A04[0, 3], A04[1, 3], A04[2, 3]
        x5, y5, z5 = A05[0, 3], A05[1, 3], A05[2, 3]
        x6, y6, z6 = A06[0, 3], A06[1, 3], A06[2, 3]
        # Se dibuja el robot
        x = [x0, x1, x2, x3, x4, x5, x6]
        y = [y0, y1, y2, y3, y4, y5, y6]
        z = [z0, z1, z2, z3, z4, z5, z6]
        print("T06: ")
        print(A06)

        print("X: ",x6,"Y: ",y6,"Z: ", z6)

        plt.plot(x6,y6,z6 ,marker=".", color="black")

        ax.grid(True)
    # Se establecen los límites de los ejes
   
        p.set_data(x, y)
        p.set_3d_properties(z)
      #  ax.scatter(x, y, z)
        # Se fuerza a Python a actualizar la pantalla
        plt.pause(0.1)

    for i in range(n):
        # Variables articulares del brazo robot
        teta[0] = mat_q7[0,i]
        teta[1] = mat_q7[1,i]+np.pi/2
        teta[2] = mat_q7[2,i]+np.pi/2
        teta[3] = mat_q7[3,i]
        teta[4] = mat_q7[4,i]
        teta[5] = mat_q7[5,i]
        d[0]= 0.17
        d[3]= 0.22
        d[5]= 0.1052
        a[1]= 0.22
        alfa[0] = np.pi/2
        alfa[2] = np.pi/2
        alfa[3] = -np.pi/2
        alfa[4] = np.pi/2




        #drawrobot3d4(teta, d, a, alfa)
        #input()
        # Matrices de transformación del primer sistema al correspondiente
        A01 = denavit(teta[0], d[0], a[0], alfa[0])
        A12 = denavit(teta[1], d[1], a[1], alfa[1])
        A23 = denavit(teta[2], d[2], a[2], alfa[2])
        A34 = denavit(teta[3], d[3], a[3], alfa[3])
        A45 = denavit(teta[4], d[4], a[4], alfa[4])
        A56 = denavit(teta[5], d[5], a[5], alfa[5])
        # Matrices de transformación del primer sistema al correspondiente
        A02 = np.dot(A01, A12)
        A03 = np.dot(A02, A23)
        A04 = np.dot(A03, A34)
        A05 = np.dot(A04, A45)
        A06 = np.dot(A05, A56)
        # Vector de posicion (x, y, z) de cada sistema de coordenadas
        x0, y0, z0 = 0, 0, 0
        x1, y1, z1 = A01[0, 3], A01[1, 3], A01[2, 3]
        x2, y2, z2 = A02[0, 3], A02[1, 3], A02[2, 3]
        x3, y3, z3 = A03[0, 3], A03[1, 3], A03[2, 3]
        x4, y4, z4 = A04[0, 3], A04[1, 3], A04[2, 3]
        x5, y5, z5 = A05[0, 3], A05[1, 3], A05[2, 3]
        x6, y6, z6 = A06[0, 3], A06[1, 3], A06[2, 3]
        # Se dibuja el robot
        x = [x0, x1, x2, x3, x4, x5, x6]
        y = [y0, y1, y2, y3, y4, y5, y6]
        z = [z0, z1, z2, z3, z4, z5, z6]
        print("T06: ")
        print(A06)

        print("X: ",x6,"Y: ",y6,"Z: ", z6)
        

        ax.grid(True)
    # Se establecen los límites de los ejes
   
        p.set_data(x, y)
        p.set_3d_properties(z)
      #  ax.scatter(x, y, z)
        # Se fuerza a Python a actualizar la pantalla
        plt.pause(0.1)

    for i in range(n):
        # Variables articulares del brazo robot
        teta[0] = mat_q8[0,i]
        teta[1] = mat_q8[1,i]+np.pi/2
        teta[2] = mat_q8[2,i]+np.pi/2
        teta[3] = mat_q8[3,i]
        teta[4] = mat_q8[4,i]
        teta[5] = mat_q8[5,i]
        d[0]= 0.17
        d[3]= 0.22
        d[5]= 0.1052
        a[1]= 0.22
        alfa[0] = np.pi/2
        alfa[2] = np.pi/2
        alfa[3] = -np.pi/2
        alfa[4] = np.pi/2




        #drawrobot3d4(teta, d, a, alfa)
        #input()
        # Matrices de transformación del primer sistema al correspondiente
        A01 = denavit(teta[0], d[0], a[0], alfa[0])
        A12 = denavit(teta[1], d[1], a[1], alfa[1])
        A23 = denavit(teta[2], d[2], a[2], alfa[2])
        A34 = denavit(teta[3], d[3], a[3], alfa[3])
        A45 = denavit(teta[4], d[4], a[4], alfa[4])
        A56 = denavit(teta[5], d[5], a[5], alfa[5])
        # Matrices de transformación del primer sistema al correspondiente
        A02 = np.dot(A01, A12)
        A03 = np.dot(A02, A23)
        A04 = np.dot(A03, A34)
        A05 = np.dot(A04, A45)
        A06 = np.dot(A05, A56)
        # Vector de posicion (x, y, z) de cada sistema de coordenadas
        x0, y0, z0 = 0, 0, 0
        x1, y1, z1 = A01[0, 3], A01[1, 3], A01[2, 3]
        x2, y2, z2 = A02[0, 3], A02[1, 3], A02[2, 3]
        x3, y3, z3 = A03[0, 3], A03[1, 3], A03[2, 3]
        x4, y4, z4 = A04[0, 3], A04[1, 3], A04[2, 3]
        x5, y5, z5 = A05[0, 3], A05[1, 3], A05[2, 3]
        x6, y6, z6 = A06[0, 3], A06[1, 3], A06[2, 3]
        # Se dibuja el robot
        x = [x0, x1, x2, x3, x4, x5, x6]
        y = [y0, y1, y2, y3, y4, y5, y6]
        z = [z0, z1, z2, z3, z4, z5, z6]
        print("T06: ")
        print(A06)

        print("X: ",x6,"Y: ",y6,"Z: ", z6)

        plt.plot(x6,y6,z6 ,marker=".", color="black")

    
        ax.grid(True)
    # Se establecen los límites de los ejes
   
        p.set_data(x, y)
        p.set_3d_properties(z)
      #  ax.scatter(x, y, z)
        # Se fuerza a Python a actualizar la pantalla
        plt.pause(0.1)

    for i in range(n):
        # Variables articulares del brazo robot
        teta[0] = mat_q9[0,i]
        teta[1] = mat_q9[1,i]+np.pi/2
        teta[2] = mat_q9[2,i]+np.pi/2
        teta[3] = mat_q9[3,i]
        teta[4] = mat_q9[4,i]
        teta[5] = mat_q9[5,i]
        d[0]= 0.17
        d[3]= 0.22
        d[5]= 0.1052
        a[1]= 0.22
        alfa[0] = np.pi/2
        alfa[2] = np.pi/2
        alfa[3] = -np.pi/2
        alfa[4] = np.pi/2




        #drawrobot3d4(teta, d, a, alfa)
        #input()
        # Matrices de transformación del primer sistema al correspondiente
        A01 = denavit(teta[0], d[0], a[0], alfa[0])
        A12 = denavit(teta[1], d[1], a[1], alfa[1])
        A23 = denavit(teta[2], d[2], a[2], alfa[2])
        A34 = denavit(teta[3], d[3], a[3], alfa[3])
        A45 = denavit(teta[4], d[4], a[4], alfa[4])
        A56 = denavit(teta[5], d[5], a[5], alfa[5])
        # Matrices de transformación del primer sistema al correspondiente
        A02 = np.dot(A01, A12)
        A03 = np.dot(A02, A23)
        A04 = np.dot(A03, A34)
        A05 = np.dot(A04, A45)
        A06 = np.dot(A05, A56)
        # Vector de posicion (x, y, z) de cada sistema de coordenadas
        x0, y0, z0 = 0, 0, 0
        x1, y1, z1 = A01[0, 3], A01[1, 3], A01[2, 3]
        x2, y2, z2 = A02[0, 3], A02[1, 3], A02[2, 3]
        x3, y3, z3 = A03[0, 3], A03[1, 3], A03[2, 3]
        x4, y4, z4 = A04[0, 3], A04[1, 3], A04[2, 3]
        x5, y5, z5 = A05[0, 3], A05[1, 3], A05[2, 3]
        x6, y6, z6 = A06[0, 3], A06[1, 3], A06[2, 3]
        # Se dibuja el robot
        x = [x0, x1, x2, x3, x4, x5, x6]
        y = [y0, y1, y2, y3, y4, y5, y6]
        z = [z0, z1, z2, z3, z4, z5, z6]
        print("T06: ")
        print(A06)

        print("X: ",x6,"Y: ",y6,"Z: ", z6)

       

        ax.grid(True)
    # Se establecen los límites de los ejes
   
        p.set_data(x, y)
        p.set_3d_properties(z)
      #  ax.scatter(x, y, z)
        # Se fuerza a Python a actualizar la pantalla
        plt.pause(0.1)

    for i in range(n):
        # Variables articulares del brazo robot
        teta[0] = mat_q10[0,i]
        teta[1] = mat_q10[1,i]+np.pi/2
        teta[2] = mat_q10[2,i]+np.pi/2
        teta[3] = mat_q10[3,i]
        teta[4] = mat_q10[4,i]
        teta[5] = mat_q10[5,i]
        d[0]= 0.17
        d[3]= 0.22
        d[5]= 0.1052
        a[1]= 0.22
        alfa[0] = np.pi/2
        alfa[2] = np.pi/2
        alfa[3] = -np.pi/2
        alfa[4] = np.pi/2




        #drawrobot3d4(teta, d, a, alfa)
        #input()
        # Matrices de transformación del primer sistema al correspondiente
        A01 = denavit(teta[0], d[0], a[0], alfa[0])
        A12 = denavit(teta[1], d[1], a[1], alfa[1])
        A23 = denavit(teta[2], d[2], a[2], alfa[2])
        A34 = denavit(teta[3], d[3], a[3], alfa[3])
        A45 = denavit(teta[4], d[4], a[4], alfa[4])
        A56 = denavit(teta[5], d[5], a[5], alfa[5])
        # Matrices de transformación del primer sistema al correspondiente
        A02 = np.dot(A01, A12)
        A03 = np.dot(A02, A23)
        A04 = np.dot(A03, A34)
        A05 = np.dot(A04, A45)
        A06 = np.dot(A05, A56)
        # Vector de posicion (x, y, z) de cada sistema de coordenadas
        x0, y0, z0 = 0, 0, 0
        x1, y1, z1 = A01[0, 3], A01[1, 3], A01[2, 3]
        x2, y2, z2 = A02[0, 3], A02[1, 3], A02[2, 3]
        x3, y3, z3 = A03[0, 3], A03[1, 3], A03[2, 3]
        x4, y4, z4 = A04[0, 3], A04[1, 3], A04[2, 3]
        x5, y5, z5 = A05[0, 3], A05[1, 3], A05[2, 3]
        x6, y6, z6 = A06[0, 3], A06[1, 3], A06[2, 3]
        # Se dibuja el robot
        x = [x0, x1, x2, x3, x4, x5, x6]
        y = [y0, y1, y2, y3, y4, y5, y6]
        z = [z0, z1, z2, z3, z4, z5, z6]
        print("T06: ")
        print(A06)

        print("X: ",x6,"Y: ",y6,"Z: ", z6)

        plt.plot(x6,y6,z6 ,marker=".", color="black")

        ax.grid(True)
    # Se establecen los límites de los ejes
   
        p.set_data(x, y)
        p.set_3d_properties(z)
      #  ax.scatter(x, y, z)
        # Se fuerza a Python a actualizar la pantalla
        plt.pause(0.1)

    for i in range(n):
        # Variables articulares del brazo robot
        teta[0] = mat_q11[0,i]
        teta[1] = mat_q11[1,i]+np.pi/2
        teta[2] = mat_q11[2,i]+np.pi/2
        teta[3] = mat_q11[3,i]
        teta[4] = mat_q11[4,i]
        teta[5] = mat_q11[5,i]
        d[0]= 0.17
        d[3]= 0.22
        d[5]= 0.1052
        a[1]= 0.22
        alfa[0] = np.pi/2
        alfa[2] = np.pi/2
        alfa[3] = -np.pi/2
        alfa[4] = np.pi/2




        #drawrobot3d4(teta, d, a, alfa)
        #input()
        # Matrices de transformación del primer sistema al correspondiente
        A01 = denavit(teta[0], d[0], a[0], alfa[0])
        A12 = denavit(teta[1], d[1], a[1], alfa[1])
        A23 = denavit(teta[2], d[2], a[2], alfa[2])
        A34 = denavit(teta[3], d[3], a[3], alfa[3])
        A45 = denavit(teta[4], d[4], a[4], alfa[4])
        A56 = denavit(teta[5], d[5], a[5], alfa[5])
        # Matrices de transformación del primer sistema al correspondiente
        A02 = np.dot(A01, A12)
        A03 = np.dot(A02, A23)
        A04 = np.dot(A03, A34)
        A05 = np.dot(A04, A45)
        A06 = np.dot(A05, A56)
        # Vector de posicion (x, y, z) de cada sistema de coordenadas
        x0, y0, z0 = 0, 0, 0
        x1, y1, z1 = A01[0, 3], A01[1, 3], A01[2, 3]
        x2, y2, z2 = A02[0, 3], A02[1, 3], A02[2, 3]
        x3, y3, z3 = A03[0, 3], A03[1, 3], A03[2, 3]
        x4, y4, z4 = A04[0, 3], A04[1, 3], A04[2, 3]
        x5, y5, z5 = A05[0, 3], A05[1, 3], A05[2, 3]
        x6, y6, z6 = A06[0, 3], A06[1, 3], A06[2, 3]
        # Se dibuja el robot
        x = [x0, x1, x2, x3, x4, x5, x6]
        y = [y0, y1, y2, y3, y4, y5, y6]
        z = [z0, z1, z2, z3, z4, z5, z6]
        print("T06: ")
        print(A06)

        print("X: ",x6,"Y: ",y6,"Z: ", z6)

        plt.plot(x6,y6,z6 ,marker=".", color="black")



        

    
        ax.grid(True)
    # Se establecen los límites de los ejes
   
        p.set_data(x, y)
        p.set_3d_properties(z)
      #  ax.scatter(x, y, z)
        # Se fuerza a Python a actualizar la pantalla
        plt.pause(0.1)
    for i in range(n):
        # Variables articulares del brazo robot
        teta[0] = mat_q12[0,i]
        teta[1] = mat_q12[1,i]+np.pi/2
        teta[2] = mat_q12[2,i]+np.pi/2
        teta[3] = mat_q12[3,i]
        teta[4] = mat_q12[4,i]
        teta[5] = mat_q12[5,i]
        d[0]= 0.17
        d[3]= 0.22
        d[5]= 0.1052
        a[1]= 0.22
        alfa[0] = np.pi/2
        alfa[2] = np.pi/2
        alfa[3] = -np.pi/2
        alfa[4] = np.pi/2




        #drawrobot3d4(teta, d, a, alfa)
        #input()
        # Matrices de transformación del primer sistema al correspondiente
        A01 = denavit(teta[0], d[0], a[0], alfa[0])
        A12 = denavit(teta[1], d[1], a[1], alfa[1])
        A23 = denavit(teta[2], d[2], a[2], alfa[2])
        A34 = denavit(teta[3], d[3], a[3], alfa[3])
        A45 = denavit(teta[4], d[4], a[4], alfa[4])
        A56 = denavit(teta[5], d[5], a[5], alfa[5])
        # Matrices de transformación del primer sistema al correspondiente
        A02 = np.dot(A01, A12)
        A03 = np.dot(A02, A23)
        A04 = np.dot(A03, A34)
        A05 = np.dot(A04, A45)
        A06 = np.dot(A05, A56)
        # Vector de posicion (x, y, z) de cada sistema de coordenadas
        x0, y0, z0 = 0, 0, 0
        x1, y1, z1 = A01[0, 3], A01[1, 3], A01[2, 3]
        x2, y2, z2 = A02[0, 3], A02[1, 3], A02[2, 3]
        x3, y3, z3 = A03[0, 3], A03[1, 3], A03[2, 3]
        x4, y4, z4 = A04[0, 3], A04[1, 3], A04[2, 3]
        x5, y5, z5 = A05[0, 3], A05[1, 3], A05[2, 3]
        x6, y6, z6 = A06[0, 3], A06[1, 3], A06[2, 3]
        # Se dibuja el robot
        x = [x0, x1, x2, x3, x4, x5, x6]
        y = [y0, y1, y2, y3, y4, y5, y6]
        z = [z0, z1, z2, z3, z4, z5, z6]
        print("T06: ")
        print(A06)

        print("X: ",x6,"Y: ",y6,"Z: ", z6)

        plt.plot(x6,y6,z6 ,marker=".", color="black")



        

    
        ax.grid(True)
    # Se establecen los límites de los ejes
   
        p.set_data(x, y)
        p.set_3d_properties(z)
      #  ax.scatter(x, y, z)
        # Se fuerza a Python a actualizar la pantalla
        plt.pause(0.1)
    for i in range(n):
        # Variables articulares del brazo robot
        teta[0] = mat_q13[0,i]
        teta[1] = mat_q13[1,i]+np.pi/2
        teta[2] = mat_q13[2,i]+np.pi/2
        teta[3] = mat_q13[3,i]
        teta[4] = mat_q13[4,i]
        teta[5] = mat_q13[5,i]
        d[0]= 0.17
        d[3]= 0.22
        d[5]= 0.1052
        a[1]= 0.22
        alfa[0] = np.pi/2
        alfa[2] = np.pi/2
        alfa[3] = -np.pi/2
        alfa[4] = np.pi/2




        #drawrobot3d4(teta, d, a, alfa)
        #input()
        # Matrices de transformación del primer sistema al correspondiente
        A01 = denavit(teta[0], d[0], a[0], alfa[0])
        A12 = denavit(teta[1], d[1], a[1], alfa[1])
        A23 = denavit(teta[2], d[2], a[2], alfa[2])
        A34 = denavit(teta[3], d[3], a[3], alfa[3])
        A45 = denavit(teta[4], d[4], a[4], alfa[4])
        A56 = denavit(teta[5], d[5], a[5], alfa[5])
        # Matrices de transformación del primer sistema al correspondiente
        A02 = np.dot(A01, A12)
        A03 = np.dot(A02, A23)
        A04 = np.dot(A03, A34)
        A05 = np.dot(A04, A45)
        A06 = np.dot(A05, A56)
        # Vector de posicion (x, y, z) de cada sistema de coordenadas
        x0, y0, z0 = 0, 0, 0
        x1, y1, z1 = A01[0, 3], A01[1, 3], A01[2, 3]
        x2, y2, z2 = A02[0, 3], A02[1, 3], A02[2, 3]
        x3, y3, z3 = A03[0, 3], A03[1, 3], A03[2, 3]
        x4, y4, z4 = A04[0, 3], A04[1, 3], A04[2, 3]
        x5, y5, z5 = A05[0, 3], A05[1, 3], A05[2, 3]
        x6, y6, z6 = A06[0, 3], A06[1, 3], A06[2, 3]
        # Se dibuja el robot
        x = [x0, x1, x2, x3, x4, x5, x6]
        y = [y0, y1, y2, y3, y4, y5, y6]
        z = [z0, z1, z2, z3, z4, z5, z6]
        print("T06: ")
        print(A06)

        print("X: ",x6,"Y: ",y6,"Z: ", z6)

        plt.plot(x6,y6,z6 ,marker=".", color="black")



        

    
        ax.grid(True)
    # Se establecen los límites de los ejes
   
        p.set_data(x, y)
        p.set_3d_properties(z)
      #  ax.scatter(x, y, z)
        # Se fuerza a Python a actualizar la pantalla
        plt.pause(0.1)
    while True:
        time.sleep(1)
    # Código que se ejecutará infinitamente
