import numpy as np
from denavit import denavit
from math import atan2



def inversekinematic4(Tdes):
    l0 = 0.17
    l1 = 0.22
    l2 = 0.22
    l3 = 0.1052
    print("Tdes: ")
    print(Tdes)

    pmx= Tdes[0,3]-l3*Tdes[0,2]
    pmy= Tdes[1,3]-l3*Tdes[1,2]
    pmz= Tdes[2,3]-l3*Tdes[2,2]
    print("pmx=",pmx, "pmy=", pmy, "pmz=", pmz)
    q1=np.arctan2(pmy,pmx)
    if q1==0:
        q1+=np.pi
    R=np.sqrt(pmx**2+pmy**2+(pmz-l0)**2)
    r=np.sqrt(pmx**2+pmy**2)
    print("R:", R)
    print("r:", r)
    cq3 = (R**2-l1**2-l2**2)/(2*l1*l2)
    q3 = np.arctan2(np.sqrt(1-cq3**2),cq3)
    q2 =  np.pi/2 - np.arctan2(pmz-l0,r) - np.arctan2(l2*np.sin(q3),l1+l2*cq3)



    # Resultado
    #print(np.degrees(q1))
    ROT03 = [[-np.cos(q1)*np.cos(q2+q3), np.sin(q1), -np.sin(q2 + q3)*np.cos(q1)], 
            [-np.sin(q1)*np.cos(q2 + q3), -np.cos(q1), -np.sin(q1)*np.sin(q2 + q3)], 
            [-np.sin(q2 + q3), 0, np.cos(q2 + q3)]] 
    
    #print("ROT03:")
    #print(np.round(ROT03,4))
    
    ROT06=Tdes[0:3,0:3]


    #print("ROT06: ")
    #print(np.round(ROT06,4))

    ROT36= np.dot(np.transpose(ROT03),ROT06)
    
    #print("ROT36: ")
    #print(ROT36)

    nx= ROT36[0,0]
    ox= ROT36[0,1]
    ax= ROT36[0,2]
    ny= ROT36[1,0]
    oy= ROT36[1,1]
    ay= ROT36[1,2]
    nz= ROT36[2,0]
    oz= ROT36[2,1]
    az= ROT36[2,2]
    q4=np.arctan2(ay,ax)
    #q5=np.arctan2(ay/np.sin(q4),az)
    q5=np.arctan2(np.sqrt(1-(az)**2),az)
    q6=np.arctan2(oz,-nz)
    print("q de las inversas:")
    print(q1, q2, q3, q4, q5, q6)
    q = np.array([q1, q2, q3, q4, q5, q6]).T
    return (q)



    # Solución de la primera articulación: q1
