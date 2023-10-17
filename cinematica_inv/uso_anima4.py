from planifica4 import planifica4
from animacion4 import animacion4
import numpy as np
from inversekinematic import inversekinematic4
from drawrobot3d4 import drawrobot3d4

p1=[-0.4,-0.05,0.4] #u
p2=[-0.4, -0.05, 0]
p3=[-0.3, -0.05 ,0]
p4=[-0.3, -0.05, 0.4]


p5=[-0.2, -0.05, 0] #empieza a
p6=[-0.2, -0.05, 0.4]
p7=[-0.1, -0.05, 0.4]
p8=[-0.1, -0.05, 0.0]

p9=[-0.1, -0.05, 0.2]
p10=[-0.2, -0.05, 0.2]

p11=[0.0, -0.05, 0.4] 
p12=[0.1, -0.05, 0.4]
p13=[0.1, -0.05, 0]
p14=[0.0, -0.05, 0]
p15=[0.0, -0.05, 0.4]

#n= [1,0,0]
#s = [0,1,0]
#a = [0,0,1]

#n = [5.83616981e-02 , 9.98295139e-01 , 8.52612103e-04  ]
#s = [ 8.16903822e-01 ,-4.72663665e-02, -5.74833921e-01 ]
#a = [-5.73813610e-01 , 3.42447859e-02 ,-8.18269660e-01 ]



n=[0.05999119, 0.02659445, -0.99784457]
s=[-0.05663413, -0.99794411, -0.03000199 ]   
a=[-0.99659101, 0.05831192, -0.0583617]

#n=[0.06600662 ,0.98794394,-0.14003534]
#s=[ 0.04949236 ,-0.14341022,-0.98842502]
#a=[-0.99659101,0.05831192 , -0.0583617]

#n=[0 ,0,-1]
#s=[ 0,1,0]
#a=[1,0, 0]

npuntos=10

l0 = 0.17
l1 = 0.22
l2 = 0.22
l3 = 0.1052

q = [0, 0, 0, 0, 0, 0]

teta = np.array([q[0], q[1]+np.pi/2, q[2]+np.pi/2, q[3],q[4],q[5]])
d = np.array([l0, 0, 0, l2, 0,l3])
al = np.array([0, l1, 0, 0, 0, 0])
alfa = np.array([np.pi/2, 0, np.pi/2, -np.pi/2, np.pi/2, 0])
#drawrobot3d4(teta, d, al, alfa)
mat_q=planifica4(p1, p2, n, s, a, npuntos)
mat_q1=planifica4(p2, p3, n, s, a, npuntos)
mat_q2=planifica4(p3, p4, n, s, a, npuntos)#u

mat_q3=planifica4(p4, p5, n, s, a, npuntos)

mat_q4=planifica4(p5, p6, n, s, a, npuntos)
mat_q5=planifica4(p6, p7, n, s, a, npuntos)
mat_q6=planifica4(p7, p8, n, s, a, npuntos)
mat_q7=planifica4(p8, p9, n, s, a, npuntos)
mat_q8=planifica4(p9, p10, n, s, a, npuntos)

mat_q9=planifica4(p10, p11, n, s, a, npuntos)

mat_q10=planifica4(p11, p12, n, s, a, npuntos)
mat_q11=planifica4(p12, p13, n, s, a, npuntos)
mat_q12=planifica4(p13, p14, n, s, a, npuntos)
mat_q13=planifica4(p14, p15, n, s, a, npuntos)
#print(mat_q)
animacion4(mat_q,mat_q1,mat_q2,mat_q3,mat_q4,mat_q5,mat_q6,mat_q7,mat_q8,mat_q9,mat_q10,mat_q11,mat_q12,mat_q13,teta,d,al,alfa)



