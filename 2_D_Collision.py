from visual import *


ball1 = sphere(pos=(5,0,0), radius=0.5, color=color.blue)
ball2 = sphere(pos=(0,5,0), radius=0.5, color=color.red)
ball1.mass = 1
ball2.mass = 1


ball1.velocity = vector(-1,0,0)
ball2.velocity = vector(0,-1,0)
refFrame = ball2.velocity

ball1.relSpeed = linalg.norm(ball1.velocity-refFrame)
ball2.relSpeed = linalg.norm(ball2.velocity-refFrame)

print ball1.relSpeed
print ball2.relSpeed
 
theta = arctan((ball1.pos.y-ball2.pos.y)/(ball1.pos.x-ball2.pos.x))
print theta

collide = false

foo = true
dt = .01

ball1.trail = curve(color=ball1.color)
ball2.trail = curve(color=ball2.color)
com = curve(color=color.green)

def comCalc(m1,m2,r1,r2):
    return (m1*r1+m2*r2)/(m1+m2)

def collision(m1,m2,v1,v2):
    v2fMag = (2*m1*v1)/(m1+m2)
    v1fMag = (m1-m2)/(m1+m2)*v1
    print v1fMag,v2fMag
    
    print vector(v1fMag*cos(theta),v1fMag*sin(theta),0)
    print vector(-v2fMag*cos(theta),v2fMag*sin(theta),0)
    
    v1f = vector(v1fMag*cos(theta),v1fMag*sin(theta),0)+refFrame
    v2f = vector(v2fMag*cos(theta),v2fMag*sin(theta),0)+refFrame
    print "v1f and v2f =",v1f,v2f
    return v1f,v2f

while foo:
    rate(100)
    ball1.pos += ball1.velocity*dt
    ball2.pos += ball2.velocity*dt
    ball1.trail.append(ball1.pos)
    ball2.trail.append(ball2.pos)
    com.append(comCalc(ball1.mass,ball2.mass,ball1.pos,ball2.pos))
    d = linalg.norm(ball1.pos-ball2.pos)
    
    if d < ball1.radius and collide == false:
        ball1.velocity, ball2.velocity = collision(ball1.mass,ball2.mass,ball1.relSpeed,ball2.relSpeed)
        print ball1.velocity, ball2.velocity
        collide = true
