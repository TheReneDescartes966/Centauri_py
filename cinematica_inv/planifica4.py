import numpy as np
from inversekinematic import inversekinematic4

def planifica4(p1, p2, n, s, a, npuntos):
    # Cálculo del vector unitario
    u = np.array(p2) - np.array(p1)
    mu = np.sqrt(u[0]**2 + u[1]**2 + u[2]**2)
    u = (1 / mu) * u
    
    # Cálculo de la distancia entre puntos
    dl = mu / (npuntos + 1)
    
    grados_x = np.radians(0)
    grados_y = np.radians(0)
    grados_z = np.radians(180)
    matriz_z = np.array([[np.cos(grados_z),-1*np.sin(grados_z),0,0],
                         [np.sin(grados_z),np.cos(grados_z),0,0],
                         [0,0,1,0],
                         [0,0,0,1]])
    matriz_x = np.array([[1,0,0,0],
                         [0,np.cos(grados_x),-1*np.sin(grados_x),-0.1],
                         [0,np.sin(grados_x),np.cos(grados_x), 0],
                         [0,0,0,1]])
    matriz_y = np.array([[np.cos(grados_y),0,np.sin(grados_y),0],
                         [0,1,0,0],
                         [-1*np.sin(grados_y),0,np.cos(grados_y),0],
                         [0,0,0,1]])
    

    matriz = np.dot(np.dot(matriz_x,matriz_y),matriz_z)
    
    # Inicialización de la matriz mat_q
    mat_q = np.zeros((6, npuntos + 2))
    #print(mat_q)
    for i in range(npuntos + 2):
        # Cálculo de la posición cartesiana actual de la mano del manipulador
        p = p1 + (i * dl) * u
        
        Tr = np.array([n, s, a, p]).T
        # Cálculo de las coordenadas articulares
        Tr = np.append(Tr,[[0,0,0,1]],axis=0)

        Tr = np.dot(matriz,Tr)

        q = inversekinematic4(Tr)
        mat_q[:, i] = q.flatten()
        #print(q)
        #input()
    return mat_q