from __future__ import division
from visual import *
from visual.graph import *

#Drop parameters
m = 10    #mass to be dropped (kg)
h = 10      #height to be dropped from (m)
lr = 3     #length of rope (m)
ls = 1     #length of unstretched spring (m)
mh = 0.1   #height of the mass (m)
k = 49     #spring constant (N/m)
g = 9.8    #gravitational field constant (N/kg)
deltax = 0 #distance the spring has stretched (m)
dt = 0.00001 #size of time steps for simulation (s)


platform = box(pos=(-2,h/2,0),size=(1,h,5))
floor = box(pos=(0,-.00005,0),size=(4,.0001,h),color=color.blue)

mass = cylinder(pos=(0,h,0),axis=(0,mh,0), radius = 0.1)
mass.velocity = vector(0,0,0)



aplot=gcurve(color=color.cyan)
vplot = gcurve(color=color.green)
posplot = gcurve(color=color.blue)

t=0
v = mass.velocity.y
while (h-mass.pos.y) < (lr+ls):
    rate(100000)
    mass.pos.y = h-(0.5*g*t**2+v*t)
    mass.velocity.y = g*t 
    t += dt
    posplot.plot(pos=(t,mass.pos.y))
    aplot.plot(pos=(t,g))
    vplot.plot(pos=(t,mass.velocity.y))
    
#print mass.pos,mass.velocity
vel2 = mass.velocity.y

t1=t
t=0
while mass.velocity.y > 0:
    rate(100000)
    deltax= (h-lr-ls)-mass.pos.y
    
    a = g-(k/m)*deltax
    aplot.plot(pos=(t+t1,a))
    mass.pos.y -= 0.5*a*dt**2+mass.velocity.y*dt
    mass.velocity.y += a*dt
    posplot.plot(pos=(t+t1,mass.pos.y))
    vplot.plot(pos=(t+t1,mass.velocity.y))
    t+=dt
    #print 
    if mass.pos.y < -mh:
        splat = True
        print "SPLAT!"
        print "delta x:",deltax,"velocity:",mass.velocity,"position:",mass.pos
        break
if not splat:
    print "Well, you didn't splatter. Let's see if you made it"
    print "delta x:",deltax,"velocity:",mass.velocity,"position:",mass.pos
