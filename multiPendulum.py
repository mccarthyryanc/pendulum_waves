#
# Pendulum Waves Demo
#
# Ryan Schilt May, 2011

from visual import *
from math import *

#ANIMATION PARAMETERS
tickrate = 13
ballsize = 0.01
speed = 50
class framestop:
    def __init__(self,frames):
        self.frames = frames
        self.frame = 0
    def tick(self):
        self.frame += 1
        if self.frame == self.frames:
            self.frame = 0
            return 1
        return 0

#PHYSICS PARAMETERS
#theta0 = -pi/2 + 2*pi/5
theta0 = -pi/4.0
pendNum = 30
g = 9.8
t = 0
delt = 0.0005
thetat = range(pendNum+1)
bpos = range(pendNum+1)
blen = range(pendNum+1)
ball = range(pendNum+1)
string = range(pendNum+1)
vlist = range(pendNum+1)
hinge = range(pendNum+1)

#build n pendulum balls
for i in range(pendNum+1):
	tempOsc = 60.0/(50.0 + float(i))
	blen[i] = g*(tempOsc/(2.0*pi))**2.0
	bpos[i] = (blen[i]*sin(theta0),-blen[i]*cos(theta0),(ballsize*2)*float(i))
	hinge[i] = (0.0,0.0,ballsize*2.0*float(i))

#SCENE PARAMETERS
scene.center = (0,-max(blen)/2.0,((ballsize*2)*float(pendNum)+0.2)/4.0)
scene.title = "Pendulum Waves"

#build walls containing pendulums
rod = cylinder(pos=(0,0,0), axis=(0,0,(ballsize*2)*float(pendNum)), radius=ballsize, color=color.black)
wallR = box(pos=(0,-max(blen)/2.0,-ballsize), size=(2.0*abs(max(blen)*sin(theta0))+ballsize,max(blen)+ballsize*2.0,0.001), color=color.white)
wallL = box(pos=(-abs(max(blen)*sin(theta0))-ballsize,-max(blen)/2.0,((ballsize*2)*float(pendNum))/2.0), size=(0.001,max(blen)+ballsize*2.0,(ballsize*2)*float(pendNum)), color=color.white)
wallB = box(pos=(0,-max(blen)-ballsize,((ballsize*2)*float(pendNum))/2.0), size=(2.0*abs(max(blen)*sin(theta0)),0.001,(ballsize*2)*float(pendNum)), color=color.white)

#Cleanup
removal = []
init = 0

#Timeline control
while 1:
    if init == 0:
        #Visual objects
        for i in range(pendNum+1):
			ball[i] = sphere(pos=(bpos[i]),radius=ballsize,color=color.yellow)
			string[i] = curve(pos=[ball[i].pos,hinge[i]])
        init = 1
    if scene.mouse.clicked == 1:
        c = scene.mouse.getclick()
        init = 0
        for i in range(pendNum+1):
			removal.append(ball[i])
			removal.append(string[i])
			vlist[i] = []
        stopper = framestop(tickrate)
        while 1:
            rate(speed)
            if stopper.tick():
				for i in range(pendNum+1):
					vlist[i].append(copy(ball[i]))
            for i in range(pendNum+1):
				t += delt
				thetat[i] = theta0*cos(sqrt(g/blen[i])*t)
				ball[i].pos = (blen[i]*sin(thetat[i]),-blen[i]*cos(thetat[i]),(ballsize*2)*float(i))
				string[i].pos=[ball[i].pos,hinge[i]]

    

