import serial
import math
import numpy as numpy

SERVO_MIN = math.radians(-80)
SERVO_MAX = math.radians(80) 
THETA = [0.0,0.0,0.0, 0.0,0.0,0.0]
BETA = [0,math.pi,2*math.pi/3,-math.pi/3,-2*math.pi/3,math.pi/3]

P = [
  [-37.62,37.62,91.20,51.83,-51.83,-91.20],
  [-91.60,-91.60,0,67.77,67.77,0]
  ]

RE = [
  [-74.70,74.70,84.66,20,-20,-84.66],
  [-62.95,-62.95,-45.48,84.80,84.80,-45.48],
  [0,0,0,0,0,0]
  ]

'''
L1-effective length of servo arm, L2 - length of base and platform connecting arm
z_home - height of platform above base, 0 is height of servo arms'''
servo_mult=400/(math.pi/4)
L1 = 20
L2 = 170
z_home = 165

'''arrays used for servo rotation calculation
H[]-center position of platform can be moved with respect to base, this is
translation vector representing this move'''
M = [[],[]]
rxp = [[],[]]
T = []
H = [0,0,z_home]
def base_attach_point(i, th, position_p):
    return (L1 * math.cos(th)*math.cos(BETA[i]) + p[position_p][i])

def getAlpha(i):
   n = 0
   th = 0
   q= [] 
   dl = []
   dl2 = []
   min=SERVO_MIN
   max=SERVO_MAX
   th=THETA[i]

   while(n<20):
    #calculation of position of base attachment point (point on servo arm where is leg connected)
      q.append(base_attach_point(i, th, 0))
      q.append(base_attach_point(i, th, 1))
      q.append(L1*math.sin(th))
      
    #calculation of distance between according platform attachment point and base attachment point
      dl[0] = rxp[0][i] - q[0]
      dl[1] = rxp[1][i] - q[1]
      dl[2] = rxp[2][i] - q[2]
      dl2 = math.sqrt(dl[0]*dl[0] + dl[1]*dl[1] + dl[2]*dl[2])

    #if this distance is the same as leg length, value of theta_a is corrent, we return it
      if(abs(L2-dl2)<0.01):
         return th
    #//if not, we split the searched space in half, then try next value
      if(dl2<L2):
         max=th
      else:
         min=th
      n+=1
      if(max==SERVO_MIN or min==SERVO_MAX):
        return th
      th = min+(max-min)/2
      return th

